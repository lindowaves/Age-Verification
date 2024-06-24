# 1. Implement Defensive Techniques:
# We need to ensure that the user inputs a 4_digit number as their 'Year Of Birth' by using a While Loop.
# the len() function enures that the input is 4 characters
# the isdigit() method ensures that the input is a digit string, not letter string.
# the int() function converts the string into an integer because we can't subtract integers with a string.

while True:
    year = input("Enter Year Of Birth: ")
    if len(year) == 4 and year.isdigit():
        year = int(year)
        break
    else:
        print("Invalid Input, please enter a 4-digit number")

# 2. Determine the user's age
age = (2024 - year)

# 3. Verify if the user meets the age requirment and Display the result.
if age == 18 or age >= 18:
    print("Congrats, You Are Old Enough!")
else:
    print("You Are Not Old Enough!")
