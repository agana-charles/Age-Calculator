# A simple Python program to calculate age based on year of birth

# Step 1: Import datetime to get the current year
import datetime

# Step 2: Ask the user to enter their year of birth
year_of_birth = int(input("Enter your year of birth (e.g., 2000): "))

# Step 3: Get the current year from the system
current_year = datetime.datetime.now().year

# Step 4: Calculate age
age = current_year - year_of_birth

# Step 5: Display the result
print(f"You are {age} years old.")
