# =============================================================================
# CREDITS
# =============================================================================
# Author : Tanguy BOULARD
# Date   : 28/06/2021
# Script : Keysight

# =============================================================================
# MODULES
# =============================================================================

import pyvisa
import sys

# =============================================================================
# FUNCTIONS
# =============================================================================

def Read(instrument):
    return float(Query(instrument, "MEAS:PRIM:VOLT:DC?"))

def Write(instrument, command):
    instrument.write(command)
    Error(instrument)

def Query(instrument, command):
    value = instrument.query(command)
    Error(instrument)
    return value

def Error(instrument):
    err = instrument.query(":SYST:ERR?")
    if int(err[1]) != 0:
        print(err, end="\n\r")
        # sys.exit()

def Initialize():
    rm = pyvisa.ResourceManager()
    # print(rm.list_resources())
    
    instrument = rm.open_resource("USB0::0x2A8D::0xB318::MY58020033::INSTR")
    instrument.read_termination = "\n"
    instrument.write_termination = ""
    instrument.baud_rate = 9600
    if (Query(instrument, "*IDN?")!= "Keysight Technologies,34450A,MY58020033,01.02-01.00"):
        print("KEYSIGHT 34450A not connected")
        sys.exit()
    instrument.clear()
    instrument.query(":SYST:ERR?")
    Write(instrument, "*RST")
    Write(instrument, "*CLS")
    Write(instrument, ":CONF:VOLT:DC")
    
    return instrument
    
def Close(instrument):
    pyvisa.ResourceManager().open_resource("USB0::0x2A8D::0xB318::MY58020033::INSTR").clear()
    instrument.close()