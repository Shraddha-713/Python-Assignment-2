database = {
    1001 : {
        'name' : 'Shraddha',
        'email' : 'shraddha123@gmail.com',
        'password' : 'shraad123',
        'balance' : 50000
    },
    1002 : {
        'name' : 'John',
        'email' : 'john123@gmail.com',
        'password' : 'john123',
        'balance' : 25000
    },
    1003 : {
        'name' : 'Alex',
        'email' : 'alex123@gmail.com',
        'password' : 'alex123',
        'balance' : 30000
    },
    1004 : {
        'name' : 'Riddhi',
        'email' : 'riddhi123@gmail.com',
        'password' : 'rid123',
        'balance' : 40000
    },
    1005 : {
        'accountNo' : 1005,
        'name' : 'Shaggy',
        'email' : 'shaggy123@gmail.com',
        'password' : 'shaggy123',
        'balance' : 24000
    }
}

#   Select Your Choice
print("What do you want?\n   1- Login \n   2- Signup\n   3- Exit")
choice = input("Enter you choice-")

if choice == '1' or choice == 'Login' :
    accountNo = int(input("Enter Account Number- "))
    password = input("Enter Password- ")
    if accountNo in database.keys() :
        if password == database[accountNo]['password'] :
            print(f"Login Successfully Welcome {database[accountNo]['name']}")
        else :
               print("Incorrect Password")
    else :
        print("Account not exist")

#                           To Deposit, Withdrawl and Balance Check

    print("What do you want?\n  1- Cash Withdraw\n  2- Deposit\n  3- Check Balance")
    ch = input("Enter you choice- ")
    if ch == "1" or ch == "Cash Withdraw" :
        amt = int(input("How much ammount? "))
        amt = database[accountNo]['balance'] - amt
        print("Thanks for banking. Available amount is: ", amt)
    elif ch == "2" or ch == "Deposit" :
        amt = int(input("How much ammount you want to add? "))
        amt = database[accountNo]['balance'] + amt
        print("Thanks for banking. Available amount is: ", amt)
    elif ch == "3" or ch == "Check Balance" :
        print(database[accountNo]['balance'])

elif choice == '2' or choice == 'Signup' :
    print("Signup")
elif choice == '3' or choice == 'Exit' :
    print("Exit Successfully")
else :
    print("Enter valid choice")


    



#print("Balance= ", database[accountNo]['balance'])
