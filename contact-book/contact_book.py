contacts={}
choice=int(input("enter your choice: 1 → Add Contact,2 → Search Contact,3 → Delete Contact,4 → View Contacts,5 → Exit:-"))
while choice!=5:
 print("Your menu is:" \
 "1 → Add Contact," \
 "2 → Search Contact," \
 "3 → Delete Contact," \
 "4 → View Contacts," \
 "5 → Exit")
 if(choice==1):
  name=input("Enter your name:")
  phone=input("Enter your phone no:")
  contacts[name]=phone
 if(choice==2):
  name=("enter the name you want to search:")
  if(name in contacts):
   print(contacts[name])
  else:
   print("Contact doesn't exist")
 if(choice==3):
  name=input("Enter the no you want to delete:")
  if(name in contacts):
   del contacts[name]
  else:
   print("Name doesn't exist")
 if(choice==4):
  for name,phone in contacts.items():
   print(name,"->",phone)
 choice=int(input("enter your choice: 1 → Add Contact,2 → Search Contact,3 → Delete Contact,4 → View Contacts,5 → Exit:-"))
 
