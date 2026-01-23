import numpy as np
import random



def simulate_bday(N):
    # the probability of 2 people having the same birthday
    return 1 / 365 * N * (N - 1) / 2


print(simulate_bday(23))
