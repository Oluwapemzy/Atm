customers = []


# function to register a customer
def register():
    name = input("your name? ")
    age = int(input("your age? "))
    if len(name) >= 3:
        print(f"{name}, you have successfully registered")
        customers.append({name:[age, 0]}) 
    else:
       print("INVALID name.\nName must al least have 3 characters")


# Deposit function
def deposit(arr,name):
    for i in range(len(arr)):
        # print(arr[i].keys())
        
        if name in arr[i].keys():
            print("Valid\nHow much do you want to deposit ? ")
            depositamount = int(input("> amount "))
            customers[i][name][1] += depositamount
            break

        else:
            pass
            # print("name not found")
            

# Function that performs withdraw
def withdraw(wdFrm):
    for j in range(len(customers)):
        print(j)


# Amount user has
def checkBalance():
    print("balance is")

print("Welcome to the Premier Bank")
print("You have to register before using Premier bank Atm")
print("What would you like to do at our bank?\n1. Register\n2. Withdraw\n3. Deposit\n4. Exit")
choic = input("> your choice\n")







while True:
    # register
    if choic == "1":
        register()
        choic = input("> your choice\n")

    # Withdraw
    elif choic == "2":
        accname = input("the account you want to withdraw from: ")
        print("Your pin? ")
        pininput = input("> ")
        withdraw(accname)
        choic = input("> your choice\n")
        
    
    # Deposit
    elif choic == "3":
        print("your name? ")
        acctodepo = input("name\n")

        deposit(customers, acctodepo)
        choic = input("> your choice\n")
    
    # quit
    elif choic == "4":
        print("thank you choosing Premier Bank.")
        break

    
    else:
        break


else:
    print("nno")


print(customers)