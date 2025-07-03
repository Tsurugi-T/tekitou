import random

print("Rolling dice...")

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2

print(f"Die 1: {die1}")
print(f"Die 2: {die2}")
print(f"Total value: {total}")

# 勝ち負けの判定を追加
if total > 7:
    print("You won")
else:
    print("You lost")
