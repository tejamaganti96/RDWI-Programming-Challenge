import re

with open('inputs/day_4.txt', 'r') as input:
    sections = input.read().strip().split('\n\n')

def mark_cards(cards, number):
    for card in cards:
        for row_index, row in enumerate(card):
            card[row_index] = [x if x != number else None for x in row]
    return cards

def check_for_winner(cards):
    winners = []
    for card_num, card in enumerate(cards):
        row_winner = False
        for row in card:
            if len(set(row)) == 1:
                winners.append(card_num)
                row_winner = True
                break

        if row_winner:
            continue

        for col_index in range(len(card[0])):
            column = []
            for row in card:
                column.append(row[col_index])

            if len(set(column)) == 1:
                winners.append(card_num)
                break

    return winners

balls = [int(x) for x in sections[0].split(',')]

cards = []
for part in sections[1:]:
    cards.append([])
    for row in part.split('\n'):
        cards[-1].append([int(x) for x in re.findall(r'\d\d?', row)])

completed_cards = []
for ball in balls:
    cards = mark_cards(cards, ball)

    winning_indices = check_for_winner(cards)
    if winning_indices:
        for index in reversed(winning_indices):
            completed_cards.append((cards[index], ball))
            del cards[index]

        if len(cards) == 0:
            break

winning_card, winning_ball = completed_cards[0]
winning_sum = sum([sum([x for x in row if x != None]) for row in winning_card])

print("Final score of winning card:", winning_sum * winning_ball)

losing_card, losing_ball = completed_cards[-1]
losing_sum = sum([sum([x for x in row if x != None]) for row in losing_card])

print("Final score of losing card:", losing_sum * losing_ball)