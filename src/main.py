"""

The runtime loop loops each turn
The model is updated
Either the user or AI move is performed each loop

"""

import model
import statecontroller
import ai


terminate = False

while not terminate:
    if not statecontroller.is_error():
        player_move = model.get_player_move()
        model.record_move(player_move)
        ai.get_ai_move()
    else:
    # check movement status and do recordmove()
    # update model refresh() and confirm consistency
    # update state refreshstate()
    # update movement queue with new moves from AI
