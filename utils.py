# utils.py

import random

CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

def draw_card():
    return random.choice(list(CARD_VALUES.keys()))

def hand_value(hand):
    total = sum(CARD_VALUES[card] for card in hand)
    aces = hand.count('A')
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def hand_type(hand):
    if len(hand) == 2 and hand[0] == hand[1]:
        return 'pair'
    elif 'A' in hand and hand_value(hand) <= 21:
        return 'soft'
    else:
        return 'hard'
