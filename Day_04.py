# =========================
# Strings in Python
# =========================

text = "Muhammad Touseef"

# Check the data type
print(type(text))  # <class 'str'>


# =========================
# String Indexing
# =========================

print(text[0])            # First character
print(text[-len(text)])   # First character using a negative index


# =========================
# Print String Using a Loop
# =========================

for i in range(len(text)):
    print(text[i], end="")

print()  # Move to the next line


# =========================
# String Slicing
# =========================
# Syntax:
# string[start : stop : step]

print(text[0:8:1])   # Muhammad
print(text[0:8:2])   # Mhmad
print(text[0:8:3])   # Maa

print(text[::])      # Complete string
print(text[::-1])    # Reverse the string