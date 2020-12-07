#2019 Advent of Code Day 1
from collections import defaultdict

def part1(data,des_out):
    """Find the two entries that sum to 2020, multiply them together
    Essentially 2sum
    """
    expense_dict = defaultdict(int)
    for expense in data:
        remain = des_out - expense
        if remain in expense_dict:
            return remain*expense
        expense_dict[expense] += 1



def part2(data,des_out):
    """Find the three entries that sum to 2020, multiply them together
    Essentially 3sum
    """
    expense_dict = defaultdict(int)
    for i in range(0, len(data)-2):
        for j in range(i+1, len(data)-1):
            remain = des_out - data[i] - data[j]
            if remain in expense_dict:
                print(data[i], data[j], remain)
                return data[i]*data[j]*remain
        expense_dict[data[i]] += 1 


def read_input(in_text):
    """
    Reads the input text file and outputs an array, each line is a data
    """
    data = []
    with open(in_text, 'r') as f:
        for line in f.readlines():
            l = line.strip()
            data.append(int(l))
    return data


if __name__ == "__main__":
    data = read_input('day1_in.txt')
    output1 = part1(data,2020)
    print("This is part 1: " + str(output1))
    
    output2 = part2(data,2020)
    print("This is part 2: " + str(output2))