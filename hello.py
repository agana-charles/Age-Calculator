#Indexing in strings
nodes="device A,device B,device C,device D"
print(nodes)
print(nodes[8:17])

#Formatted strings
node_1= "device A"
node_2= "device B"
node_3= "device C"
node_4= "device D"
print(f"{node_1},{node_2},{node_3},{node_4}")

#Striping
user_name= "   Charles  Agana "
user_url="https://www.google.com"
print(user_name.strip())
print(user_url.lstrip("https://www."))
print(user_url.rstrip("www.google.com"))

#Concatentating
user= " Agana"
print(user.strip() + " is awesome")
print(user + "is God's child")

#Assignment
user_FN= "  Charles Agana "
user_CN= user_FN.strip()

"""using the upper function"""
user_UC= user_CN.upper()
print(user_CN)
print(user_UC)
user_SN= user_UC.split()
print(user_SN)
first_name= user_SN[0]
last_name= user_SN[-1]
print(f"First Anme: {first_name}")
print(f"Last Nsame: {last_name}")
print(first_name+"-"+last_name)

"""Findung the length of a value"""
length=len(user_UC.replace("",""))
print(length)
"""Getting the reversed name"""
reversed_name= user_UC[::-1]
print(reversed_name)

#Comparison Operators
kofi_age= 10
ama_age= 15 
print(kofi_age == ama_age)
print(kofi_age >= ama_age)
print(kofi_age <= ama_age)
print(kofi_age > ama_age)
print(kofi_age < ama_age)
print(kofi_age != ama_age)

#Bitwise operations
a= 5
b=6
a&b

#Boolean operators 
charles_age=10
ataryine_age=20
if charles_age < ataryine_age:
    print(f"charles age == ataryine age :{charles_age > ataryine_age}")
"""   
victim_ip_address= "10.10.10.10"
hacker_address= "10.10.10.01"
user_nAme=input("Kindly enter your name: ")
user_ip_address = input("Please input yor IP address: ") 
if user_ip_address==victim_ip_address:
    print(f"Hey {user_nAme}, You are prone to cyber attacks")

elif user_ip_address==hacker_address:
    print(f"Hey {user_nAme}, You are hacker, BE WARNED!!!")

else:
    print(f"{user_nAme} you are save")
"""
#Lists
ip_lists= ["10.10.10.01","10.10.10.02","10.10.10.03","10.10.10.4"]
ip_lists.append("10.10.10.00")
print(ip_lists)

ip_lists.insert(1,"10.10.10.10")
print(ip_lists)

ip_lists.pop(1)
print(ip_lists)

"""
ip_user_name= input("Please enter your name: ")
ip_user_enter= input("Please enter your IP address: ")
if ip_user_enter in ip_lists:
    print(f"Hello {ip_user_name}, call me immediately")

else:
    print(f"{ip_user_name},YOU FREE TO CONTINUE HACKING")

"""
  
#Fuctions
def intro_python():
    print('hello charles')