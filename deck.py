import random

def get_sorted_deck():
    deck = []
    suits = ["C", "D", "H", "S"]
    for suit in suits:
        for num in range(2,15):
            card = (num, suit)
            deck.append(card)
    return deck

def get_shuffled_deck():
    deck = get_sorted_deck()
    random.shuffle(deck)
    return deck

def draw(n, input_deck = get_shuffled_deck()):
    if n < 1:
        return -1
    elif type(n) != int:
        return -1
    elif n > len(input_deck):
        raise Exception("Error: The deck is empty")
    else:
        drawn_cards = input_deck[:n]
        new_deck = input_deck[n:]
        return (drawn_cards, new_deck)

def initiate_round():
    current_deck = get_shuffled_deck()
    draw1 = draw(5, current_deck)
    p1_hand = draw1[0]
    current_deck = draw1[1]
    draw2 = draw(5, current_deck)
    p2_hand = draw2[0]
    current_deck = draw2[1]
    result = (p1_hand, p2_hand, current_deck)
    return result