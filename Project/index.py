# Program to check exam eligibility based on attendance

name = input("Enter your name: ")
attendance = float(input("Enter your attendance percentage: "))

if attendance >= 75:
    print(f"{name}, you are eligible to appear for the exam.")
else:
    print(f"{name}, you are not eligible to appear for the exam.")
    print("Minimum required attendance is 75%.")