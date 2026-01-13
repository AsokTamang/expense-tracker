from fastapi import FastAPI
import database
from datetime import date
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Expense(BaseModel):
    expense_date:date
    amount:int
    category:str
    notes:str


@app.get('/expenses')
async def get_expenses():
    expenses =  database.get_all_datas()
    return expenses

#getting data from specific date
@app.get('/expenses/{expense_date}')
async def get_date_expense(expense_date:date):
    expense = database.get_expense_date_data(expense_date)
    return expense


#deleting the data based on specific date
@app.post('/expenses/delete/{expense_date}')
async def delete_date_expense(expense_date:date):
    expense = database.delete_expense_date_data(expense_date)
    return expense

@app.post('/expenses/insert',response_model=Expense)
async def insert_date_expense(data:Expense):
    expense = database.insert_into_database(expense_date=data.expense_date,amount=data.amount,category=data.category,notes=data.notes)
    return expense

@app.put('/expenses/update/{expense_date}',response_model=List[Expense]|Expense)  #here for the updation we are using date in the param too
async def update_date_data(data:Expense, expense_date:date):
    expense = database.update_date_data(expense_date=expense_date,amount=data.amount,category=data.category,notes=data.notes)
    return expense


@app.delete('/expenses/delete/{expense_date}')
async def delete_date_data(expense_date:date):
    try:
        expense = database.delete_expense_date_data(expense_date)
        return 'Successful deletion'
    except Exception as e:
        return 'Error occured',e

