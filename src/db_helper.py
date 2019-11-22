import mysql.connector
from mysql.connector import Error
from environs import Env
import os

# it helps to connect with database and read the rows of the table


class DbHelper:
    # constructor 1. load the environment varialbles
    # 2. create connection with database
    # 3. attach a cursor with object
    def __init__(self):
        try:
            self.load_env()
            self.connection = mysql.connector.connect(host=os.environ.get('HOST'),
                                                      database=os.environ.get(
                                                          'DB'),
                                                      user=os.environ.get(
                                                          'USER'),
                                                      password=os.environ.get('PASSWORD'))

            if self.connection.is_connected():
                self.cursor = self.connection.cursor()

        except Error as e:
            print("Error while connecting to MySQL", e)

    def get_maximum_salary(self):
        '''
        the logic to find and return maximum salary from employee table
        '''
        self.cursor.execute('select max(salary) from emp_salary;')
        single_data = self.cursor.fetchone()
        return single_data[0]

    def get_minimum_salary(self):
        '''
        the logic to find and return minimum salary from employee table
        '''
        self.cursor.execute('select min(salary) from emp_salary;')
        single_data = self.cursor.fetchone()
        return single_data[0]

    # load the environment variables
    def load_env(self):
        env = Env()
        # Read .env into os.environ
        env.read_env()


if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)
