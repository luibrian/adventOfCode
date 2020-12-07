#2020 Advent of Code Day 2 
import re

def part1(data):
    """Find number of valid passwords according to policy
    """
    count = 0
    for line in data:
        min_count = int(line[0])
        max_count = int(line[1])
        des_letter = line[2]
        password = line[3]
        letter_count = 0
        for letter in password:
            if letter == des_letter:
                letter_count += 1
        if letter_count >= min_count and letter_count <= max_count:
            count +=1
    return count


def part2(data):
    """Find number of valid passwords according to policy
    """
    count = 0
    for line in data:
        pos1 = int(line[0])-1 
        pos2 = int(line[1])-1
        des_letter = line[2]
        password = line[3]
        if pos1 < len(password) and pos2 < len(password):
            if (password[pos1] == des_letter) ^ (password[pos2] == des_letter):
                count += 1
    return count


def read_input(in_text):
    """
    Reads the input text file and outputs an array of arrays.
    Each individual array is 1x4 and contains min count a password must contain the letter, 
    the max count, the desired letter, and the password itself
    """
    data = []
    with open(in_text, 'r') as f:
        for line in f.readlines():
            line_clean = line.strip()
            line_clean = re.split(' |-',line_clean)
            data.append(line_clean)
        for line in data:
            line[2] = line[2].strip(':')
    return data


if __name__ == "__main__":
    data = read_input('day2_in.txt')
    output1 = part1(data)
    print("This is part 1: " + str(output1))
    
    output2 = part2(data)
    print("This is part 2: " + str(output2))