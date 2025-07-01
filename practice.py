"""
user_name= \
  "charles"\
 "Agana"
print(user_name)
number=6
number1=6.0
num_string=str(number1)
print(num_string)
print(type(num_string))
"""
"""
age= 455
if age>= 18:
    print("You are an old person")   
elif age>= 12:
    print("You are an adult")
else:
    print("You are a child")   

my_list= [12,10,"charles",True,4.5,"hello"]
my_list.append(88)
print(my_list)
my_list.append("fish")
print(my_list)
my_list[4]=6.6
print(my_list)
del my_list[5]
print(my_list)
print(my_list[3])
"""
"""
def my_fn():
    print("hello")

def add(n1,n2):
    print(n1 + n2)
#calling the fuction
my_fn()
add(4,6)
"""
#class
"""
class Person:
    name= None
    age= None

def __inti__(self,name,age):
    self.name= name
    self.age=age

def say_name(self):
    print("My name is %s" % self.name)
def say_age(self):
    print("My age is %d" % self.age)
"""
import carlyne
phone_2=carlyne.Mobile_Phone("Samsung","S42 Ultra")
phone_2.make_call()
phone_2.send_message("Hello chief",233592931925)
phone_2.turn_on()