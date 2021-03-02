from datetime import datetime, timedelta
import sqlite3
from sqlite3 import Error


def create_connection():
    conn = sqlite3.connect('project_data.db')
    return conn


def update_table(conn, value, ID):
    query = f"UPDATE Project_Data SET date_added=\"{value}\" WHERE id=\"{ID}\""
    cursor_obj = conn.cursor()
    cursor_obj.execute(query)
    conn.commit()


def execute_query():
    conn = create_connection()
    cursor_obj = conn.cursor()

    query = "SELECT id, project_name, submitDate from Project_Data WHERE complete_status=\"complete\""
    cursor_obj.execute(query)
    data = cursor_obj.fetchall()
    for date in data:
        # print(date)
        # accept days before
        datetime_obj_database = datetime.strptime(date[2], "%d.%m.%Y")
        display_date = datetime.strftime(datetime_obj_database, "%d %B,%Y")
        project_name = date[1]
        print(f"( {project_name}: {display_date} )", end="\t")
        days_back = int(input("Date-added (%d):"))
        datetime_obj_date_added = datetime_obj_database - timedelta(days=days_back)
        time_taken = datetime_obj_date_added.strftime("%d %B,%Y")
        update_table(conn, time_taken, date[0])
        print(time_taken)


execute_query()
