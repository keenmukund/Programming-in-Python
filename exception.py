
a=25
try:
   print("enter a number")
   b=int(input())
   print(a//b)
   raise NameError("hey")
except NameError as c:
   print("0 can't divide")
   print(c)

d=10
e=6
d, e=e, d
print(d)
print(e)


