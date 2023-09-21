import itertools

deck = list(range(7, 15)) * 4

fifty_point_combinations = 0
total_combinations = 0

for combination in itertools.combinations(deck, 6):
    fifty_point_combinations += sum(combination) == 50
    total_combinations += 1

print(round(fifty_point_combinations / total_combinations, 6))
