import unittest
import buffer
import movetools


class TestFlow(unittest.TestCase):

    def test_coordinates(self):
        coords = movetools.coordinates('e1')
        assert coords[0] == 5
        assert coords[1] == 1

    def test_buffer(self):
        move1 = buffer.read_buffer()
        assert move1.movements[0].movement_type == 'up'
        assert move1.movements[0].square_x == 5
        assert move1.movements[0].square_y == 1
        assert move1.movements[1].movement_type == 'down'
        assert move1.movements[1].square_x == 5
        assert move1.movements[1].square_y == 2

    """
def test_record_move(self):

def test_ai_move(self):
    """


if __name__ == '__main__':
    unittest.main()

