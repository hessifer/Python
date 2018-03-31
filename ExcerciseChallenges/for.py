# Column: name, day/month, celebrates, age
BIRTHDAYS = (
    ("James", "9/8", True, 9),
    ("Shawna", "12/6", True, 22),
    ("Amaya", "28/2", False, 8),
    ("Kamal", "29/4", True, 19),
    ("Sam", "16/7", False, 22),
    ("Xan", "14/3", False, 34),
)

# Problem 1: Celebrations
# Loop through all the people in BIRTHDAYS
# if they celebrate their birthday, print out
# "Happy Britday" and their name

print("Celebrations:")

# Solution 1 here
for entry in BIRTHDAYS:
    name, bday, celebrate, age = entry
    if celebrate:
        print("Happy Birthday {}".format(name))

print("-"*20)

# Problem 2: Half Birthdays
# Loop through all the people in BIRTHDAYS
# Calculate their half birthday (six months later)
# print out their name and half birthday
print("Half Birthdays:")

# Solution 2 here
for entry in BIRTHDAYS:
    name, bday, celebrate, age = entry
    day, month = bday.split("/")
    hbday_month = int(month) + 6
    
    if hbday_month > 12:
        hbday_month -= 12 
    print("{} {}/{}".format(name, day, hbday_month))

print("-"*20)

# Problem 3: Only School Year Birthdays
# Loop through all the people in BIRTHDAYS
# If birthday between September (9)
# and June (6), print their name
print("School Birthdays:")

# Solution 3 here
for entry in BIRTHDAYS:
    name, bday, celebrate, age = entry
    day, month = bday.split("/")

    if int(month) in range(1, 7) or int(month) in range(9, 13):
        print("{}".format(name))

print("-"*20)

# Problem 4: Wishing stars
# Loop through all the people in BIRTHDAYS
# If the person celebrates their bday and
# the person is < 10 years old
# print out their name and the number of stars equivelant to their age

# Solution 4 here
for entry in BIRTHDAYS:
    name, bday, celebrate, age = entry
    
    stars = [ '*' for _ in range(age) ]
    
    if celebrate and age <= 10:
        # print("{} - {}".format(name, '*'*age))
        print("{} - {}".format(name, ''.join(stars)))

print("-"*20)