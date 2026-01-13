from backend.src import app


#test case done for get_expense_date_data module
def test_get_expense_date_data():
    expenses = app.get_expense_date_data("2024-09-01")
    assert len(expenses) == 5
    assert expenses[0]['id'] == 31

def test_get_all_datas():
    expenses = app.get_all_datas()
    assert expenses[0]['id'] == 3

def test_insert_into_database():
    new_expense = app.insert_into_database('2026-02-11',75,'Clothes','Shopping')
    assert new_expense['notes'] == 'Shopping'


def test_get_datas():
    expenses = app.get_datas('2026-01-13','2026-02-11')
    assert len(expenses) == 2