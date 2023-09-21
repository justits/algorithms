import numpy as np

# Number of people on the ship
total_people = 124

# Binomial distribution parameters
n = 10  # Number of infection attempts per day
p = 0.08  # The probability of infection in each attempt

#  Number of experiments
num_simulations = 1000

# A list for storing the results of each experiment
results = []

# Simulation of experiments
for _ in range(num_simulations):
    # Array for tracking how many days each person is sick
    days_in_quarantine = np.zeros(total_people, dtype=int)

    # As long as there are people without symptoms
    while np.any(days_in_quarantine < 14):
        # Randomly choose who to infect
        infected_today = np.random.binomial(n, p, total_people)

        # Increasing the days for infected
        days_in_quarantine[infected_today == 1] += 1

        days_in_quarantine += 1

    # The number of days it took everyone to visit the hold
    results.append(np.max(days_in_quarantine))

# Find the average value of the day
average_day = np.mean(results)

print(f"The average day when everyone was in the hold: {average_day:.2f}")