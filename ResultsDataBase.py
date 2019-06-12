import sqlite3
from sqlite3 import Error

"""
Class for handling the database and saving the results of running programs

"""


class ResultsDataBase:
    """ the folder for the database should be created earlier """
    database = "C:\\sqlite\db\pythonsqlite.db"

    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return None

    def create_table(self, conn):
        """
           If not exits create a table programs_results
           :param conn:
       """
        sql_create_programs_results_table = """ CREATE TABLE IF NOT EXISTS programs_results (
                                            id integer PRIMARY KEY,
                                            program_name text NOT NULL,
                                            result double NOT NULL,
                                            date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP

                                        ); """

        # check a database connection
        if conn is not None:
            # create programs_results table
            try:
                c = conn.cursor()
                c.execute(sql_create_programs_results_table)
            except Error as e:
                print(e)
        else:
            print("Error! cannot create the database connection.")

    def add_program_result(self, result):
        """
            Add a new result into the programs_results table
            :param result:
            :return: project id
        """

        conn = self.create_connection(self.database)

        with conn:
            # if not exits create a table programs_results
            self.create_table(conn)

            sql = ''' INSERT INTO programs_results(program_name, result)
                      VALUES(?,?) '''
            cur = conn.cursor()
            cur.execute(sql, result)
            return cur.lastrowid

    def select_all_results(self):
        """
            Print all results from base
            :return:
        """

        conn = self.create_connection(self.database)

        cur = conn.cursor()
        cur.execute("SELECT * FROM programs_results WHERE 1")

        rows = cur.fetchall()

        for row in rows:
            print(row)

    def main(self):
        # create a database connection
        conn = self.create_connection(self.database)
        with conn:
            # if not exits create a table programs_results
            self.create_table(conn)

            # add new results to base (program_name, result_value)
            result = ('test program', '54.456')
            result_id = self.add_program_result(result)

            print("Get all results from base")
            self.select_all_results()
