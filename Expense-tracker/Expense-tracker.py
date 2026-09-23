expense={}
def add_expense(expense):
    while True:
     name=input("Enter the name of your expense:-")
     if(name==""):
        print("Add name,name can't be empty")
        continue
     elif name in expense:
        print("Name already exists")
        continue
     else:
       break
    while True:
     try:
      amount=int(input("Enter the amount of your expense:"))
      if(amount<=0):
            print("amount must be greater than 0")
            continue
      expense[name]=amount
      return expense
     except ValueError:
      print("Enter a valid number")
def show_expenses(expense):
    for name,amo in expense.items():
        print(name,"->",amo)
def delete_expenses(expense):
    dele=input("Enter the expense name you want to delete : ")
    if dele in expense:
     del expense[dele]
    else:
        print("Expense doesn't exist")
    return expense
def total_expense(expense):
    total=0
    for i in expense.values():
        total+=i
    print("Your total expense is",total)


while True:
 try:
    choices=int(input("Enter your choice:1->add expense 2->view expense 3->delete expense 4->check total 5->exit: "))
    if(choices==1):
        expense=add_expense(expense)
    elif(choices==2):
        show_expenses(expense)
    elif(choices==3):
        delete_expenses(expense)
    elif(choices==4):
        if(expense=={}):
          print("No expense added yet")
        else:
         total_expense(expense)
    elif(choices==5):
        break
    else:
        print("Invalid choice!!")
 except ValueError:
    print("Enter a valid choice")




 


