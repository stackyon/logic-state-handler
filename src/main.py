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


terminate = False

fish = ai.StockfishAI()

while not terminate:
    irs_move_code = buffer.read_buffer()
    if not statecontroller.is_error():
        model.Model.record_player_move(irs_move_code)
        fish.get_ai_move()
        movementqueue.print_queue()
    else:
        # determine undo if board error, add to movement queue
        print('player move was invalid')
