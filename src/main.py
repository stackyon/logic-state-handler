"""

The runtime loop loops each turn
The model is updated
Either the user or AI move is performed each loop

"""

import model
import statecontroller
import ai
import buffer
import movementqueue
import movetools
import time


terminate = False

game = model.Model()
fish = ai.StockfishAI()

while not terminate:
    irs_code = buffer.read_buffer()
    if statecontroller.is_ready():
        statecontroller.wait()  # current buffer has been acted upon
        game.enter_move(irs_code)
        if not statecontroller.is_error():
            ai_uci = fish.get_ai_uci(game)
            entombment = game.enter_move(ai_uci)
        if not statecontroller.is_error():
            if not entombment == '':
                movementqueue.add_move(movetools.build_move(entombment))
            movementqueue.add_move(movetools.build_move(ai_uci))
            print(movementqueue.to_string())
    elif statecontroller.is_error():
        # determine undo if board error, add to movement queue
        print('player move was invalid!')
        while statecontroller.is_error():
            # wait for error to be cleared by new buffer
            buffer.read_buffer()
    elif statecontroller.is_wait():
        while statecontroller.is_wait():
            # wait for new buffer to execute
            buffer.read_buffer()
    else:
        print('Unknown state!')
        time.sleep(2)
