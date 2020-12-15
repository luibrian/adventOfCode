#2020 Advent of Code Day 8


def part1(data, goal):
    """ Return value of accumulator before it repeats
    """
    accumulator = 0
    seen = set()
    if acc:
    if jmp:
    if nop:



def part2(data, goal):
    """ 
    """
    return 1


def read_input(in_text):
    """ Reads the input text file
    """
    data = []
    with open(in_text, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            line = line.split(' ')
            
            data.append(line)
    return data


if __name__ == "__main__":
    data = read_input('day8_in.txt')
    
    part1_out = part1(data)
    print("This is part 1: " + str(part1_out))

    part2_out = part2(data, goal)
    print("This is part 2: " + str(part2_out))
