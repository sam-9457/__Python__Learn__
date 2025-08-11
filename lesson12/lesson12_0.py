import random

answer = [
    "hi",
    "I don`t know",
    "HaHa"
]

while True:
    player = input("")
    if player != "Bye!":
        ai = random.randint(0, 2)
        print(f"Ai: {answer[ai]}")
    else:
        print("Ai: Bye!")
        break