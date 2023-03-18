#!/usr/bin/python3

from flask import Flask
import Gpib
from markupsafe import escape
import signal
import sys
import time

from multiprocessing import Process, Value, Array


## General GP-IB Setup ##
interface_id = 0 # Interface number of the GP-IB
device_address = 7 # Address of the test insturment

device = Gpib.Gpib(interface_id,device_address)


## DMM Example ##
# set DC voltage for PSU range
#device.write("CONF:VOLT:DC 50,0.0005")
# read measurement back converted from scientific notation
#device.write("READ?")
#print(float(device.read(100)))


dmm_value=Value('d', 0.0)
ending=Value('d', 0.0)

start=time.time()

def dmm_update(dmm_value,ending):

    while(ending.value==0):
        # write a command
        #device.write("*IDN?") # Standard SCPI identification command
        try:
            device.write("READ?")
            data=float(device.read(100))
            device.ibloc()
        except:
            data=float("NaN")
        dmm_value.value=data
        # read data back and print
        # Read up to 100 bytes
        try:
            time.sleep(3)
        except KeyboardInterrupt:
            return

procs = []
proc = Process(target=dmm_update, args=(dmm_value, ending))  # instantiating without any argument
procs.append(proc)
proc.start()

app = Flask("The Script about the DMM GUI")

@app.route("/inst/dmm/fetch.json")
def inst_dmm_fetch():
    return {"fetch":round(dmm_value.value,2)}

@app.route("/refresh/fetch.json")
def refresh_fetch():
    return {"fetch":start}

@app.route("/")
def hello_world():
    return " <link rel=\"stylesheet\" type=\"text/css\" href=\"/static/content/styles/main.css\" /><script src=\"/static/content/scripts/test.js\"></script><div id=\"p1080\"><p id=\"red\"></p></div>"


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


app.run(host="0.0.0.0")

print("post run")


ending.value=1

for proc in procs:
    proc.join()
