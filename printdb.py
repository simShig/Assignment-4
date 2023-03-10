from persistence import *

def main():
    
    #TODO: implement

    print_activities()
    print_branches()
    print_employees()
    print_products()
    print_suppliers()
    print_employees_report()
    print_activity_report()
   
    # pass
   
def print_employees ():
    print("Employees")
    cursor = repo._conn.cursor()
    cursor.execute("SELECT * FROM employees ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close

def print_suppliers ():
    print("Suppliers")
    cursor = repo._conn.cursor()
    cursor.execute("SELECT * FROM suppliers ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close
   
def print_products ():
    print("Products")
    cursor = repo._conn.cursor()
    cursor.execute("SELECT * FROM products ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close
   
def print_branches ():
    print("Branches")
    cursor = repo._conn.cursor()
    cursor.execute("SELECT * FROM branches ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close
   
def print_activities ():
    print("Activities")
    cursor = repo._conn.cursor()
    cursor.execute("SELECT * FROM activities ORDER BY date ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close
   
    # Employees report:  Name(asc),salary,workingLocation,total sales income
def print_employees_report ():
    print()
    print("Employees report")
    cursor = repo._conn.cursor()
    cmd = """SELECT employees.name, employees.salary, branches.location, IFNULL(SUM(products.price*-activities.quantity),0) as total_sales_income
    FROM employees LEFT JOIN activities ON employees.id=activities.activator_id
    LEFT JOIN products ON activities.product_id=products.id
    LEFT JOIN branches ON employees.branche = branches.id
    GROUP BY employees.id ORDER BY name ASC
    """
    cursor.execute(cmd)

    # cursor.execute("UPDATE this SET total_sales_income=0 WHERE total_sales_income ISNULL ")
    rows = cursor.fetchall()
    for row in rows:
        # print(row[0] +" "+str(row[1])+" "+row[2])
        print(*row)

    cursor.close
    
    # Activity report: date,item description, quantity, name of seller, name of supplier
    # if SALE -> supplier=NONE, if supplying ->seller=NONE
    # print by date descending
             
   
def print_activity_report ():
    print()
    print("Activities report")
    cursor = repo._conn.cursor()
    cmd = """
    SELECT a.date,p.description,a.quantity,e.name,s.name
    FROM activities a
    JOIN products p ON a.product_id = p.id
    LEFT JOIN suppliers s ON s.id=a.activator_id
    LEFT JOIN employees e ON e.id = a.activator_id
    ORDER BY a.date
    """
    cursor.execute(cmd)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close  
   
   
if __name__ == '__main__':
    main()