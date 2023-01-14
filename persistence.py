import sqlite3
import atexit
from dbtools import Dao
 
# Data Transfer Objects:
class Employee(object):
    # TODO: implement
    def __init__(self, id, name, salary, branche):
        self.id = id
        self.name = name
        self.salary = salary
        self.branche = branche
    # pass
 
class Supplier(object):
    #TODO: implement
    def __init__(self, id, name,contact_information):
        self.id = id
        self.name = name
        self.contact_information = contact_information
    # pass

class Product(object):
    #TODO: implement
    def __init__(self, id, description, price, quantity):
        self.id = id
        self.description = description
        self.price = price
        self.quantity = quantity
    # pass

class Branche(object):
    #TODO: implement
    def __init__(self, id, location, number_of_employees, branche):
        self.id = id
        self.location = location
        self.number_of_employees = number_of_employees
        self.branche = branche
    # pass

class Activitie(object):
    #TODO: implement
    def __init__(self, product_id, quantity, activator_id, date):
        self.product_id = product_id
        self.quantity = quantity
        self.activator_id = activator_id
        self.date = date
    # pass
 
# Data Access Objects (DAOs) were not written here, think weather needed


#Repository
class Repository(object):
    def __init__(self):
        self._conn = sqlite3.connect('bgumart.db')
        self._conn.text_factory = bytes
        # tTODO: complete
        
    def _close(self):
        self._conn.commit()
        self._conn.close()
 
    def create_tables(self):
        self._conn.executescript("""
            CREATE TABLE employees (
                id              INT         PRIMARY KEY,
                name            TEXT        NOT NULL,
                salary          REAL        NOT NULL,
                branche    INT REFERENCES branches(id)
            );
    
            CREATE TABLE suppliers (
                id                   INTEGER    PRIMARY KEY,
                name                 TEXT       NOT NULL,
                contact_information  TEXT
            );

            CREATE TABLE products (
                id          INTEGER PRIMARY KEY,
                description TEXT    NOT NULL,
                price       REAL NOT NULL,
                quantity    INTEGER NOT NULL
            );

            CREATE TABLE branches (
                id                  INTEGER     PRIMARY KEY,
                location            TEXT        NOT NULL,
                number_of_employees INTEGER
            );
    
            CREATE TABLE activities (
                product_id      INTEGER REFERENCES products(id),
                quantity        INTEGER NOT NULL,
                activator_id    INTEGER NOT NULL,
                date            TEXT    NOT NULL
            );
        """)

    def execute_command(self, script: str) -> list:
        return self._conn.cursor().execute(script).fetchall()
 
# singleton
repo = Repository()
atexit.register(repo._close)




#Generic ORM and DAO:
import inspect
 
def orm(cursor, dto_type):
 
    #the following line retrieve the argument names of the constructor
    args = inspect.getargspec(dto_type.__init__).args
    
    #the first argument of the constructor will be 'self', it does not correspond 
    #to any database field, so we can ignore it.
    args = args[1:]  
 
    #gets the names of the columns returned in the cursor
    col_names = [column[0] for column in cursor.description]
    
    #map them into the position of the corresponding constructor argument
    col_mapping = [col_names.index(arg) for arg in args]
    return [row_map(row, col_mapping, dto_type) for row in cursor.fetchall()]
 
 
def row_map(row, col_mapping, dto_type):
    ctor_args = [row[idx] for idx in col_mapping]
    return dto_type(*ctor_args)
 
 
#we can use our method above in order to start writing a generic Dao
#note that this class is not complete and we will add methods to it next
class Dao(object):
    def __init__(self, dto_type, conn):
        self._conn = conn
        self._dto_type = dto_type
 
        #dto_type is a class, its __name__ field contains a string representing the name of the class.
        self._table_name = dto_type.__name__.lower() + 's'
 
    def insert(self, dto_instance):
        ins_dict = vars(dto_instance)
 
        column_names = ','.join(ins_dict.keys())
        params = ins_dict.values()
        qmarks = ','.join(['?'] * len(ins_dict))
 
        stmt = 'INSERT INTO {} ({}) VALUES ({})'\
               .format(self._table_name, column_names, qmarks)
 
        self._conn.execute(stmt, params)
 
    def find_all(self):
        c = self._conn.cursor()
        c.execute('SELECT * FROM {}'.format(self._table_name))
        return orm(c, self._dto_type)
    
    
    def find(self, **keyvals):
        column_names = keyvals.keys()
        params = keyvals.values()
 
        stmt = 'SELECT * FROM {} WHERE {}' \
               .format(self._table_name, ' AND '.join([col + '=?' for col in column_names]))
 
        c = self._conn.cursor()
        c.execute(stmt, params)
        return orm(c, self._dto_type)