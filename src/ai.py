import movementqueue
import model
import movetools
import statecontroller
from chess import uci
from config import STOCKFISH_PATH


class StockfishAI:
    def __init__(self):
        # Open stockfish engine and run it
        self.engine = uci.popen_engine(STOCKFISH_PATH)
        self.engine.uci()

    def get_ai_uci(self):
        self.engine.position(model.Model.chess_board)
        move = self.engine.go(movetime=2000)
        return move.bestmove

    def get_ai_move(self):
        ai_move_code = self.get_ai_uci()    # get uci from stockfish AI
        model.Model.enter_move(ai_move_code)
        if not statecontroller.Controller.current_state == 'error':
            ai_move = movetools.build_move(ai_move_code)
            movementqueue.add_move(ai_move)
        else:
            print('AI MOVE ERRONEOUS!')
