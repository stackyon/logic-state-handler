"""
Receive update from IRS
buttonPressed, changeCode, moveCode

"""

import movetools
import statecontroller


class BufferHold:
    last_buffer = ''


def read_buffer():
    # read from the server instead of dummy
    new_buffer = 'p,m,' + input('next move: ')
    if not new_buffer == BufferHold.last_buffer:
        BufferHold.last_buffer = new_buffer   # remember this input so it isn't duplicated
        move_codes = new_buffer.split(',')
        if move_codes[1] == 'm':
            statecontroller.ready()
            return move_codes[2]    # move uci
        if move_codes[1] == 'e':
            print('A new error was received!')
            statecontroller.error(move_codes[2])
            return move_codes[2]    # error code
        else:
            print('Invalid buffer!')
