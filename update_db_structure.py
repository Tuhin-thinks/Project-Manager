import sqlite3
from sqlite3 import Error

DATA_BASE = "project_data.db"
COLUMNS = ['id', 'project_name', 'definition', 'price', 'submitDate', 'complete_status', 'date_added', 'payment_cleared']
def create_connection():
    conn = sqlite3.connect(DATA_BASE)
    return conn

def update_cols(query):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

def fill_data_for_new_col(column_name):
    conn = create_connection()
    query = "select * from \"Project_Data\""
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        complete_status = row[COLUMNS.index('complete_status')]
        if complete_status == 'complete':
            query = f"update \"Project_Data\" set \"{COLUMNS[-1]}\" = \"cleared\" where \"id\"=\"{row[COLUMNS.index('id')]}\""
        else:
            query = f"update \"Project_Data\" set \"{COLUMNS[-1]}\" = \"not cleared\" where \"id\"=\"{row[COLUMNS.index('id')]}\""
        update_cols(query=query)
    

fill_data_for_new_col("payment_cleared")