#2020 Advent of Code Day 7

import re
from collections import defaultdict

def part1(data, goal):
    """ Return sum of everyone who said yes. Max one question per group"""
    count = 0
    for container in data:
        seen = set()
        truth = bag_check(container, goal, data, seen)
        if truth:
            count += 1
    return count -1  # Minus 1 is to deal with the entry of goal in the dict


def part2(data, goal):
    """ Return the sum of questions to which everyone answered yes. """
    return count_bags(goal, data)


def read_input(in_text):
    """ Reads the input text file and outputs dict of bags and dict of their possible contents
    """
    data = {}
    with open(in_text, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            line =line.strip('.')
            line = re.split(' contain |, ', line)
            
            # Make a dictionary, in which the key is the container and value is the contents of container
            contents = {}
            for bag in line[1:]:
                if 'bags' in bag:
                    bag = bag[:-1]
                if not bag == 'no other bag':
                    number = bag[0:1]
                    bag_type = bag[2:] + 's'
                    contents[bag_type] = number
                else: 
                    contents[bag + 's'] = 0
            data[line[0]] = contents
    return data


def bag_check(bag, goal, data, seen):
    """ Check if bag contains the desired goal, defined by data dict"""
    if bag == goal:
        return True
    if bag in seen or bag == 'no other bags':
        return False

    seen.add(bag)
    truth = False
    for content in data[bag]:
        if content not in seen:
            truth = truth or bag_check(content, goal, data, seen)
            if truth:
                return truth


def count_bags(bag, data):
    """Count the number of bags within bag
    """
    if data[bag] == {'no other bags':0}:
        return 0

    count = 0
    for content in data[bag]:
        print(content, data[bag][content])
        count += int(data[bag][content]) + int(data[bag][content]) * count_bags(content, data)
    return count


if __name__ == "__main__":
    data = read_input('day7_in.txt')
    goal = 'shiny gold bags'

    part1_out = part1(data, goal)
    print("This is part 1: " + str(part1_out))

    part2_out = part2(data, goal)
    print("This is part 2: " + str(part2_out))
