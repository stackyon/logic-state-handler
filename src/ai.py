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

    def get_ai_uci(self, game):
        self.engine.position(game.chess_board)
        move = self.engine.go(movetime=2000)
        return move.bestmove.uci()
