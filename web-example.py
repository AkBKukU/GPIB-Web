#!/usr/bin/python3

from flask import Flask
import Gpib
from markupsafe import escape

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

app = Flask(__name__)

@app.route("/inst/dmm/fetch.json")
def inst_dmm_fetch():
# write a command
    #device.write("*IDN?") # Standard SCPI identification command
    try:
        device.write("READ?")
        data=float(device.read(100))
        device.ibloc()
    except:
        data=""
    # read data back and print
    # Read up to 100 bytes
    return {"fetch":data}

@app.route("/")
def hello_world():
    return " <link rel=\"stylesheet\" type=\"text/css\" href=\"/static/content/styles/main.css\" /><script src=\"/static/content/scripts/test.js\"></script><p id=\"red\"></p>"

