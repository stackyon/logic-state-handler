import chess
import movetools
import statecontroller
import tomb


class Model:

    def __init__(self):
        self.chess_board = chess.Board()
        self.graveyard = []
        self.occupied_tombs = [0]*32    # initialize as all unoccupied

    def record_player_move(self, player_move):
        move_uci = movetools.get_uci(player_move)
        self.enter_move(move_uci)

    def enter_move(self, move_uci):
        if chess.Move.from_uci(move_uci) in self.chess_board.legal_moves:
            pc_move = chess.Move.from_uci(move_uci) # python-chess move type
            if self.chess_board.is_capture(pc_move):
                self.entomb(self.chess_board.piece_at(pc_move.to_square))
            self.chess_board.push(pc_move)
            print(self.chess_board.unicode().replace(u'.', u'〼'))
            print('\n')
        else:
            statecontroller.error('Illegal Move')

    def entomb(self, piece):
        position = 0
        for i in range(1, len(self.occupied_tombs)):
            if self.occupied_tombs.get(i) == 0:
                position = i
                break
        if position != 0:
            self.graveyard.append(tomb.Tomb(piece, position))
        else:
            print('Graveyard is full!')

    def reset(self):
        self.chess_board = chess.Board()
