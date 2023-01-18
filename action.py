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
            print(cursor)
            current_q = cursor.fetchone()[1]
            print (current_q - quantity)
            if quantity>0:      #supplier supplied more products
                #update products table (quantity)
                cmd = """
                UPDATE products SET quantity = quantity + {} WHERE id = {}
                """.format(quantity,product_id)
                cursor.execute(cmd)
                repo._conn.commit
                #update activities table
                cmd = "INSERT INTO activities (product_id, quantity, activator_id, date) VALUES ({},{},{},{})".format(product_id,quantity,activator_id,date)
                repo._conn.execute(cmd)
            else:
                if current_q<quantity:
                    print ("smaller")
                    #DO NOTHING!
                else:
                    print ("bigger")
                    
                    
                    #update products quantity

                    
                    #add to activities table



    #     action = action.strip() # remove leading and trailing whitespace
    #     action_parts = action.split(' ') # split the action into parts
    #     if action_parts[0] == 'buy':
    #         # Handle buying products
    #         product_id = int(action_parts[1])
    #         quantity = int(action_parts[2])
    #         c.execute("UPDATE products SET quantity = quantity + ? WHERE id = ?", (quantity, product_id))
    #     elif action_parts[0] == 'sell':
    #         # Handle selling products
    #         product_id = int(action_parts[1])
    #         quantity = int(action_parts[2])
    #         c.execute("SELECT quantity FROM products WHERE id = ?", (product_id,))
    #         current_quantity = c.fetchone()[0]
    #         if current_quantity >= quantity:
    #             c.execute("UPDATE products SET quantity = quantity - ? WHERE id = ?", (quantity, product_id))
    #             c.execute("INSERT INTO activities (product_id, quantity) VALUES (?, ?)", (product_id, -quantity))
    #     else:
    #         # Handle invalid actions
    #         print(f'Invalid action: {action}')
    # conn.commit()
    # conn.close()

            # print (cmd)
            # print(repo.execute_command(cmd))
            
            
            

            # cmd = "INSERT INTO employees (id, name, salary, branche) VALUES ({},{},{},{})".format(splittedline[0],"'"+splittedline[1]+"'","'"+splittedline[2]+"'","'"+splittedline[3]+"'")



if __name__ == '__main__':
    main(sys.argv)