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
    newl = []
    file = read_file(sys.argv[1])
    
    for line in file.split("\n")[:-1]:
        work = line.split(": ")
        yea = work[1].split("; ")
        new_list = []

        for i in yea:
            x = i.split(", ")
            green = "0"
            blue = "0"
            red = "0"
            for j in range(len(x)):
                if "green" in x[j]:
                    for char in x[j]:
                        if char.isdigit():
                            green += char
                if "red" in x[j]:
                    for char in x[j]:
                        if char.isdigit():
                            red += char
                if "blue" in x[j]:
                    for char in x[j]:
                        if char.isdigit():
                            blue += char
            if int(green) < 14 and int(blue) < 15 and int(red) < 13:
                new_list.append(i)
        
        yeah = "0"
        if '; '.join(new_list) == work[1]:
            for j in range(len(work[0])):
                for char in work[0][j]:
                    if char.isdigit():
                        yeah += char
            newl.append(yeah)

    final = 0
    for g in newl:
        final += int(g)
    print(final)

main()