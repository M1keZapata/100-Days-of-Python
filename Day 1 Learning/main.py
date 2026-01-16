# This is my very first Python program - Practicing printing
print("This is a great time!")
print("What a beautiful day!")

# Practicing Variable assignment
first_name = "Mike"
hometown = "New York"
age = "Ancient"
favorite_team = "New York Yankees"

#Data types
string_practice = "This is a string" #String -----------------  
integer_practice = 123 #Integer -----------------------------
float_practice = 123.456 #Float -------------------------------
boolean_practice = True #Boolean -------------------------------

# Using F-Strings
print(f"Hi, my name is {first_name}, and I am from {hometown}.")
print(f"{hometown} is home to the thin crust pizza and the world famous {favorite_team}.")

# Typecasting Data Types    
print(str(boolean_practice))
print(int(float_practice))
print(float(integer_practice))

#Accepting User Input
''' snack = input("What is Scooby's famous snack called?: ")
best_friend = input("Who is his Scooby's best friend?: ")
car = input("What is his group's car called?: ")'''

# Day 1 Challenge -- Create a story using the user input
starting_lives = input("How many lives do you want to start with?: ")
adventure_type = input("What type of adventure do you want to go on? (Scary, Fun, or Relaxing): ")
crew_number = input("How many people are in your crew?: ")

print(f"You have {starting_lives} lives\nand you went on a {adventure_type} adventure\nwith {crew_number} people.. and you actually survived!\nThat's great!... ")
