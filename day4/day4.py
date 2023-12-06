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
    file = file.split("\n")
    total = 0

    for line in file:
        line = line.split(":")
        
        cards = line[1].split("|")

        ticket = set(cards[0].split())
        winning = set(cards[1].split())

        actualwin = ticket.intersection(winning)

        if actualwin != set():
            amount = len(actualwin)
            if amount == 1:
                total += 1
            else:
                total += 1 * (2 ** (amount - 1))
    
    print(total)
            

main()