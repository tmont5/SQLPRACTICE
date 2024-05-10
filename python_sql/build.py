import os

from db import create_table, create_connection, delete_table
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
        INSERT INTO amenaties VALUES
        ('Swimming Pool'),
        ('Gym'),
        ('Spa'),
        ('Golf Park'),
        ('Golf Course'),
        ('Horses'),
        ('Simulator');
    """

    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_members(conn):

    sql = """
        INSERT INTO member VALUES
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
	        ('Nicolene', 'Jones', 20, 7),
            ('Anna', 'Smith', 10, 7),
            ('Jessica', 'Brown', 5, 7);
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid




def build_main():
    database = "./pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    delete_table(conn, sql_drop_employee_table)
    create_table(conn, sql_create_employee_table)
    insert_to_employees(conn)
    delete_table(conn, sql_drop_member_table)
    create_table(conn, sql_create_member_table)
    insert_to_members(conn)
    delete_table(conn, sql_drop_amenaties_table)
    create_table(conn, sql_create_amenaties_table)
    insert_to_amenaties(conn)