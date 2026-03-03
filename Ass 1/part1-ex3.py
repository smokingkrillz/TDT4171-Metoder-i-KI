import numpy as np


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
