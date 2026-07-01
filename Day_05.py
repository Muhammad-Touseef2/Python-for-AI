"""
Python Operators

This file covers the following operators:
1. Arithmetic Operators
2. Assignment Operator
3. Compound Assignment Operators
4. Comparison Operators
5. Logical Operators
"""

# ==========================================
# Arithmetic Operators
# (+, -, *, /, %, //, **)
# ==========================================

# a = 10
# b = 20

# print(a + b)    # Addition
# print(a - b)    # Subtraction
# print(a * b)    # Multiplication
# print(a / b)    # Division
# print(a // b)   # Floor Division (removes decimal part)
# print(a % b)    # Modulus (remainder)
# print(a ** 2)   # Exponent (power)


# ==========================================
# Assignment Operator
# (=)
# ==========================================

# a = 10
# b = a
# print(b)


# ==========================================
# Compound Assignment Operators
# (+=, -=, *=, /=, //=, %=, **=)
# ==========================================

# a = 10
# a += 5
# a += 10
# a += 20
# print(a)        # 45

# b = 20
# b -= 5
# print(b)        # 15

# c = 15
# c *= 2
# print(c)        # 30

# d = 20
# d /= 4
# print(d)        # 5.0

# e = 20
# e //= 4
# print(e)        # 5

# f = 20
# f %= 3
# print(f)        # 2

# g = 4
# g **= 2
# print(g)        # 16


# ==========================================
# Comparison Operators
# (==, !=, >, <, >=, <=)
# Returns True or False
# ==========================================

# a = 10
# b = 20

# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)


# ==========================================
# Logical Operators
# (and, or, not)
# ==========================================

# AND: Returns True only if all conditions are True.
print(45 > 30 and 30 > 15)      # True
print(45 > 30 and 30 > 31)      # False

# OR: Returns True if at least one condition is True.
print(45 > 30 or 30 > 31)       # True
print(15 != 15 or 15 < 15 or 15 > 15)   # False

# NOT: Reverses the Boolean result.
print(not (45 > 30 or 30 > 31)) # False