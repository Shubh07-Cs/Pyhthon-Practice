name=input("Your Name: ")
pin=1234
user_pin=int(input("PIN: "))
balance=2000000000
if pin==user_pin:
    print("Welcome Mr",name)
    print("(a)Check Balance")
    print("(b)Deposit Balance")
    print("(c)Withdraw Balance")
    work=input( )
    if work=="a":
        print("Your balance: ",balance)
        if balance>=5000:
            print("(a)Deposit Balance")
            print("(b)Withdraw Balance")
            new_work=input(" ")
            if new_work=="a":
                Deposit_balance=int(input("Deposit Balance: Rs "))
                print("Savings Account Balance: Rs",Deposit_balance+balance)
                print("Thank You")
            elif new_work=="b":  
                Withdrawl_balance=int(input("Withdrawl Amount: Rs "))  
                if Withdrawl_balance<balance:
                    print("Amount successfully withdrawn")
                    print("Savings Account Balance: Rs",balance-Withdrawl_balance)
                    print("Thank You") 
                else:   
                    print("Not sufficient amount")
                    print("Sorry to hear")
                    print("")
                    print("(ノへ￣、)") 
                    print("")
            else:
                print("Enter valid option")
                print("Thank You")        
        else:
            print("You have low balance")  
            print("(a)Deposit Balance")  
            print("(b)Withdraw Balance")
            new_work=input(" ")
            if new_work=="a":
                Deposit_balance=int(input("Deposit Balance: Rs "))
                print("Savings Account Balance: Rs",Deposit_balance+balance)
                print("Thank You")
            elif new_work=="b":
                Withdrawl_balance=int(input("Withdrawl Amount: Rs "))  
                if Withdrawl_balance<balance:
                    print("Amount successfully withdrawn")
                    print("Savings Account Balance: Rs",balance-Withdrawl_balance) 
                    print("Thank You")
                else:
                    print("Not sufficient amount") 
                    print("Sorry to hear")
                    print("")
                    print("(ノへ￣、)")
                    print("")
            else:
                print("Enter valid option")
                print("Thank You")        
    elif work=="b":
        Deposit_balance=int(input("Deposit Balance: Rs "))
        print("Savings Account Balance: Rs",Deposit_balance+balance)
        print("Thank You")
    elif work=="c":
        Withdrawl_balance=int(input("Withdrawl Amount: Rs "))  
        if Withdrawl_balance<balance:
            print("Amount successfully withdrawn")
            print("Savings Account Balance: Rs",balance-Withdrawl_balance) 
            print("Thank You")
        else:
            print("Not sufficient amount")
            print("Sorry to hear")
            print("")
            print("(ノへ￣、)") 
            print("")      
    else:
        print("Enter valid option")
        print("Thank You")
else:
    print("Enter valid pin")
    print("Thank You")
