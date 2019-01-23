"""
Receive update from IRS
buttonPressed, changeCode, moveCode

"""

import movetools
import statecontroller


def read_buffer():
    #read from the server
    dummy_buffer = 'p,m,e1e2'

    move_codes = dummy_buffer.split(',')
    if move_codes[1] == 'm':
        movetools.build_move(move_codes[2])
    if move_codes[1] == 'e':
        statecontroller.error(move_codes[2])
