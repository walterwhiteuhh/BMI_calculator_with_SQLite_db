import sqlite3
from sqlite3 import Error
import pandas as pd
import pylab


def fetch_table_data_into_df(TABLE_NAME, conn):
    return pd.read_sql_query("select * from " + TABLE_NAME, conn)

def create_connection(database):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(database)
    except Error as e:
        print(e)

    return conn

def main():
    database = r"C:\Python\BMI_calculator_with_SQLite_db\bmi.sqlte"

    TABLE_NAME = "bmirechner"
    # create a database connection
    conn = create_connection(database)
    with conn:
        print("Database connected:")
        df = fetch_table_data_into_df(TABLE_NAME, conn)
        # reading what you want to do, I presumed you want 
        # to plot per measuremnt
        for measurement in df.name.unique():
            df[df.name == measurement].plot("name", "bmi")
            pylab.savefig(f"{measurement}.png")
            pylab.clf()
            pylab.show()

if __name__ == '__main__':
    main()