import movementqueue
import model
import movetools
import statecontroller


class AI:
    @staticmethod
    def get_ai_move(dummy_uci):
        ai_move_code = dummy_uci    # get uci from server instead of dummy
        model.Model.enter_move(ai_move_code)
        if not statecontroller.Controller.current_state == 'error':
            ai_move = movetools.build_move(ai_move_code)
            movementqueue.add_move(ai_move)
        else:
            print('AI MOVE ERRONEOUS!')
