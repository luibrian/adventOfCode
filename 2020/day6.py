#2020 Advent of Code Day 6

from collections import defaultdict

def part1(data):
    """ Return sum of everyone who said yes. Max one question per group
    """
    count = 0
    for group in data:
        seen = set()
        for person in group:
            for answer in person:
                if answer not in seen:
                    seen.add(answer)
                    count += 1
    return count



def part2(data_p1):
    """ Return the sum of questions to which everyone answered yes. 
    """
    count = 0
    for group in data:
        seen = defaultdict(int)
        group_size = 0
        for person in group:
            group_size += 1
            for answer in person:
                seen[answer] += 1
        
        for answer in seen:
            if seen[answer] == group_size:
                count += 1
    return count



def read_input(in_text):
    """
    Reads the input text file and outputs array of arrays
    """
    data = []
    cur_group = []
    with open(in_text, 'r') as f:
        for line in f.readlines():
            if line == '\n': 
                data.append(cur_group)
                cur_group = []
            else:
                cur_group.append(line.strip())
        data.append(cur_group)
    return data


if __name__ == "__main__":
    data = read_input('day6_in.txt')
    part1_out = part1(data)
    print("This is part 1: " + str(part1_out))

    part2_out = part2(data)
    print("This is part 2: " + str(part2_out))
