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

    def test_buffer(self):
        move1 = buffer.read_buffer('p,m,e2e3')
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
        move1 = buffer.read_buffer('p,m,c2c3')
        model.Model.record_player_move(move1)
        movementqueue.add_move(move1)
        fish = ai.StockfishAI()
        fish.get_ai_move()
        movementqueue.print_queue()

    def test_entomb(self):
        game = model.Model()
        game.entomb(game.chess_board.piece_at('e2'))
        for tomb in game.graveyard:
            print('' + tomb.piece.piece_type + ' ' + tomb.position)

    # helper functions
    def user_move(self):
        move1 = buffer.read_buffer('p,m,e2e3')
        model.Model.record_player_move(move1)


if __name__ == '__main__':
    unittest.main()

