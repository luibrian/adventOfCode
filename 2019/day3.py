#2019 Advent of Code Day 3

def part1(data, noun, verb):
    """
    Provide the value left at position 0 after the program halts
    """
    output = intcode(data, noun, verb)
    return output


def read_input(in_text):
    """
    Reads the input text file and outputs array of values.
    Input file contains list of directions, each list is one row
    Outputs an array of arrays- each array is the list of travel points
    """
    data = []
    with open(in_text, 'r') as f:
        for line in f.readlines():
            data.append(line.strip().split(','))
    return data


def calc_vertices(wire_path):
    """
    Given a wire path (R8,U5,L5,D3,etc), calculate all vertices of the path
    """
    for move in 


if __name__ == "__main__":
    data = read_input('day3_in.txt')
    part1_out = part1(data,12,2) 
    print("This is part 1: " + str(part1_out))

#    part2_out = part2(data,19690720)
#    print("This is part 2: " + str(part2_out))
