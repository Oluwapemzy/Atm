customers = [{'ojo' :[30, 30000, {'pinchosen': "1270"}]}, {'bade' :[33, 20000, {'pinchosen': "1990"}]}, {'setemi' :[23, 15000, {'pinchosen': "1690"}]}]


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

    return    

# Function that performs withdraw
def withdraw(wdFrm):
    for j in range(len(customers)):
        # print(customers[j])
        if wdFrm in customers[j].keys():
            # print(customers[j][wdFrm])
            wdamount = int(input("Amount\n > "))
            print("Your pin? ")
            pininput = input("> ")
            if pininput == customers[j][wdFrm][2]['pinchosen']:
                print("valid")
                customers[j][wdFrm][1] = customers[j][wdFrm][1] - wdamount
            else:
                print("invalid pin")
                pass
            # break
        else:
            # print("invalid name")
            pass
    return


# Amount user has
def checkBalance(detail_to_check):
    # print("balance is")
    for k in range(len(customers)):
        if detail_to_check in customers[k].keys():
            print("Your pin? ")
            pininput = input("> ")
            
           
            if pininput == customers[k][detail_to_check][2]['pinchosen']:
                print("valid")
                print(f"Your balance, {detail_to_check} is #"+ str(customers[k][detail_to_check][1]))
            else:
                print("invalid pin")
                pass
        else:
            pass
    return

print("Welcome to the Premier Bank")
print("You have to register before using Premier bank Atm")
print("What would you like to do at our bank?\n1. Register\n2. Withdraw\n3. Deposit\n4. Check balance\n5. Exit")
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
    
    # Balance check
    elif choic == "4":
        print("Account Name")
        accdetail = input("> ")
        checkBalance(accdetail)
        choic = input("> your choice ")

    # quit
    elif choic == "5":
        print("thank you choosing Premier Bank.")
        break


    else:
        break

else:
    print("nno")

print(customers)
