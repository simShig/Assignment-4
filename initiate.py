from persistence import *

import sys
import os

def add_branche(splittedline : list):      ##was like this - (splittedline : list[str])
    #TODO: add the branch into the repo
    cmd ="INSERT INTO branches (id, location, number_of_employees) VALUES ({},{},{})".format(splittedline[0],"'"+splittedline[1]+"'",splittedline[2])
    repo.execute_command(cmd)
    # pass

def add_supplier(splittedline : list):
    #TODO: insert the supplier into the repo
    cmd = "INSERT INTO suppliers (id, name, contact_information) VALUES ({},{},{})".format(splittedline[0],"'"+splittedline[1]+"'","'"+splittedline[2]+"'")
    repo.execute_command(cmd)
    # pass

def add_product(splittedline : list):
    #TODO: insert product
    cmd = "INSERT INTO products (id, description, price, quantity) VALUES ({},{},{},{})".format(splittedline[0],"'"+splittedline[1]+"'",splittedline[2],splittedline[3])
    repo.execute_command(cmd)
    # pass

def add_employee(splittedline : list):
    #TODO: insert employee
    cmd = "INSERT INTO employees (id, name, salary, branche) VALUES ({},{},{},{})".format(splittedline[0],"'"+splittedline[1]+"'",splittedline[2],"'"+splittedline[3]+"'")
    repo.execute_command(cmd)
    # pass

adders = {  "B": add_branche,
            "S": add_supplier,
            "P": add_product,
            "E": add_employee}

def main(args : list):
    inputfilename = args[1]
    # delete the database file if it exists
    repo._close()
    # uncomment if needed
    if os.path.isfile("bgumart.db"):
        os.remove("bgumart.db")
    repo.__init__()
    repo.create_tables()
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(",")
            adders.get(splittedline[0])(splittedline[1:])

if __name__ == '__main__':
    main(sys.argv)