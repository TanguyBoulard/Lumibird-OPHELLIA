# =============================================================================
# CREDITS
# =============================================================================
# Author : Tanguy BOULARD
# Date   : 28/06/2021
# Script : Data processing

# =============================================================================
# MODULES
# =============================================================================

import PRO8000

import pyvisa
import sys
import time

# =============================================================================
# FUNCTIONS
# =============================================================================

def Timer(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer, end='\n\r')
        time.sleep(1)
        t -= 1
    print('FIN')
    return 1

def main(I, T, t):

    pro8000 = PRO8000.Initialize(T, I)
    Timer(int(t))
    PRO8000.Close(pro8000)
    

def Stop():
    rm = pyvisa.ResourceManager()
    pro8000 = rm.open_resource("ASRL8::INSTR")
    PRO8000.Close(pro8000)
    sys.exit()