from scoring import *

def cpu_choice(hand):
    """
    Parameters
    ----------
    hand : input hand
        the hand of the computer player

    Returns
    -------
    the cards the computer selects to keep
    """
    if royalflush(hand):
        return hand
    if straightflush(hand):
        return hand
    if fourofakind(hand):
        hand_score = fourofakind(hand)
        if hand_score[2] < 8:
            new_hand = []
            for card in hand:
                if card[0] == hand_score[1]:
                    new_hand.append(card)
            return new_hand
        return hand
    if fullhouse(hand):
        return hand
    if flush(hand):
        return hand
    if straight(hand):
        return hand
    if threeofakind(hand):
        hand_score = fourofakind(hand)
        if hand_score[2] < 8:
            new_hand = []
            for card in hand:
                if card[0] == hand_score[1]:
                    new_hand.append(card)
            return new_hand
        return hand
    if twopairs(hand):
        hand_score = twopairs(hand)
        if hand_score[3] < 8:
            new_hand = []
            for card in hand:
                if card[0] == hand_score[1] or card[0] == hand_score[2]:
                    new_hand.append(card)
            return new_hand
        return hand
    if onepair(hand):
        hand_score = onepair(hand)
        new_hand = []
        for card in hand:
            if card[0] == hand_score[1]:
                new_hand.append(card)
        return new_hand
    else:
        hand_score = highcard(hand)
        new_hand = []
        for card in hand:
            if card[0] == hand_score[1]:
                new_hand.append(card)
                return new_hand