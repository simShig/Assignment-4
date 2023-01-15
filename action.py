from persistence import *

import sys

# You may assume that the configuration file exists and that the syntax and the data are valid
# but you need to check that the quantity of the sold product is enough.
# If for any reason an action may not be fulfilled do NOTHING!!


# activity - productID,quantity,activator id,date

def main(args : list):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            #TODO: apply the action (and insert to the table) if possible

if __name__ == '__main__':
    main(sys.argv)