#basic syntax
"""
(#)single line commenting
Multi line comment
user_name="charles";user_age=19;user_height=12.5
print(f"{user_name},{user_age},{user_height}")
user_school="saint francis\
 xavier minor\
seminary"
print(user_school)
"""
"""
user_name="charles agana"
print(f"First Name: {user_name[0:7]}")
x="agana"
y=19
z=12.7
y=str(19)
print(type(y))
"""
"""
kofi_age= 12
ama_age= 15
if kofi_age<ama_age:
    print("Jesus is lord")
else:
    print("Jesus is still lord")
"""
"""
my_stuff=["pen","book","eraser","mouse","router",78]
print(my_stuff)
my_stuff.append("Jesus")
print(my_stuff)
my_stuff[3]="Airpods"
print(my_stuff)
del my_stuff[2]
print(my_stuff)
edit=my_stuff.pop(4)
print(my_stuff)
print(edit)
print(my_stuff[4])
"""

my_library={"Name":"charles","Age":12}
my_library["height"]=34;my_library["gender"]="male/female"
print(my_library["Name"])
my_library["Name"]="Kenneth"
print(my_library)
del my_library["height"]
print(my_library)

animals=open("Animals.txt","a+")
text= animals.read()
print(text)
animals.seek(0)