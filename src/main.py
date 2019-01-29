"""

The runtime loop loops each turn
The model is updated
Either the user or AI move is performed each loop

"""

import model
import statecontroller
import ai
import buffer


terminate = False

while not terminate:
    buffer.read_buffer()
    if not statecontroller.is_error():
        irs_move_code = buffer.read_buffer()
        model.record_move(irs_move_code)
        ai.get_ai_move()
    else:
    # check movement status and do recordmove()
    # update model refresh() and confirm consistency
    # update state refreshstate()
    # update movement queue with new moves from AI
