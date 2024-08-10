from datetime import datetime

print("======================================================================")

customernames=input("Enter your name=")
customercity=input("Enter your city=")
customerbalance=0
deposition=0
withdrawal=0
balance=0
counter_1=1
counter_2=2
counter_3=3
i=0
while True:
    print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
    print("-------------------WELCOME TO GRAMIN BANK-------------------------")
    print("===================================================================")
    print("1. Open a new account")
    print("2. Withdrawal money")
    print("3. Deposit money")
    print("4. Apply for ATM")
    print("5. Apply for personal loan")
    print("6. Exit/Quit")
    choicenumber=input("select your chiocenumber from the above list=")
    if choicenumber=="1":
        print("choice number 1 is selected by the customer")
        noc=int(input("number of customers="))
        i=i+noc
        if i>7:
            i=i-noc
        else:
            while counter_1 <=i:
                name=input("Enter the name to open account=")
                pin=int(input("set a pin to the new account="))
                balance=0
                deposition=int(input("Enter the deposition="))
                balance=balance+deposition
                debit_amount=int(input("Enter the amount that u want to debit="))
                print("amount after debits",balance-debit_amount)
                counter_1=1+1
                counter_2=2+1
                counter_3=3+1
                print("/RS")
                print("<<<your name is added in our bank system>>>")
                print("<<<your pin is added in our bank system>>>")
                print("<<<your complete statement will be displayed in bank system>>>")
                print("/n")
                print("-------------New account created successfully!---------------")
                print("your name displays on the customers list now:")
                print(customernames)
                print(customercity)
                print(pin)
                print(deposition)
                print(debit_amount)
                print("Note! Rate your experience with our bank")
                experince=int(input("Enter the numbers for 5 star exerince="))
                stars=input('''1 for average,
                               2 for ok ok,
                               3 for good,
                               4 for very, 
                               5 for excellent=''')
                print(stars)
                "/n"
                print("--------------------------------------------------------------------")
                mainmenu=input("please press M key to go back to main menu to perform another function=")
    elif choicenumber=="2":
        print("choice number 2 is selected by the customer")
        name=input("please input your name=")
        pin=input("please input your pin=")
        Amount=10000
        debit_amount=int(input("Enter the amount that u want to debit="))
        print("amount after debit",Amount-debit_amount)
        print(name)
        print(pin)
        print(Amount)
        print(debit_amount)
        print(Amount-debit_amount)
        print("-------------------------WITHDRAW SUCCESSFULLY----------------------------")
        mainmenu=input("please press M key to go back to main menu to perform another function=")
    elif choicenumber=="3":
        print("choice number 3 is selected by the customer")
        name_1=input("please input your name:")
        pin_2=int(input("please input pin"))
        Amount_3=10000
        deposit_amount_4=int(input("Enter the amount that u want to deposit"))
        print("amount after deposit",Amount_3+deposit_amount_4)
        print(name_1)
        print(pin_2)
        print(Amount_3)
        print(deposit_amount_4)
        print(Amount_3+deposit_amount_4)
        print("========================DEPOSITED SUCCESSFULLY==============================")
        mainmenu=input("please press M key to go back to main menu to perform another function=")
    elif choicenumber=="4":
        print("coice number 4 is selected by the customer")
        name=input("Input your name=")
        pin=int(input("Input your pin="))
        print("<<<To apply ATM card minimum balance is required>>>")
        ATM=int(input("please enter 4 to apply atm card="))
        pin=int(input("please set pin for ATM card="))
        print("<<<<<<ATM succesffully generated card will send via post>>>>>>")
        print("==========================SUCCESSFULLY ATM CARD GENERATED=============================")
        mainmenu=input("please press M key to go back to main menu to perform another function=")
    elif choicenumber=="5":
        print("choicenumber 5 is selected by the customer")
        name=input("Input your name=")
        pin=int(input("Input pin="))
        print("<<<<To Apply the personal please enter 5>>>>")
        print("Sorry its not possible to apply pesonal loan in online in our Gramin bank")
        print("BETTER LUCK NEXT TIME")
        mainmenu=input("please press M to go back to main menu to perform another function=")
    elif choicenumber=="6":
        print("choicenumber 6 is selected by the customer")
        print("THANK YOU FOR YOUR EXPERIENCE IN OUR BANK!!")
        print("VISIT AGAIN")
        print("BETTER LUCK FOR YOUR FUTURE")
    else:
        print("Invalid option selected by the customer")
        print("please try again!!!!")
        mainmenu=input("please press M to go back to main menu=")





















                
                


