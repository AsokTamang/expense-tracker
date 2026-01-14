from dotenv import load_dotenv
import os
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from logging_setup import set_logger

load_dotenv()  # configuring the dotenv
from contextlib import contextmanager
#asdas


logger = set_logger(__name__)  #passing the current filename


@contextmanager
def get_connection(commit= False):
    db = mysql.connector.connect(
        host="localhost",
        user=os.getenv("USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        database="expense_manager"
    )

    if db.is_connected():
        print('database connected')
    else:
        print('database not connected')

    db_cursor = db.cursor(
        dictionary=True)  # here cursor is like a sql pointer which helps to run the sql query on databases and with using dictionary=True we

    yield db_cursor,db # yielding the cursor object which can be used in other functions at its current state

    if commit:  #only when the passed commit is true , we commit the staged changes into our database
        db.commit()
    db_cursor.close()
    db.close()


def get_all_datas():
    logger.info(f'Fetched all expenses data from database')
    with get_connection() as (cursor,db):
        cursor.execute("SELECT * FROM expenses;")  # this will gives us the current use and host
        datas = cursor.fetchall()  # fetching all the datas using sql query
        return datas


def get_expense_date_data(expense_date):  # retrieving the expense data based on expense date
    logger.info(f'Fetched all expenses data from database on date {expense_date}')
    with get_connection() as (cursor,db):
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s",
                       [expense_date])  # this will gives us the current use and host
        datas = cursor.fetchall()  # fetching all the datas using sql query
        return datas



def insert_into_database(expense_date,amount,category,notes):
    logger.info(f'Inserted new expense data on database with data {expense_date,amount,category,notes}')
    with get_connection(commit=True) as (cursor,db):
        cursor.execute("INSERT INTO expenses (expense_date,amount,category,notes) VALUES (%s, %s, %s, %s)",[expense_date,amount,category,notes])    #inserting the new data
        rowid = cursor.lastrowid
        cursor.execute("SELECT * FROM expenses WHERE id = %s",[rowid])
        data=cursor.fetchone()
        return data


def delete_expense_date_data(expense_date):  # retrieving the expense data based on expense date
    logger.info(f'Deleted all expenses data from database on date {expense_date}')
    with get_connection(commit=True) as (cursor,db):
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s",
                       [expense_date])  # this will gives us the current use and host



def get_datas_between_date(start_date, end_date):
    logger.info(f'Fetched all expenses data from database between date: {start_date} and {end_date}')
    with get_connection() as (cursor, db):
        cursor.execute('''SELECT category,SUM(amount) AS total FROM expenses
                           WHERE expense_date BETWEEN %s AND %s
                           GROUP BY category;''',[start_date,end_date])  # here db is our sql connecting instance\
        datas = cursor.fetchall()
        return datas

def update_date_data(expense_date,amount,category,notes):
    logger.info(f'Updated all expenses data from database on date {expense_date} with values {amount,category,notes}')
    with get_connection(commit=True) as (cursor, db):
        cursor.execute('''UPDATE expenses
        SET amount = %s, category = %s ,notes = %s WHERE expense_date = %s;''',[amount,category,notes,expense_date])
        cursor.execute('SELECT * FROM expenses WHERE expense_date = %s',[expense_date])
        data=cursor.fetchall()
        return data

def get_month_data(month):
    logger.info(f'fetched all expenses data from database on month {month}')
    with get_connection(commit=True) as (cursor, db):
        cursor.execute('''SELECT category,SUM(amount) AS total FROM expenses
                           WHERE MONTH(expense_date) = %s 
                           GROUP BY category;''',[month])
        data=cursor.fetchall()
        return data



if __name__ == '__main__':
   #delete_expense_date_data('2026-05-01')
   pass


