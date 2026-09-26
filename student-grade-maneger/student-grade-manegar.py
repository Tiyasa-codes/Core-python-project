students={}
def add_student(students):
    while True:
     name=input("Enter student name: ")
     name=name.title()
     if name in students:
       print("Student already exists")
       continue
     if(name==""):
       print("Name can't be empty")
       continue
     break
    while True:
     try:
      marks=int(input("Enter marks: "))
      if(marks<0 or marks>100):
       print("Enter no between 0 and 100")
       continue
      if(marks>=90):
         grade="A+"
      elif(marks>=80):
          grade="A"
      elif(marks>=70):
        grade="B+"
      elif(marks>=60):
        grade="B"
      elif(marks>=50):
        grade="C"
      elif(marks>=40):
        grade="D"
      else:
        grade="F"
      
      break
     except ValueError:
      print("Enter an integer")
    
    students[name]={
        "marks":marks,
        "grade":grade
      }
    print("Student successfully added!!")  
def view_student(students):
   for name,data in students.items():
      print("Student","->",name)
      print("Marks","::",data["marks"])
      print("Grade","::",data["grade"])
      print("----------------")
def search_student(students):
   name=input("Enter the student name you want to search->")
   name=name.title()
   if name in students:
      print(name,"::",students[name]["marks"],"::",students[name]["grade"])
   else:
      print("Student doesn't exist")
def calculate_average(students):
   if not students:
      print("No students added yet")
   else:
    total=0
    ct=0
    for name,data in students.items():
      total+=data["marks"]
      ct+=1
    avg=total/ct
    print("Average marks is",avg)
def highest_marks(students):
   if not students:
      print("List is empty")
   else:
     high=0
     for name,data in students.items():
      if(data["marks"]>high):
         high=data["marks"]
         na=name
     print("Highest marks is",na,"::",high)
def delete_students(students):
   name=input("Enter the student name you want to delete->")
   name=name.title()
   if name in students:
      del students[name]
      print(" student name deleted successfully! ")
   else:
      print(" student name doesn't exist")
def show_menu():
   choice=int(input("enter your choice:1->Add student 2->View student 3->calculate average 4->highest marks 5->delete student 6->search student 7->exit->"))
   return choice
while True:
 try:
    choice=show_menu()
    if(choice==1):
      add_student(students)
    elif(choice==2):
      view_student(students)
    elif(choice==3):
      calculate_average(students)
    elif(choice==4):
      highest_marks(students)
    elif(choice==5):
      delete_students(students)
    elif(choice==6):
      search_student(students)
    elif(choice==7):
     break
    else:
      print("Invalid choice")
 except ValueError:
    print("Enter valid choice")
      


      



