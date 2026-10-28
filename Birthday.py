
import time
import random

print("=" * 40)
print("       HAPPY BIRTHDAY TO ME!")
print("=" * 40)

name = input("\nBirthday star ka naam batao: ").strip()

if name == "":
    name = "Birthday Star"

print("\nPreparing your birthday surprise...")
time.sleep(1)

print("\nLoading happiness...")
time.sleep(1)

print("\n" * 2)

for i in range(3, 0, -1):
    print("Surprise in", i, "...")
    time.sleep(1)

print("\n" + "*" * 40)
print("       HAPPY BIRTHDAY,", name.upper())
print("*" * 40)

print(r"""
              i   i   i
             _|___|___|_
            |           |
            |   CAKE!   |
            |___________|
           |             |
           |_____________|
          /_______________\
""")

print("\nLet the celebration begin!\n")

for i in range(3):
    print(" ".join(random.choice(["*", "+", "o", "~"]) for _ in range(30)))
    time.sleep(0.3)

print("\nA SPECIAL MESSAGE FOR YOU")
print("-" * 40)

messages = [
    "May your dreams come true!",
    "May your life be full of happiness!",
    "Keep smiling and keep growing!",
    "Believe in yourself every day!",
    "This year is your chance to shine!"
]

for message in messages:
    print(message)
    time.sleep(0.5)

print("\n" + "=" * 40)
print("  TODAY IS YOUR DAY, " + name.upper() + "!")
print("  Celebrate, Smile and Enjoy!")
print("=" * 40)

input("\nPress Enter to finish your celebration...")
