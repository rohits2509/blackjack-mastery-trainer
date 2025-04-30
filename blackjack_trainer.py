import random
from strategy_chart import HINTS
from utils import draw_card, hand_value, hand_type

def suggest_move(player_hand, dealer_card):
    value = hand_value(player_hand)
    p_type = hand_type(player_hand)
    dealer_val = CARD_VALUES[dealer_card]
    key = (p_type, value, dealer_val)
    return HINTS.get(key, 'No Hint Available')

def play_round():
    player_hand = [draw_card(), draw_card()]
    dealer_card = draw_card()
    print(f"Your hand: {player_hand} (value: {hand_value(player_hand)})")
    print(f"Dealer shows: {dealer_card}")
    suggestion = suggest_move(player_hand, dealer_card)
    print(f"Suggested move: {suggestion}")
    user_move = input("Your move (Hit/Stand/Split/Double): ").strip().capitalize()
    if user_move == suggestion:
        print("✅ Correct!")
    else:
        print(f"❌ Incorrect. The correct move was: {suggestion}")

if __name__ == '__main__':
    while True:
        play_round()
        if input("Play another round? (y/n): ").lower() != 'y':
            break
