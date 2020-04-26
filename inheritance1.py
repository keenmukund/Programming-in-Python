class x:
   print("enter name and roll number")
   name=input()
   roll=input()

class y:
   print("Enter address")
   add=input()

class z(x,y):
   print("name is ",x.name)
   print("roll number is ",x.roll)
   print("address is ",y.add)
