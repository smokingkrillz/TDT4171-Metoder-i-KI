import random
import numpy as np

symbols = ["BAR", "BELL", "LEMON", "CHERRY"]


def slot_machine():
    result = []
    for i in range(3):
        result.append(random.choice(symbols))
    return result


def payout(s):

    if s[0] == s[1] == s[2] and s[0] == "BAR":
        return 20
    if s[0] == s[1] == s[2] and s[0] == "BELL":
        return 15
    if s[0] == s[1] == s[2] and s[0] == "LEMON":
        return 5
    if s[0] == s[1] == s[2] and s[0] == "CHERRY":
        return 3
    if s[0] == s[1] and s[0] == "CHERRY":
        return 2
    if s[0] == "CHERRY":
        return 1
    return 0


def plays_until_broke(start=10):
    bankroll = start
    plays = 0
    while bankroll > 0:
        s = slot_machine()
        prize = payout(s)
        bankroll += prize - 1
        plays += 1
    return plays


total_plays = np.zeros(5000)
# simulate
for i in range(5000):
    plays = plays_until_broke()
    total_plays[i] = plays
# mean
mean_plays = total_plays.mean()
print("Mean plays until broke:", mean_plays)

# calculate median
median_plays = np.median(total_plays)
print("Median plays until broke:", median_plays)
