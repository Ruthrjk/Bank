#bank loan
age = int(input("Enter your age"))
KRA_PIN = int(input("Enter KRA PIN"))
income = float(input("Enter Income"))
if (age>21 and income>21000):
    print("you qualify for a loan")
else:
    print("You don't qualify for a loan")
