if __name__ == '__main__':
    select_organizers = {int(i) for i in input().split(' ')}
    num_tickets = int(input())
    for _ in range(num_tickets):
        lottery_ticket = {int(i) for i in input().split(' ')}
        good_num = lottery_ticket.intersection(select_organizers)
        print('Lucky' if len(good_num) >= 3 else 'Unlucky')
