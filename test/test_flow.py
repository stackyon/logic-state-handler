import unittest
import buffer
import movetools
import model
import ai
import movementqueue
import chess


class TestFlow(unittest.TestCase):

    def test_coordinates(self):
        x_y = movetools.coordinates('e1')
        assert x_y[0] == 5
        assert x_y[1] == 1

    def test_build_move(self):
        move1 = movetools.build_move('e2e3')
        assert move1.movements[0].movement_type == 'up'
        assert move1.movements[0].square_x == 5
        assert move1.movements[0].square_y == 2
        assert move1.movements[1].movement_type == 'down'
        assert move1.movements[1].square_x == 5
        assert move1.movements[1].square_y == 3

    def test_record_move(self):
        move1 = buffer.read_buffer('p,m,e2e3')
        model.Model.record_player_move(move1)

    def test_add_move(self):
        move1 = buffer.read_buffer('p,m,c2c3')
        movementqueue.add_move(move1)
        movementqueue.print_queue()

    def test_ai_uci(self):
        self.user_move()
        fish = ai.StockfishAI()
        uci = fish.get_ai_uci()
        assert len(uci) == 4

    def test_both_move(self):
        game = model.Model()
        move1 = movetools.build_move('c2c3')
        game.record_player_move(move1)
        fish = ai.StockfishAI()
        ai_uci = fish.get_ai_uci(game)
        game.enter_move(ai_uci)
        movementqueue.print_queue()

    def test_entomb(self):
        game = model.Model()
        game.entomb(game.chess_board.piece_at(chess.E2))
        self.print_graveyard(game)

    def test_multi_entomb_delete(self):
        game = model.Model()
        game.entomb(game.chess_board.piece_at(chess.E2))
        game.entomb(game.chess_board.piece_at(chess.E1))
        self.print_graveyard(game)

    # helper functions
    def user_move(self):
        move1 = buffer.read_buffer('p,m,e2e3')
        model.Model.record_player_move(move1)

    def print_graveyard(self, game):
        for tomb in game.graveyard:
            print('' + tomb.piece.symbol() + ' ' + str(tomb.position))


if __name__ == '__main__':
    unittest.main()

