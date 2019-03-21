"""
Receive update from IRS
buttonPressed, changeCode, moveCode

"""

import movetools
import statecontroller


def read_buffer(dummy_buffer):
    # read from the server instead of dummy

    move_codes = dummy_buffer.split(',')
    if move_codes[1] == 'm':
        return movetools.build_move(move_codes[2])
    if move_codes[1] == 'e':
        statecontroller.error(move_codes[2])
    else:
        print('INVALID BUFFER!')
