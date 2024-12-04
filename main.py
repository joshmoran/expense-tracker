import math

# Global Variables 
total = 500.00

transactions = [
    [ 22, 'Bills', 'Internet'],
    [ 10, 'Debt', 'Car payment'],
    [ 50, 'Food', 'Groceries'],
    [ 1000, 'Income', 'Job Salary'],
    [ 30, 'Household Expenses', 'Cleaning'],
    [ 25, 'Transportation', 'Bus transport'],
    [ 15, 'Entertainment', 'Game'],
    [ 10, 'Food', 'Eating out']
]

categories = [
    [ 'Income', 10],
    [ 'Debt', 10.00 ],
    [ 'Bills', 225],
    [ 'Household Expenses', 47],
    [ 'Transportation', 234 ],
    [ 'Food', 22 ],
    [ 'Entertainment', 69 ],
    [ 'Miscellaneous', 92 ]
]

def init () :
    print("")
    print("Hello and welcome to your 'expense tracker'")
    print("")
    print("Lets get your finances in order!!!")
    print("")
    menu()

def menu():
    print("1. View expenses")
    print("2. Add a transaction")
    print("3. Quit")
    print("")
    choice = int(input(">>> "))

    if choice == 1:
        view_expenses()
    elif choice == 2:
        menu_expenses()
    elif choice == 3:
        print("Thank you for using your 'expense tracker'!")
        exit()
    else:
        print("Invalid choice. Please try again.")
        menu()

def view_expenses(): 
    global user_name
    global total

    print("")
    # Print available total
    print("> Balance")
    rounded_total = round_number(total)
    print(f"Your account balance is: £{rounded_total}0")
    print("")
    print(f"> By Categories")
    # List categories and their total
    for category in categories:
        rounded_amount = round_number( category[1] )
        print(f"{category[0]}: £{rounded_amount}0")
    
    print("")
    # List transactions
    print("> All Transactions")
    print("")
    print("Category -- Description : Amount")
    for transaction in transactions:
        rounded_amount = round_number( transaction[0] )
        print(f"{transaction[1]} ----- {transaction[2]}: £{rounded_amount}0")
    print("")
    menu()


def menu_expenses():
    print("")
    print("1. Add income")
    print("2. Add expense")
    print("3. Return to main menu")
    print("")
    choice = int(input(">>> "))

    if choice == 1:
        add_income()
    elif choice == 2:
        add_expense()
    elif choice == 3:
        menu()
    else:
        print("Invalid choice. Please try again.")
        menu_expenses()


def add_income():
    global total

    valid_amount = False
    valid_description = False

    amount = 0
    description = ''

    print("")
    print("Let's add some income to your account")
    print("")
    print("We will need two thing from you")
    print("1. The description")
    print("2. The amount")
    print("")
    print("What is the description")
    print("")
    while not valid_description:
        print("Please enter the description: ")
        description = input(">>> ")
        if description!= "":
            valid_description = True
    print("")
    print("Okay the amount")
    while not valid_amount:
        amount = input(">>> ")
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError
            valid_amount = True
        except ValueError:
            print("Invalid input. Amount must be a positive number. Please try again.")
    
    # Change income category by changing the amount 
    categories[0][1] += amount

    # Add transaction to the list
    transactions.append([amount, 'Income', description])

    # Update total
    total += amount

    print("")
    print("Income added successfully")
    print("")
    menu()

def add_expense():
    global total
    global categories
    
    valid_amount = False
    valid_description = False
    valid_category = False
    validated = False

    chosen_category = ''

    print("")

    print("We will need three things from you")
    print("1. The category")
    print("2. The description")
    print("3. The amount")
    
    # Category

    print("")
    print("Choose a category:")
    show_categories()
    category_length = len(categories)

    while not valid_category:
        try:
            print("")
            print("Please pick a number from the categories") 
            category_input = int(input(">>> "))
            if category_input in range(1, category_length - 1):
                valid_category = True
                break
        except ValueError:
            print("Invalid input. Please enter a number from the categories.")
    print("")
    chosen_category = categories[category_input][0]
    print(f"You chose: {chosen_category}")
    print("")

    # Description
    print("What is the description?")
    print("")
    while not valid_description:
        print("Please enter the description: ")
        description = input(">>> ")
        if description!= "":
            valid_description = True
    print("")

    # Amount 
    print("What is the amount?")
    while not valid_amount:
        amount = input(">>> ")
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError
            valid_amount = True
        except ValueError:
            print("Invalid input. Amount must be a positive number. Please try again.")

    while not validated:
        if amount > total:
            print("")
            print("Insufficient funds in your account.")
            print("Returning to the main menu")
            print("")
            menu()
        else:
            validated = True
            # Remove amount from total
            total -= amount
            # Add to transactions
            create_transaction = [ amount, chosen_category, description ]
            transactions.append(create_transaction)
            # Update the categories
            for category in categories:
                if category[0] == chosen_category:
                    category[1] += amount
                    break
            print("")
            print("Successfully added the transaction")
            print("")
            menu()

def round_number( number ):
    return round( float(number), 3 )
    
def show_categories():
    index_value = 1
    for category in categories:
        if category[0] != 'Income':
            print(f"{index_value}. {category[0]}")
            index_value += 1

init()