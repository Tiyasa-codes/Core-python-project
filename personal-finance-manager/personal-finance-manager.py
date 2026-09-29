finance=[]
def add_transaction(finance):
 while True:
    name=input("Enter your expense name:")
    if(name==""):
       print("Name can't be empty")
       continue
    for i in range(len(finance)):
       if(finance[i]["name"]==name):
          print("Transaction name already exist")
          continue
    break
 while True:
  try:  
    amount=float(input("Enter the amount of your expense:"))
  except ValueError:
    print("Enter a float value please!")
    continue
  break
 type=input("Is it a expense/income,if expense type yes otherwise type no:")
 transaction={}
 finance.append(transaction)
 transaction["name"]=name
 transaction["amount"]=amount
 if(type=="yes"):
  transaction["type"]="expense"
 else:
   transaction["type"]="income"
 print("Transaction added successfully!!")
def view_transaction(finance):
 if not finance:
   print("No transaction added yet!")
 else:
   for i in range(len(finance)):
      print("name:",finance[i]["name"])
      print("amount:",finance[i]["amount"])
      print("It is",finance[i]["type"])
      print("<---------------------->")
def search_transaction(finance):
  if not finance:
      print("Transaction not added yet")
  else:
   name=input("Enter the expense name you want to search: ")
   for i in range(len(finance)):
      if(finance[i]["name"]==name):
         print("name",finance[i]["name"])
         print("amount",finance[i]["amount"])
         print("transaction type:",finance[i]["type"])
         break
   print("No matched transaction of this name")
#calculate total income,expenses and balance
def balance(finance):
   income=0
   expense=0
   for i in range(len(finance)):
      if(finance[i]["type"]=="income"):
         income+=finance[i]["amount"]
      elif(finance[i]["type"]=="expense"):
         expense+=finance[i]["amount"]
   balance=income-expense
   print("Your balance is:",balance)
#find the highest expense
def highest_expense(finance):
 if not finance:
   print("Transaction not added yet!!")
 else:
   highest_expense=0
   for i in range (len(finance)):
      if(finance[i]["type"]=="expense" and finance[i]["amount"]>highest_expense):
         highest_expense=finance[i]["amount"]
         expense=finance[i]["name"]
   print("Your highest expense is in",expense,"and amount is","->",highest_expense)
#delete transaction
def delete_transition(finance):
 if not finance:
   print("Transaction not added yet!!")
 else:
   name=input("Enter the transition name you want to delete->")
   for i in range(len(finance)):
      if(finance[i]["name"]==name):
         del finance[i]
         print("Your transaction deleted successfully!!")
      break
   else:
         print("Transaction name not present!")
def show_menu():
   print("1->Add transaction")
   print("2->View transaction")
   print("3->Search transaction")
   print("4->Find balance")
   print("5->Find highest expense")
   print("6->Delete transaction")
   print("7->Exit")
   choice=int(input("enter your choice:"))
   return choice
while True:
 try:
    choice=show_menu()
    if(choice==1):
      add_transaction(finance)
    elif(choice==2):
       view_transaction(finance)
    elif(choice==3):
       search_transaction(finance)
    elif(choice==4):
       balance(finance)
    elif(choice==5):
       highest_expense(finance)
    elif(choice==6):
       delete_transition(finance)
    elif(choice==7):
       break
    else:
       print("Invalid choice")
 except ValueError:
    print("Enter a valid choice please")
    

      