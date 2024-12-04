
# Expense Tracker App
## This is an assignment for 'JustIT' within their technical training for Python
- Please see 'Project Brief.pdf' for full project details that this script must meet 
- Overview
- [x] 1. Welcome message 
- [x] 2. Log Expense
  - [x] Expense Amount 
  - [x] Expense Category
  - [x] Description
- [x] 3. Store Data
- [x] 4. Display Summary
  - [X] Total Expense Spent
  - [X] Amount for each category
  - [X] Show a list of expenses with details
- [x] 5. Data validation 
- [x] 6. Thank you message

## Index
1. Overview and Error Handling
2. Adding new quizzes

# Overview and Error Handling 

## Initial Load
- Greets user and welcomes them to the expense tracker

## Menu
### Overview 
- Gives three options
    1. View expenses
    2. Add a transaction
       - Three main options
           1. Add Income
           2. Add Expense
           3. Back to main menu
    3. Quit

### Error Handling
- User can only select a valid number - 1 to 3
  - This goes for the main menu and 'Add a transaction' menu
- If the user enters an invalid option, it repeats and asks the user to select a valid option

## View Expenses
### Overview
- Three main areas to be shown
    1. Account Balance
    2. Category and their balance
    3. Print transactions
### Error Handling

## Add Income
### Overview
- Asks the user for 2 pieces of information 
  1. Description
  2. Amount 
- Does not need a category as Category array index 0 is the income category
- 
### Error Handling
- Choosing a category 
  - The user is shown an index with a name for each category
    - Index increases as it loops over the categories
    - Must be a valid number and in the range of the categories 
- Description
  - Must not be empty
- Amount 
  - Needs to be an integer and must be greater than 0
  - Must not be a string 
- Final checks 
  - Add the income amount to the account balance 
  - Update the total for the income category
  - Add a new array with the details (category, description and amount)
  
## Add Expense
### Overview
- Asks the users for 3 pieces of information
    1. Category
        - Categories are printed and the user enters an index for each value
        - Income category is at the start of categories and is skipped and not shown to the user 
    2. Description
    3. Amount 

### Error Handling
- Each element (Category, description and amount) are checked and validated
- Process one at a time and until a valid input is entered, the script repeats the failed question
- Category
  - User selects an index for the category
  - If user enters an invalid number then it repeats
- Description
  - Must not be empty
- Amount 
  - Needs to be an integer and must be greater than 0
  - Must not be a string 
- Final checks 
  - If the amount is larger than the account balance, it does not update and returns back to the main menu 
  - If the amount is smaller than the account balance
    - Update the total for the category
    - Add a new array with the details (category, description and amount)

## Quit
- Thanks the user for using 'expense tracker'
- Returns back to command line