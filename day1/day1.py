#
#
#
#

import sys

def read_file(filename):
    """ opens and reads file with name filename and returns a string of text """
    infile = open(filename, "r")
    text = infile.read()
    infile.close()
    return text

def main():
    file = read_file(sys.argv[1])
    
    numb_dict = {"one": 1, "two": 2, "three": 3,
                    "four": 4, "five": 5, "six": 6,
                    "seven": 7, "eight": 8, "nine": 9}
    full = []

    for line in file.split():
        numbers = []

        for item in numb_dict.keys():
            yealist = []
            if item in line:
                yealist.append(item)
        
            for i in yealist:
                line = line.replace(i, i[0] + str(numb_dict[item]) + i[-1])
        print(line)
        for char in line:
            if char.isdigit():
                numbers.append(char)
        yea = numbers[0] + numbers[-1]
        full.append(yea)
    
    final = 0
    for i in full:
        final += int(i)
    
    print(final)

if __name__ == "__main__":
    main()