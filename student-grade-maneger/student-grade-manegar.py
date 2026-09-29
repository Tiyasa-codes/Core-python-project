students={}
def add_student(students):
    while True:
     name=input("Enter student name: ")
     name = name.strip()
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
   if not students:
     print("No students added yet")
   else:
     for name,data in students.items():
      print("Student","->",name)
      print("Marks","::",data["marks"])
      print("Grade","::",data["grade"])
      print("----------------")
def search_student(students):
   name=input("Enter the student name you want to search->")
   name=name.strip()
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
    count=0
    for _,data in students.items():
      total+=data["marks"]
      count+=1
    avg=total/count
    print("Average marks is",avg)
def highest_marks(students):
   if not students:
      print("No students added yet")
   else:
     highest=-1
     for name,data in students.items():
      if(data["marks"]>highest):
         highest=data["marks"]
         student=name
     print("Highest marks is",student,"::",highest)
def delete_student(students):
   name=input("Enter the student name you want to delete->")
   name=name.strip()
   name=name.title()
   if name in students:
      del students[name]
      print(" student name deleted successfully! ")
   else:
      print(" student name doesn't exist")
def show_menu():
    print("1 -> Add student")
    print("2 -> View student")
    print("3 -> Calculate average")
    print("4 -> Highest marks")
    print("5 -> Delete student")
    print("6 -> Search student")
    print("7 -> Exit")
    choice = int(input("Enter your choice: "))
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
      delete_student(students)
    elif(choice==6):
      search_student(students)
    elif(choice==7):
     break
    else:
      print("Invalid choice")
 except ValueError:
    print("Enter valid choice")
      


      



