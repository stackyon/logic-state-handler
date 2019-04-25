import unittest
import buffer
import movetools
import model
import ai
import movementqueue
import chess
import statecontroller
from config import DEMO_BOARDS


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

    def test_movement_queue(self):
        movementqueue.add_move(movetools.build_move('e2e3'))
        print(movementqueue.to_string())

    def test_save_state(self):
        game = model.Model()
        game.enter_move('e2e3')
        save_num = game.save_board()
        game.enter_move('e7e6')
        game.load_board(save_num)
        print('current board:')
        print(game.to_string())

    def test_load_from_file(self):
        game = model.Model()
        game.load_board_from_file(DEMO_BOARDS, 0)
        print(game.to_string())

    def test_castling(self):
        game = model.Model()
        game.load_board_from_file(DEMO_BOARDS, 0)
        game.enter_move('d1b1')
        print(game.to_string())

    def test_demo(self):
        game = model.Model()
        fish = ai.StockfishAI()
        while True:
            command = input('>> ')
            parts = command.split(' ')
            statecontroller.ready()
            try:
                if parts[0] == 'm':
                    game.enter_move(parts[1])
                    if not statecontroller.is_error():
                        ai_uci = fish.get_ai_uci(game)
                        game.enter_move(ai_uci)
                    if not statecontroller.is_error():
                        movementqueue.add_move(movetools.build_move(ai_uci))
                    print(movementqueue.to_string())
                elif command == 'save':

                    game.save_board()
                elif parts[0] == 'load':
                    game.load_board(int(parts[1]))
                elif parts[0] == 'fileload':
                    game.load_board_from_file(DEMO_BOARDS, int(parts[1]))
                elif parts[0] == 'pop':
                    print(movementqueue.pop_move())
                else:
                    print('invalid command')
                    pass
            except Exception as e:
                print(e)


if __name__ == '__main__':
    unittest.main()

