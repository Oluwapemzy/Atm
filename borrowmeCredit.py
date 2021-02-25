# def borrowfFunc (code):
#     if code == "*600#":
#         print(f"Welcome dear MTN user, {name} ")
#         print("""
#             How much would like to borrow?
#             1. #50
#             2. #100
#             3. #150
#             4. #200
#             5. #500
#             6. #1000
#         """)
#     amount = input("> ")
#     if amount == "1":
#         print(f'You have successfully borrowed #50.')

#     elif amount == "2":
#         print(f'You have successfully borrowed #100')

#     elif amount == "3":
#         print(f'You have successfully borrowed #150')

#     elif amount == "4":
#         print(f'You have successfully borrowed #200')

#     elif amount == "5":
#         print(f'You have successfully borrowed #500')

#     elif amount == "6":
#         print(f'You have successfully borrowed #1000')

#     else:
#         print("Your Choice was incorrect.")
    
# elif code == "*321#":
#     print(f"Welcome dear GLO user, {name} ")
#     print("""
#         How much would like to borrow?
#         1. #50
#         2. #100
#         3. #150
#         4. #200
#         5. #500
#         6. #1000
#     """)

#     amount = input("> ")
#     if amount == "1":
#         print(f'You have successfully borrowed #50.')

#     elif amount == "2":
#         print(f'You have successfully borrowed #100')

#     elif amount == "3":
#         print(f'You have successfully borrowed #150')

#     elif amount == "4":
#         print(f'You have successfully borrowed #200')

#     elif amount == "5":
#         print(f'You have successfully borrowed #500')

#     elif amount == "6":
#         print(f'You have successfully borrowed #1000')

#     else:
#         print("Your Choice was incorrect.")

# elif code == "*500#":
#     print(f"Welcome dear AIRTEL user, {name} ")
#     print("""
#         How much would like to borrow?
#         1. #50
#         2. #100
#         3. #150
#         4. #200
#         5. #500
#         6. #1000
#     """)

#     amount = input("> ")
#     if amount == "1":
#         print(f'You have successfully borrowed #50.')

#     elif amount == "2":
#         print(f'You have successfully borrowed #100')

#     elif amount == "3":
#         print(f'You have successfully borrowed #150')

#     elif amount == "4":
#         print(f'You have successfully borrowed #200')

#     elif amount == "5":
#         print(f'You have successfully borrowed #500')

#     elif amount == "6":
#         print(f'You have successfully borrowed #1000')

#     else:
#         print("Your Choice was incorrect.")

# elif code == "*200#":
#     print(f"Welcome dear 9Mobile user, {name} ")
#     print("""
#         How much would like to borrow?
#         1. #50
#         2. #100
#         3. #150
#         4. #200
#         5. #500
#         6. #1000
#     """)

#     amount = input("> ")
#     if amount == "1":
#         print(f'You have successfully borrowed #50.')

#     elif amount == "2":
#         print(f'You have successfully borrowed #100')

#     elif amount == "3":
#         print(f'You have successfully borrowed #150')

#     elif amount == "4":
#         print(f'You have successfully borrowed #200')

#     elif amount == "5":
#         print(f'You have successfully borrowed #500')

#     elif amount == "6":
#         print(f'You have successfully borrowed #1000')

#     else:
#         print("Your Choice was incorrect.")
# else:
#     print(f'{name}, the code is invalid')



# print("Your name > ")
# name = input("")
# # print(name)


# print("Enter USSD code ")
# ussd = input("")


# borrowfFunc(ussd)

def howmuch():
    print("""How much would like to borrow?\n1. #50\n2. #100\n3. #150\n4. #200\n5. #500\n6. #1000""")


def amountfunc(response, firstName):
    if response =="1":
        print (f"{firstName}, you have successfully borrowed #50")

    elif response == "2":
        print (f"{firstName}, you have successfully borrowed #100")

    elif response == "3":
        print (f"{firstName}, you have successfully borrowed #150")

    elif response == "4":
        print (f"{firstName}, you have successfully borrowed #200")

    elif response == "5":
        print (f"{firstName}, you have successfully borrowed #500")

    elif response == "6":
        print (f"{firstName}, you have successfully borrowed #1000")

    else:
        print ("invalid input")


def borrowfFunc(ussd,user):
    if ussd == "*321#":
        print(f"welcome dear glo user, {user}.")
        howmuch()
        amount = input("> ")
        amountfunc(amount,name)
        
    elif ussd == "*606#":
        print(f"welcome dear MTN user, {user}.")
        howmuch()
        amount = input("> ")
        amountfunc(amount, name)

    elif ussd == "*500#":
        print(f"welcome dear Airtel user, {user}.")
        howmuch()
        amount = input("> ")
        amountfunc(amount, name)

    elif ussd == "*665#":
        print(f"welcome dear 9Mobile user, {user}.")
        howmuch()
        amount = input("> ")
        amountfunc(amount, name)

    else:
        print("invalid code.")


  
name = input("Your name > ")
code = input("Enter USSD code > ")

borrowfFunc(code, name)
