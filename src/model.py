import chess
import movetools
import buffer


class Model:
    chess_board = 0

    @staticmethod
    def record_player_move(move_message):
        player_move = movetools.build_move(move_message)
        move_uci = player_move.move[1], player_move.move[2]
        enter_move(move_uci)

    @staticmethod
    def enter_move(move_uci):
        chess.Move.from_uci(move_uci) in Model.chess_board.legal_moves

    @staticmethod
    def reset():
        Model.chess_board = chess.Board()
