#2019 Advent of Code Day 5

def part1(data, noun, verb):
    """
    Provide the value left at position 0 after the program halts
    """
    output = intcode(data, noun, verb)
    return output


def part2(data,desOut):
    for noun in range(0,100):
        for verb in range(0,100):
            output = intcode(data, noun, verb)
            if output == desOut:
                return 100*noun + verb


def read_input(in_text):
    """
    Reads the input text file and outputs array of values
    """
    with open(in_text, 'r') as f:
        for line in f.readlines():
            data = line.strip().split(',')
            for index,num_str in enumerate(data):
                data[index] = int(num_str)
        return data


def intcode(data, noun, verb):
    data_copy = data.copy()
    data_copy[1] = noun         # Given in problem description
    data_copy[2] = verb         # Given in problem description
    
    i = 0
    while data_copy[i] != 99 and i < len(data_copy):
        index1 = data_copy[i+1]
        index2 = data_copy[i+2]
        index3 = data_copy[i+3]
        if data_copy[i] == 1:
            data_copy[index3] = data_copy[index1] + data_copy[index2]
        if data_copy[i] == 2:
            data_copy[index3] = data_copy[index1] * data_copy[index2]
        i += 4
    return data_copy[0]


if __name__ == "__main__":
    data = read_input('day2_in.txt')
    part1_out = part1(data,12,2) 
    print("This is part 1: " + str(part1_out))

    part2_out = part2(data,19690720)
    print("This is part 2: " + str(part2_out))
