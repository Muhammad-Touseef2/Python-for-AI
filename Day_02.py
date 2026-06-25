# Day 02 - Python Basics

# =========================
# Variables and Data Types
# =========================

name = "Touseef"
age = 18
is_adult = True
cgpa = 3.44

print(name)
print(age)
print(is_adult)
print(cgpa)


# =========================
# Taking Input
# =========================

# Input always returns a string in Python

age = int(input("Enter your age: "))
print("Your age is", age)

name = input("Enter your name: ")
print("Your name is", name)


# =========================
# If-Else Conditions
# =========================

marks = int(input("Enter your marks: "))

if marks >= 85:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")