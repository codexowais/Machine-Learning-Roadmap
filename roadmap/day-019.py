# # Day 019 - NumPy Random and Simulation
#
# Learn: random numbers, seeds, random samples, simple simulations.
#
# Math checkpoint (Required foundation): learn basic probability, outcomes,
# frequency, samples, and why randomness appears in ML experiments.
#
# Practice: simulate 100 dice rolls and count results.
#
# Output: print frequency of each dice face.
#
# Review: why do we set a random seed?
#

# Code here
import numpy as np
np.random.seed(42)

# dice_roll = np.random.randint(1,7,size = 100)

# for face in range(1,7):
#     count = np.sum(dice_roll == face)
#     print(f"Face {face}:{count}")


coin_tosses = np.random.choice(
    ["Heads", "Tails"],
    size=50
)

unique, counts = np.unique(coin_tosses, return_counts=True)

print(unique)
print(counts)
