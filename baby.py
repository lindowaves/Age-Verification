# This program tests if a user is 18 or older and allowed entry into a party.

# 1. Ask the user their year of birth
year = int(input("Enter Year Of Birth: "))

# 2. Determine the user's age
age = (2024 - year)

# 3. Determine if the user meets the age requirment and Display thr result.
if age == 18 or age >= 18:
    print("Congrats, You Are Old Enough")
elif age <= 18:
    print("You Are Not Old Enough")