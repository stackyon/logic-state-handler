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
    buffer.read_buffer('p,m,e2e3')
    if not statecontroller.is_error():
        irs_move_code = buffer.read_buffer('p,m,e2e3')
        model.Model.record_player_move(irs_move_code)
        ai.AI.get_ai_move('a7a5')
    else:
        # determine undo if board error, add to movement queue
        print('player move was invalid')
    terminate = True
