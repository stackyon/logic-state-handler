import chess
import movementqueue


class AI:
    def get_ai_move(self):
        # reference model
        # call ai based on model
        # create move(chess.A1, chess.B2, chess.Piece(type, color))
        # send move to movement queue
        ai_move = 'this will be a move'
        for movement in ai_move.movements:
            movementqueue.add_movement()