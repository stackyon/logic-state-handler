import chess


class Model():

    board = 0

    @staticmethod #may want to have a game instance containing a model instance to run multiple games instead
    def get_player_move():
        #get move from vision
        move_message = '233'   # placeholder
        player_move = build_move(move_message)
        return player_move

    @staticmethod
    def reset():
        board = chess.board
