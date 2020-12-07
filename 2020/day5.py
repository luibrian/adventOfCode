#2020 Advent of Code Day 5

def part1(data):
    """
    Find your seat- binary search tree
    """
    unseen = make_dict()

    highest = 0
    for board_pass in data:
        assert len(board_pass) == 10, "Bad boarding pass " + board_pass
        
        if unseen[board_pass] > highest:
            highest = unseen[board_pass]
    return highest    



def part2(data_p1):
    """ Takes the passport data (array of dictionary values) and finds the ones that 
    satisfies the tighter measure
    """
    unseen = make_dict()
    for board_pass in data:
        unseen.pop(board_pass)

    curKeys = list(unseen.keys())
    for d in curKeys:
        if d[:2] == 'FF' or d[:2] == 'BB':
            unseen.pop(d)
    return unseen


def read_input(in_text):
    """
    Reads the input text file and outputs array of arrays
    """
    data = []
    with open(in_text, 'r') as f:
        for line in f.readlines():
            data.append(line.strip())
        return data


def make_dict():
    passport = 'FFFFFFFLLL'
    unseen = {passport:0}
    max_id = 8*127+7

    for id in range(1, max_id+1):
        for j in range(0,len(passport)):
            if (id % (2**j)) == 0:
                passport = update_passport(passport,len(passport)-j-1)
        unseen[passport] = id
    return unseen
    

def update_passport(passport,loc):
    """Update passport for make_dict
    """
    new_char = swap(passport[loc])
    p_list = list(passport)
    p_list[loc] = new_char
    new_pass = ''
    return new_pass.join(p_list)


def swap(data):
    """ Swap F/B or L/R
    """
    assert data in set(['F','B','R','L']), 'Not the right character'

    if data == 'F':
        return 'B'
    elif data == 'B':
        return 'F'
    elif data == 'L':
        return 'R'
    elif data == 'R':
        return 'L'
    


def calc_seat_id(board_pass):
    """ Calculate the seat_id (8*row + column) based on board_pass (eg. FBFBBFFRLR)
    """
    pass_row = seat[:7]
    pass_col = seat[7:]


if __name__ == "__main__":
    data = read_input('day5_in.txt')
    part1_out = part1(data)
    print("This is part 1: " + str(part1_out))

    part2_out = part2(data)
    print("This is part 2: " + str(part2_out))
