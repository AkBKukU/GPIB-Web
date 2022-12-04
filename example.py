#!/usr/bin/python3
import Gpib

## General GP-IB Setup ##
interface_id = 0 # Interface number of the GP-IB 
device_address = 7 # Address of the test insturment

device = Gpib.Gpib(interface_id,device_address) 

# write a command
device.write("*IDN?") # Standard SCPI identification command
# read data back and print
print(device.read(100)) # Read up to 100 bytes

## DMM Example ##
# set DC voltage for PSU range
device.write("CONF:VOLT:DC 50,0.0005")
# read measurement back converted from scientific notation
device.write("READ?")
print(float(device.read(100)))
