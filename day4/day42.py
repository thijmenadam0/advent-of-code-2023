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
    file = file.split("\n")[::-1]
    total = []

    for i in range(len(file)):
        line = file[i].split(":")
        cards = line[1].split("|")
        amount = len(set(cards[0].split()) & set(cards[1].split()))
        total = [1 + sum(total[:amount])] + total
    
    print(sum(total))
            

main()