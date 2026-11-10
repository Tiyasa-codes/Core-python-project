tasks=[]
def add_task(tasks):
 name=input("Enter your task-")
 while True:
    status=(input("Enter status:True/False->"))
    if(status=="True"):
        status="Completed"
    elif(status=="False"):
        status="Pending"
    else:
        print("Invalid input")
        continue
    break
 NEW_ITEM={}
 NEW_ITEM["name"]=name
 NEW_ITEM["status"]=status
 tasks.append(NEW_ITEM)
 print("Task added successfully")
def view_task(tasks):
   while True:
      if(tasks==[]):
         print("List is empty")
         break
      for i in range(len(tasks)):
       print(i+1,".","  ",tasks[i]["name"],"-->",tasks[i]["status"])
      break
def complete_task(tasks):
 while True:
   task_no=int(input("Enter the task no you completed:"))
   if(task_no<1 or task_no>len(tasks)):
      print("Enter valid task_no")
      continue
   if(tasks[task_no-1]["status"]=="Pending"):
      tasks[task_no-1]["status"]="Completed"
      print("Task mark as completed!")
   else:
      print("you already marked it as completed!")
   break
def delete_task(tasks):
   while True:
    task_no=int(input("Enter the task no you want to delete:"))
    if(task_no<1 or task_no>len(tasks)):
       print("Enter valid task no!")
       break
    del tasks[task_no-1]
    print("Task deleted successfully!")
    break
def show_menu():
 print("1->Add task")
 print("2->View task")
 print("3->Complete task")
 print("4->Delete task")
 print("5->Exit")
 menu=int(input("Enter the task no you want to perform:"))
 return menu
while True:
   menu=show_menu()
   if(menu==1):
      add_task(tasks)
   elif(menu==2):
       view_task(tasks)
   elif(menu==3):
      complete_task(tasks)
   elif(menu==4):
      delete_task(tasks)
   elif(menu==5):
      break
   else:
      print("Invalid input")
      continue
   

      
