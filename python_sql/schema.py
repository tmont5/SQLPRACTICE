sql_drop_employee_table = "DROP TABLE IF EXISTS employee"
sql_create_employee_table = """ 
    CREATE TABLE IF NOT EXISTS employee (
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL,
        years_of_experience INTEGER NOT NULL,
        access_level INTEGER NOT NULL,
        FOREIGN KEY (access_level) REFERENCES amenaties(id)
    );
"""

sql_drop_member_table = "DROP TABLE IF EXISTS member"
sql_create_member_table = """
    CREATE TABLE IF NOT EXISTS member (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL,
        spouseID INTEGER,
        number_of_children INTEGER NOT NULL,
        access_level INTEGER NOT NULL,
        FOREIGN KEY (access_level) REFERENCES amenaties(id)
    );
"""

sql_drop_amenaties_table = "DROP TABLE IF EXISTS amenaties"
sql_create_amenaties_table = """
    CREATE TABLE IF NOT EXISTS amenaties (
        description VARCHAR(30) NOT NULL
    );
"""

def get_schema():
    schema = f"{sql_create_employee_table}{sql_create_member_table}{sql_create_amenaties_table}"
    return schema