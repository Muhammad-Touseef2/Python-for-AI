# ============================================================
#                    LOOPS IN PYTHON
#          for | while | do-while (simulated)
# ============================================================


# ============================================================
#  1. FOR LOOP
#     - Used when the number of iterations is known
#     - Iterates over a sequence (range, list, string, etc.)
# ============================================================

# --- Basic for loop (0 to 4) ---
print("--- Basic for loop ---")
for i in range(5):
    print(i)
print()

# --- Print "Hello World" five times ---
print("--- Print Hello World 5 times ---")
for i in range(5):
    print("Hello World")
print()

# --- range(start, stop, step) ---
print("--- range(start, stop, step) : Odd numbers from 1 to 19 ---")
for i in range(1, 20, 2):
    print(i)
print()

# --- Iterating over a list ---
print("--- Iterating over a list ---")
fruits = ["Apple", "Banana", "Cherry", "Mango"]
for fruit in fruits:
    print(fruit)
print()

# --- break : stops the loop when condition is True ---
print("--- break statement (stops at 5) ---")
for i in range(1, 10):
    if i == 5:
        break
    print(i)
print()

# --- continue : skips the value where condition is True ---
print("--- continue statement (skips odd numbers) ---")
for i in range(1, 10):
    if i % 2 != 0:
        continue
    print(i)
print()

# --- break and continue together ---
print("--- break and continue together (skip 3, stop at 7) ---")
for i in range(1, 10):
    if i == 3:
        continue    # skip 3
    if i == 7:
        break       # stop at 7
    print(i)
print()


# ============================================================
#  2. WHILE LOOP
#     - Used when the number of iterations is NOT known
#     - Runs as long as the condition remains True
# ============================================================

# --- Print 1 to 5 ---
print("--- while loop: print 1 to 5 ---")
i = 1
while i <= 5:
    print(i)
    i += 1
print()

# --- Print 5 to 1 (countdown) ---
print("--- while loop: countdown 5 to 1 ---")
i = 5
while i >= 1:
    print(i)
    i -= 1
print()

# --- break in while loop ---
print("--- while loop with break (stops at 4) ---")
i = 1
while i <= 10:
    if i == 4:
        break
    print(i)
    i += 1
print()

# --- continue in while loop (skip even numbers) ---
print("--- while loop with continue (skips even numbers) ---")
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
print()


# ============================================================
#  3. DO-WHILE LOOP (Simulated)
#     - Python has no built-in do-while loop
#     - Simulated using: while True + break
#     - Guarantees the loop body runs at LEAST once
# ============================================================

# --- Basic do-while simulation ---
print("--- do-while simulation: print 1 to 5 ---")
i = 1
while True:
    print(i)
    i += 1
    if i > 5:
        break
print()

# --- do-while with user-style input validation ---
print("--- do-while simulation: runs at least once ---")
i = 10
while True:
    print(f"Running with i = {i}")  # runs even if condition would fail upfront
    if i < 5:
        break
    i -= 3
print()

# --- do-while simulation using a flag ---
print("--- do-while using a flag variable ---")
i = 1
run = True
while run:
    print(i)
    i += 1
    if i > 5:
        run = False
print()