#2019 Advent of Code Day 4
"""
You arrive at the Venus fuel depot only to discover it's protected by a password. 
The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same 
(like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?


--- Part Two ---
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?

"""

from collections import defaultdict

def part1(min_range, max_range):
    """
    Finds the number of different passwords within range that meets the criteria in problem
    """
    pass_good = 0
    for num in range(min_range, max_range+1):
        num_str = str(num)
        if len(num_str) == 6:
            if_double = False
            if_increase = True
            prev_digit_str = num_str[0]
            for digit_str in num_str[1:]:
                if_double = if_double or (prev_digit_str == digit_str)
                if_increase = if_increase and (int(digit_str) >= int(prev_digit_str))
                prev_digit_str = digit_str

            if if_double and if_increase:
                pass_good += 1

    return pass_good


def part2(min_range, max_range):
    """
    Finds the number of different passwords within range that 
    meets the criteria in problem
    Numbers that are still okay: 111122, 112233, 112344, 1123456
    Numbers that are not okay anymore: 111234, 111222, 331124
    """
    pass_good = 0
    for num in range(min_range, max_range+1):
        num_str = str(num)
        if len(num_str) == 6:
            if_double = False
            if_increase = True
            doubles_dict = defaultdict(int) # Tracks the count of repeats
            prev_digit_str = num_str[0]
            for digit_str in num_str[1:]:   # Goind through digits of the number
                if_increase = if_increase and (int(digit_str) >= int(prev_digit_str))

                # Keeping track of repeats 
                if prev_digit_str == digit_str:
                    doubles_dict[digit_str] += 1
                    if_double = True

                prev_digit_str = digit_str

            if if_double and if_increase:
                if len(doubles_dict) == 1:
                    if doubles_dict[list(doubles_dict)[0]] > 1:
                        continue
                if len(doubles_dict) == 2:
                    if doubles_dict[list(doubles_dict)[0]] == 2 and doubles_dict[list(doubles_dict)[1]] == 2:
                        continue
                pass_good += 1

    return pass_good


if __name__ == "__main__":
    part1_out = part1(156218,652527)
    print("This is part 1: " + str(part1_out))

    #part2_out = part2(123440,123550)
    part2_out = part2(156218,652527)
    print("This is part 2: " + str(part2_out))
        #1148
