#Assignment
"""
user_name="   Charles Agana"
print(user_name)
user_cleared_name=user_name.strip()
print(user_cleared_name)
user_upper_name=user_cleared_name.upper()
print(user_upper_name)
First_Name= user_upper_name[0:7]
Last_Name= user_upper_name[8:13]
print(f"First name: {First_Name}")
print(f"Last Name: {Last_Name}")
concat_name=f"{First_Name}-{Last_Name}"
print(concat_name)
length_name=len(user_upper_name.replace("",""))
print(f"Length of Name: {length_name}")
if "A" in user_upper_name:
    print("True")
else:
    print("False")

reversed_name=user_upper_name[::-1]
print(reversed_name)
"""
"""
name="Jeff Charles Agana Ato"
first=name.split()[1]
last=name.split()[0]
print(f"first name: {first}")
print(f"last name: {last}")
"""
"""
user_name=input("Please Enter Your First Name:")
user_sex=input("please enter your gender:")
user_ip_address=input("Please Enter your IP address: ")
victim_ip_addresses=["10.10.10.10","10.10.10.00","10.10.10.01","10.10.10.02"]
if user_ip_address in victim_ip_addresses:
    print(f"Hey Mr.{user_name.upper().split()[0]},your device is vulnurable")
else:
    print(f"Hey Mr.{user_name.upper().split()[0]},Your device is safe")
"""
"""
victim_ip_addresses=["10.10.10.10","10.10.10.00","10.10.10.01","10.10.10.03","10.10.10.04"]
victim_ip_addresses.append("10.10.10.05")
victim_ip_addresses.insert(3,"10.10.10.02")
victim_ip_addresses.pop(0)
print(victim_ip_addresses)
for i in victim_ip_addresses:
    print(i)
"""
"""
counting_numbers=[]
for i in range(0,21):
    counting_numbers.append(i)
for number in counting_numbers:
    print(number)
"""
#Dictionary 
"""
ip_dictionary={"device_a":"10.10.10.01","device_b":"10.10.10.02","device_c":"10.10.10.10"}
for key in ip_dictionary.items():
print(ip_dictionary["device_a"])
ip_dictionary["device_d"]="10.10.10.00"
print(ip_dictionary)
"""
"""
#Functions
def my_function(a):
   return 5*a
print(my_function(10))
"""
#Classes
class Mobile_Phone:
    def __init__(self, brand, model):
     self.brand = brand
     self.model = model
    
    def turn_on(self):
       print("Mobile phone is on")

    def turn_off(self):
       print("Mobile phone is off")
    
    def make_call(self):
       print("Phone is calling")

    def send_message(self,message,number):
       print(f"sending {message} to {number}")

phone_1= Mobile_Phone("Apple","!6 Pro max")

phone_1.turn_on()
phone_1.turn_off()
phone_1.send_message("Hello Jesus",+223592931925)










