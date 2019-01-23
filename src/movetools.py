import movement as movement


#get a player move from an input string
def build_move(move_code):
    from_square = move_code[0:2]
    to_square = move_code[2:4]
    new_movements = []
    # 3 digit code, use enum to compare type digit
    from_coords = coordinates(from_square)
    to_coords = coordinates(to_square)
    new_movements.add(movement.Movement( 'up', from_coords[0], from_coords[1]))
    new_movements.add(movement.Movement( 'down', to_coords[0], to_coords[1]))
    new_move = Move(new_movements)
    return new_move

def print_move(p_move):
    # use enum to get type
    # generate phrase eg "pick up at square H8"

def coordinates(square)
    # return a tuple x,y for square number