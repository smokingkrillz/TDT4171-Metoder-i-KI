import random
import numpy as np

# going broke simulation
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


# birthday problem simulation part a


def birthday_problem(num_people: int, num_simulations: int = 1000):
    """Simulate the birthday problem to estimate the probability
    that at least two people in a group share the same birthday.

    Args:
       num_people : Number of people in the group.
       num_simulations : Number of simulations to run.
    Returns:
       Estimated probability that at least two people share a birthday.
    """
    shared = 0

    for i in range(num_simulations):
        # generate random birthdays for num_people
        birthdays = np.random.randint(0, 365, size=num_people)
        # birthdays set will remove duplicates
        if len(birthdays) != len(set(birthdays)):
            shared += 1
    return shared / num_simulations


def birthday_2():

    N = 11
    possibilites = []
    for N in range(10, 51):
        prob = birthday_problem(N, num_simulations=10000)
        if prob >= 0.5:
            possibilites.append((N, prob))
            print(f"Number of people: {N}, Probability of shared birthday: {prob:.4f}")

    return possibilites


if __name__ == "__main__":
    birthday_2()


# part 2

import numpy as np


def Peter_bday():
    number = 0
    total_bdays = []
    while total_bdays.__len__() < 365:
        birthday = np.random.randint(0, 365)
        if birthday not in total_bdays:
            total_bdays.append(birthday)
        number += 1
    return number


if __name__ == "__main__":
    simulations = 1000
    results = np.zeros(simulations)
    for i in range(simulations):
        results[i] = Peter_bday()
    print(f"Expected group size: {np.mean(results):.2f}")

