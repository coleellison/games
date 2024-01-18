import random

def get_sorted_deck():
    """generates a sorted deck

    Returns
    -------
    list
        fresh set of 52 unshuffled cards
    """
    deck = []
    suits = ["C", "D", "H", "S"]
    for suit in suits:
        for num in range(2,15):
            card = (num, suit)
            deck.append(card)
    return deck

def get_shuffled_deck():
    """generates a shuffled deck

    Returns
    -------
    list
        shuffled full deck
    """
    deck = get_sorted_deck()
    random.shuffle(deck)
    return deck

def draw(n, input_deck = get_shuffled_deck()):
    """places new cards in hand and removes them from the deck

    Parameters
    ----------
    n : int
        number of cards requested
    input_deck : list, optional
        deck to be drawn from, by default will call for a fresh deck if no input given

    Returns
    -------
    tuple
        package of new cards and updated deck

    Raises
    ------
    Exception
        if insufficient cards are in the deck
    """
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
    """

    Returns
    -------
    tuple
        package of two five-card hands and the remaining cards of the deck
    """
    current_deck = get_shuffled_deck()
    draw1 = draw(5, current_deck)
    p1_hand = draw1[0]
    current_deck = draw1[1]
    draw2 = draw(5, current_deck)
    p2_hand = draw2[0]
    current_deck = draw2[1]
    result = (p1_hand, p2_hand, current_deck)
    return result
