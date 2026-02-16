
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

