import time
import tkinter
import calendar


d1={"Name":"Abhay", "Age":"26", "Class":"MCA"}
print(d1)
d1["Address"]="Patna"
print(d1)
print("hello",end=" ")
print("world")
del(d1["Name"])
sec=("Name","age")
d1=d1.fromkeys(sec,10)
print(d1)
print(d1.get("Name"))
print(d1.keys())
d1.setdefault("address",None)
d2={1:"a",2:"b",3:"c"}
d1.update(d2)
ticks=time.time()
print(ticks)
lc=time.localtime()
print(lc)
print(time.asctime())
print(calendar.month(2018,5))

