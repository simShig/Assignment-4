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
            product_id=splittedline[0]
            quantity = int(splittedline[1])  #casting to int
            activator_id=splittedline[2]
            date = splittedline[3]
            # print (product_id + ","+quantity +", "+activator_id+", "+date)
            cmd1= """SELECT id,quantity FROM products WHERE products.id={}""".format(product_id)
            cursor = repo._conn.cursor().execute(cmd1)
            current_q = cursor.fetchone()[1]
            # print ("exsists:" + str(current_q) + " actions:" +str(quantity))   #for debug
            if quantity>0:      #supplier supplied more products
                # print("supply attempt, updating products and activities")
                #update products table (quantity)
                cmd = """
                UPDATE products SET quantity = quantity + {} WHERE id = {}
                """.format(quantity,product_id)
                cursor.execute(cmd)
                repo._conn.commit
                #update activities table
                cmd = "INSERT INTO activities (product_id, quantity, activator_id, date) VALUES ({},{},{},{})".format(product_id,quantity,activator_id,date)
                repo._conn.execute(cmd)
            else:   #attempt to SELL
                if current_q+quantity<0:      #cant sell, not enough quantity
                    # print ("cant SELL, not enough quantity")
                    #DO NOTHING!
                    continue
                else:                          #selling proccess
                    # print ("SELLING YEYYY!!!!") 
                    #update products table (quantity)
                    cmd = """
                    UPDATE products SET quantity = quantity + {} WHERE id = {}
                    """.format(quantity,product_id)
                    cursor.execute(cmd)
                    repo._conn.commit
                    #update activities table
                    cmd = "INSERT INTO activities (product_id, quantity, activator_id, date) VALUES ({},{},{},{})".format(product_id,quantity,activator_id,date)
                    repo._conn.execute(cmd)


if __name__ == '__main__':
    main(sys.argv)