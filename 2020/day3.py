#2020 Advent of Code Day 3

def part1(data):
    """
    Provide the value left at position 0 after the program halts
    """
    movement = [3,1]
    tree_count = travel_slope(data,movement)
    return tree_count
    

def part2(data):
    movements = [[1,1], [3,1], [5,1], [7,1], [1,2]]
    product = 1
    for movement in movements:
        tree_count = travel_slope(data,movement)
        product *= tree_count
    return product


def read_input(in_text):
    """
    Reads the input text file and outputs array of arrays
    """
    data = []
    with open(in_text, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            data.append(line) 
        return data


def travel_slope(data, movement):
    tree_count = 0
    cur_loc = 0
    for line in data[::movement[1]]:
        if line[cur_loc] == '#':
            tree_count += 1
        cur_loc = (cur_loc + movement[0]) % len(line)
    return tree_count


if __name__ == "__main__":
    data = read_input('day3_in.txt')
    part1_out = part1(data)
    print("This is part 1: " + str(part1_out))

    part2_out = part2(data)
    print("This is part 2: " + str(part2_out))
