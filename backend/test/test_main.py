from src.app import Bank

def test_bankapp():
    account=Bank("Asok",100000)   #here we are creating one object of Bank class
    assert account.name == "Asok"  #asserting means making sure
    assert account.balance == 100000
