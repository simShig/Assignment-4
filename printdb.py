from persistence import *

def main():
    #TODO: implement

    print_branches()
    print_products()
    print_products()
    print_suppliers()
        
    
    # pass
    
def print_employees ():
    cursor = repo._conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close

def print_suppliers ():
    cursor = repo._conn.cursor()
    cursor.execute("SELECT * FROM suppliers")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close
    
def print_products ():
    cursor = repo._conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close
    
def print_branches ():
    cursor = repo._conn.cursor()
    cursor.execute("SELECT * FROM branches")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close
    
if __name__ == '__main__':
    main()