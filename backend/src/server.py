from fastapi import FastAPI
import database
from datetime import date

app = FastAPI()

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

