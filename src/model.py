import chess
import movetools
import buffer


class Model:
    chess_board = 0

    @staticmethod #may want to have a game instance containing a model instance to run multiple games instead
    def get_player_move():
        #get move from vision
        move_message = buffer.read_buffer()
        player_move = movetools.build_move(move_message)
        return player_move

    @staticmethod
    def record_move(p_move):
        move_uci = p_move.move[1], p_move.move[2]
        chess.Move.from_uci(move_uci) in Model.chess_board.legal_moves

    @staticmethod
    def reset():
        Model.chess_board = chess.Board()
