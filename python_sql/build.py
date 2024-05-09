import os

from db import create_table, create_connection
from schema import *


def select_all_from_amenaties(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM amenaties")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def insert_to_amenaties(conn):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = """
        INSERT INTO menu VALUES
        (1, 'Swimming Pool'),
        (2, 'Gym'),
        (3, 'Spa'),
        (4, 'Golf Park',
        (5, 'Golf Course'),
        (6, 'Horses'),
        (7, 'Simulator');
    """

    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_members(conn):

    sql = """
        INSERT INTO customers VALUES
	    (1, 'Mark', 'Lee', 2, 4, 1),
        (2, 'Jenny', 'Lee', 1, 4, 1),
        (3, 'Shaun', 'White', NULL, 0, 7),
        (4, 'Jim', 'Carter', 5, 3, 5),
        (5, 'Shauna', 'Carter', 4, 3, 5);
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_employees(conn):
    sql = """
         INSERT INTO employee VALUES
	        (1, 'Nicolene', 'Jones', 20),
            (2, 'Anna', 'Smith', 10),
            (3, 'Jessica', 'Brown', 5);
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid


def main():
    database = "./pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    create_table(conn, sql_create_employee_table)
    insert_to_employees(conn)
    create_table(conn, sql_create_member_table)
    insert_to_members(conn)
    create_table(conn, sql_create_amenaties_table)
    insert_to_amenaties(conn)