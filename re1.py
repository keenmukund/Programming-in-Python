
import re
xx = "guru99,education is fun"
r1 = re.findall(r"^\w+",xx)
print (r1)


phone = "2004-959-559 # This is Phone Number"


num = re.sub(r'#.*$', "", phone)
print ("Phone Num : ", num)


num = re.sub(r'\D', "", phone)    
print ("Phone Num : ", num)
