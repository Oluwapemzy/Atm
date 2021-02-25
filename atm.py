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


def deposit(arr):
    for i in range(len(arr)):
        print(arr[i])

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
        print("Your pin? ")
        pininput = input("> ")
        choic = input("> your choice\n")
    
    # Deposit
    elif choic == "3":
        print("your name? ")
        acctodepo = input("name")
        print("How much?")
        depositamount = input("> amount ")

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