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

while not terminate:
    buffer.read_buffer()
    if not statecontroller.is_error():
        irs_move_code = buffer.read_buffer()
        model.record_player_move(irs_move_code)
        ai_move = ai.record_ai_move()
        for movement in ai_move.movements:
            movementqueue.add_movement(movement)
    else:
        # determine undo if board error, add to movement queue
        print('player move was invalid')

