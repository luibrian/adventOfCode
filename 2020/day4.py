#2020 Advent of Code Day 4

def part1(data):
    """Count number of valid passports"""
    req_set = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    opt_set = set(['cid'])
    count = 0
    good_data = []
    for passport in data:
        # Build a dictionary for every passport
        pass_dict ={}
        for value in passport:
            field_value = value.split(':')
            pass_dict[field_value[0]] = field_value[1]
        
        check8 = len(passport) == (len(req_set) + len(opt_set))
        check7 = (len(passport) == len(req_set)) and ('cid' not in pass_dict)
        if check8 or check7:
            count += 1
            good_data.append(pass_dict)
    return (count, good_data)


def part2(data_p1):
    """ Takes the passport data (array of dictionary values) and finds the ones that 
    satisfies the tighter measure
    """
    count = 0
    for passport in data_p1:
        check = True
        for field,value in passport.items():
            if not check:
                break

            if field == 'byr':
                check = check and check_byr(value)
            elif field == 'iyr':
                check = check and check_iyr(value)
            elif field == 'eyr':
                check = check and check_eyr(value)
            elif field == 'hgt':
                check = check and check_hgt(value)
            elif field == 'hcl':
                check = check and check_hcl(value)
            elif field == 'ecl':
                check = check and check_ecl(value)
            elif field == 'pid':
                check = check and check_pid(value)
            elif field == 'cid':
                pass
            else:
                check = False
        if check: 
            count += 1
    return count

    
def check_byr(data):
    return (int(data) >= 1920) and (int(data) <= 2002)


def check_iyr(data):
    return (int(data) >= 2010) and (int(data) <= 2020)


def check_eyr(data):
    return (int(data) >=2020) and (int(data) <= 2030)


def check_hgt(data):
    if 'cm' in data:
        num = int(data[:-2])
        return (num >= 150) and (num <= 193)
    if 'in' in data:
        num = int(data[:-2])
        return (num >= 59) and (num <= 76)


def check_hcl(data):
    possible_set = set(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'])
    truth = (data[0] == '#') and (len(data[1:]) == 6)
    
    i = 1
    while truth and i < len(data):
        if data[i] not in possible_set:
            return False
        i += 1
    return truth


def check_ecl(data):
    return (data in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])) and (len(data) == 3)


def check_pid(data):
    return len(str(data)) == 9


def read_input(in_text):
    """
    Reads the input text file and outputs array of arrays
    """
    data = []
    passport = []
    with open(in_text, 'r') as f:
        for line in f.readlines():
            if line == "\n":
                data.append(passport)
                passport = []
            else:
                passport += line.strip().split(' ')
        data.append(passport)
        return data


if __name__ == "__main__":
    data = read_input('day4_in.txt')
    part1_count,good_data_1 = part1(data)
    print("This is part 1: " + str(part1_count))

    part2_out = part2(good_data_1)
    print("This is part 2: " + str(part2_out))
