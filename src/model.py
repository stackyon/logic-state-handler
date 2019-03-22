import chess
import movetools


class Model:

    chess_board = chess.Board()

    @staticmethod
    def record_player_move(player_move):
        move_uci = movetools.get_uci(player_move)
        Model.enter_move(move_uci)

    @staticmethod
    def enter_move(move_uci):
        if chess.Move.from_uci(move_uci) in Model.chess_board.legal_moves:
            Model.chess_board.push(chess.Move.from_uci(move_uci))
            print(Model.chess_board.unicode().replace(u'.', u'〼'))
            print('\n')
        else:
            print('ILLEGAL MOVE!')

    @staticmethod
    def reset():
        Model.chess_board = chess.Board()
