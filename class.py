a=5
class xyz:
   a=10
   print("inside class")
   def input1(self,name,roll):
      self.name=name
      self.roll=roll,
      print(self.name,self.roll)
   def __init__(self,n1,n2):
       print("constructor is cllaed")
       self.n1=n1
       self.n2=n2
       #c
       c=n1+n2
       print(self.n1,self.n2)
       print(c)
      
print(xyz.a)
ob=xyz("p","q")
ob.input1("abhay",123)
