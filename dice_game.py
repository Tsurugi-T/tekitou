import random

# ユーザーに名前を尋ねる (experimentalブランチの機能)

name = input("What is your name? > ")

print(f"Hello, {name}!")

print("Rolling dice...")

die1 = random.randint(1, 6)

die2 = random.randint(1, 6)

total = die1 + die2

print(f"Die 1: {die1}")

print(f"Die 2: {die2}")

print(f"Total value: {total}")

# 勝ち負けの判定 (masterブランチの機能) をユーザー名で表示するように修正

if total > 7:

    print(f"{name} won!")

else:

    print(f"{name} lost!")

