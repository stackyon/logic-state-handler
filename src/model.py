import chess
import movetools
import statecontroller
import tomb


class Model:

    def __init__(self):
        self.chess_board = chess.Board()
        self.graveyard = []
        self.occupied_tombs = [0]*32    # initialize as all unoccupied
        self.saves = []

    def enter_move(self, move_uci):
        if chess.Move.from_uci(move_uci) in self.chess_board.legal_moves:
            pc_move = chess.Move.from_uci(move_uci)     # python-chess move type
            if self.chess_board.is_capture(pc_move) \
                    and not self.chess_board.piece_at(pc_move.to_square).piece_type == chess.PAWN:
                self.entomb(self.chess_board.piece_at(pc_move.to_square))
            self.chess_board.push(pc_move)
            print(self.to_string())
        else:
            statecontroller.error('Illegal Move')

    def entomb(self, piece):
        position = None
        for i in range(0, len(self.occupied_tombs) - 1):
            if self.occupied_tombs[i] == 0:
                position = i
                break
        if position is not None:
            self.occupied_tombs[position] = 1
            self.graveyard.append(tomb.Tomb(piece, position))
            print(self.graveyard_to_string())
        else:
            print('Grave is full!')

    def reset(self):
        self.chess_board = chess.Board()

    def save_board(self):
        # returns save file_num
        new_save = self.chess_board.board_fen()
        self.saves.append(new_save)
        return len(self.saves) - 1

    def load_board(self, file_num):
        save = self.saves[file_num]
        self.chess_board.set_board_fen(save)
        print(self.to_string())

    def load_board_from_file(self, filename, index_in_file):
        file = open(filename)
        line = ''
        for i in range(0, index_in_file + 1):
            line = file.readline()
        self.chess_board.set_board_fen(line)
        file.close()
        print(self.to_string())

    def castle_short(self):
        pass

    def graveyard_to_string(self):
        representation = ''
        for current_tomb in self.graveyard:
            representation += 'piece ' + current_tomb.piece.symbol() + ' in tomb ' + str(current_tomb.position) + '\n'
        return representation + '\n'

    def to_string(self):
        return self.chess_board.unicode().replace(u'.', u'〼').replace(u'·', u'〼') + '\n\n'
