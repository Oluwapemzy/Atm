customers = []


# function to register a customer
def register():
    name = input("your name? ")
    age = int(input("your age? "))
    choosepin = input("please choose a 4-digit pin ")
    
    if len(name) >= 3:
        print(f"{name}, you have successfully registered")
        customers.append({name:[age, 0, {'pinchosen':choosepin}]}) 
    else:
       print("INVALID name.\nName must al least have 3 characters")


# Deposit function
def deposit(arr,name):
    for i in range(len(arr)):
        # print(arr[i].keys())
        
        if name in arr[i].keys():
            print("Valid\nHow much do you want to deposit ? ")
            depositamount = int(input("> "))
            customers[i][name][1] += depositamount
            break

        else:
            pass
            # print("name not found")
            

# Function that performs withdraw
def withdraw(wdFrm):
    for j in range(len(customers)):
        # print(customers[j])
        if wdFrm in customers[j].keys():
            print(customers[j][wdFrm])
            wdamount = int(input("Amount\n > "))
            print("Your pin? ")
            pininput = input("> ")
            if pininput == customers[j][wdFrm][2]['pinchosen']:
                print("valid")
                customers[j][wdFrm][1] = customers[j][name][1] - wdamount
            else:
                print("invalid pin")
                pass
            # break
        else:
            # print("invalid name")
            pass

# Amount user has
def checkBalance():
    print("balance is")




print("Welcome to the Premier Bank")
print("You have to register before using Premier bank Atm")
print("What would you like to do at our bank?\n1. Register\n2. Withdraw\n3. Deposit\n4. Exit")
choic = input("> your choice ")



while True:

    # register
    if choic == "1":
        register()
        choic = input("> your choice ")

    # Withdraw
    elif choic == "2":

        accname = input("the account you want to withdraw from: ")
        
        withdraw(accname)
        choic = input("> your choice ")
        
    
    # Deposit
    elif choic == "3":
        print("your name? ")
        acctodepo = input("> ")

        deposit(customers, acctodepo)
        choic = input("> your choice ")
    
    # quit
    elif choic == "4":
        print("thank you choosing Premier Bank.")
        break
    
    else:
        break

else:
    print("nno")

print(customers)
