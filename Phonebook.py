import sys
def initial_phonebook():
    rows, cols = int(input("Please enter initial number of contacts ")), 5
    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("\nEnter contact id details in the following order (ONLY)"% (i + 1))
        print("NOTE: *indicates mandatory fields")
        print(".......................................................")
        temp = []
        for j in range(cols):
            if j==0:
                temp.append(str(input("Enter name*: ")))
                if temp[j] == '' or if temp[j] == ' ':
                    sys.exit(
                        "Name is a mandatory field. Process exiting due to blank field..."
                    )
            if j==1:
                temp.append(str(input("Enter number*: ")))
            if j == 2:
                temp.append(str(input("Enter email address*: ")))
                if temp[j] == '' or temp[j] == ' ' :
                    temp[j] = None
            if j == 3:
                temp.append(str(input("Enter date of birth (dd/mm/yy):")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
            if j == 4:
                temp.append(str(input("Enter category(Family/friends/work/others)")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
        phone_book.append(temp)
    print(phone_book)
    return phone_book
def menu():
    print("**********************************************")
    print("\t\t\tSMARTPHONE DIRECTORY", flush=False)
    print("**********************************************")
    print("\tYou can now preform the following operations on this phonebook\n")
    print("1. add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit phone book")
    return choice
def add_contact(pb):
    dip = []
    for i in range(
    


        