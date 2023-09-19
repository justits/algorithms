def check(participants, n):
    num_of_tours = n.bit_length()

    # Check the number of participants
    if len(participants) != (1 << num_of_tours):
        return 'NO SOLUTION'

    finalists = []
    num_of_participants = [0] * num_of_tours
    opponents_of_participants = [set() for _ in range(num_of_tours)]

    for surname, opponents in participants.items():
        num_of_games = len(opponents)

        # Number of games can't be more than number of tours
        if num_of_games > num_of_tours:
            return 'NO SOLUTION'

        if num_of_games == num_of_tours:
            finalists.append(surname)

        num_of_participants[num_of_games - 1] += 1
        opponents_of_participants[num_of_games - 1].update(opponents)

    # The number of participants who have played only i games should be 2^(num_of_tours-i)
    correct_participants = [1 << i for i in range(num_of_tours - 1, 0, -1)] + [2]
    if num_of_participants != correct_participants:
        return 'NO SOLUTION'

    # The opponents of the participants who have played only i games do not overlap
    correct_opponents = [correct_participants[i] * (i + 1) for i in range(num_of_tours)]
    if [len(i) for i in opponents_of_participants] != correct_opponents:
        return 'NO SOLUTION'

    return ' '.join(finalists)


if __name__ == "__main__":
    n = int(input())
    participants = {}
    for _ in range(n):
        participant_1, participant_2 = input().split(' ')
        participants[participant_1] = participants.get(participant_1, []) + [participant_2]
        participants[participant_2] = participants.get(participant_2, []) + [participant_1]
    print(check(participants, n))
