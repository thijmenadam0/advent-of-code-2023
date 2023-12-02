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
    final = 0
    
    for line in file.split("\n")[:-1]:
        work = line.split(": ")
        yea = work[1].split("; ")
        new_list = []

        greenl = []
        redl = []
        bluel = []
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
            greenl.append(green)
            bluel.append(blue)
            redl.append(red)
        
        greenreal = 0
        bluereal = 0
        redreal = 0
        for item in greenl:
            if int(item) > greenreal:
                greenreal = int(item)
        for item2 in bluel:
            if int(item2) > bluereal:
                bluereal = int(item2)
        for item3 in redl:
            if int(item3) > redreal:
                redreal = int(item3)        
        
        final += redreal * bluereal * greenreal

    print(final)

main()