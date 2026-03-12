'''.Banking System with Transactions 
Simulate real-time transactions between bank accounts. 
Handle errors like overdraft, transaction timeout, incorrect account numbers.'''

accounts = {
    1001: 5000,
    1002: 3000,
    1003: 7000
}

def transfer():
    try:
        sender = int(input("Enter sender account number: "))
        receiver = int(input("Enter receiver account number: "))
        amount = float(input("Enter amount to transfer: "))

        if sender not in accounts or receiver not in accounts:
            raise Exception("Incorrect account number")

        if accounts[sender] < amount:
            raise Exception("Overdraft! Not enough balance")

        print("Processing transaction...")
        time.sleep(2)   

        if amount > 10000:
            raise TimeoutError("Transaction timeout!")


        accounts[sender] -= amount
        accounts[receiver] += amount

        print("Transaction successful!")

    except TimeoutError as t:
        print("Error:", t)

    except Exception as e:
        print("Error:", e)

    finally:
        print("\nCurrent Account Balances:")
        for acc, bal in accounts.items():
            print("Account", acc, ":", bal)

transfer()
