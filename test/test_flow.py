import unittest
import buffer
import movetools
import model


class TestFlow(unittest.TestCase):

    def test_coordinates(self):
        x_y = movetools.coordinates('e1')
        assert x_y[0] == 5
        assert x_y[1] == 1

    def test_buffer(self):
        move1 = buffer.read_buffer('p,m,e1e2')
        assert move1.movements[0].movement_type == 'up'
        assert move1.movements[0].square_x == 5
        assert move1.movements[0].square_y == 1
        assert move1.movements[1].movement_type == 'down'
        assert move1.movements[1].square_x == 5
        assert move1.movements[1].square_y == 2

    def test_record_move(self):
        move1 = buffer.read_buffer('p,m,c2c3')
        model.Model.record_player_move(move1)


"""
def test_ai_move(self):
"""


if __name__ == '__main__':
    unittest.main()

