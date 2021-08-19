# =============================================================================
# CREDITS
# =============================================================================
# Author : Tanguy BOULARD
# Date   : 28/06/2021
# Script : Gentec-EO P-Link

# =============================================================================
# MODULES
# =============================================================================

import pyvisa
import sys

# =============================================================================
# FUNCTIONS
# =============================================================================

def Read(instrument):
    instrument.write("*CVU")
    instrument.read()  # ACK
    return float(instrument.read()) # VALUE

def Query(instrument, command):
    value = instrument.query(command)
    return value

def Initialize(wavelength):
    rm = pyvisa.ResourceManager()
    # print(rm.list_resources())
    
    instrument = rm.open_resource("ASRL5::INSTR")
    instrument.read_termination = "\r\r\n"
    instrument.write_termination = "\n"
    instrument.baud_rate = 57600
    instrument.delay = 100
    if Query(instrument, "*NAM") != "UP19K-30H-H5\t":
        print("Gentec-eo U-link not connected")
        sys.exit()
    instrument.clear()
    Query(instrument, "*ANT")
    Query(instrument, "*CFT")
    Query(instrument, "*CMX")
    Query(instrument, "*FAS")
    l = len(str(wavelength))
    if l != 4:
        for i in range(l):
            wavelength = "0" + wavelength[:]
    Query(instrument, "*PWC%s" % str(wavelength))
    Query(instrument, "*MUL10.0E+00")
    
    return instrument
    
def Close(instrument):
    Query(instrument, "*RST")
    instrument.close()
    return 1