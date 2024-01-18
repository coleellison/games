from fcd_scoring import *

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
        #keep the hand
        return hand
    if straightflush(hand):
        #keep the hand
        return hand
    if fourofakind(hand):
        #if the off-card is low, try for a better one. with only one deck, it won't ever change the outcome though <:)
        hand_score = fourofakind(hand)
        if hand_score[2] < 8:
            new_hand = []
            for card in hand:
                if card[0] == hand_score[1]:
                    new_hand.append(card)
            return new_hand
        return hand
    if fullhouse(hand):
        #keep the hand
        return hand
    if flush(hand):
        #keep the hand
        return hand
    if straight(hand):
        #keep the hand
        return hand
    if threeofakind(hand):
        #try for better off-cards if they are low.
        hand_score = fourofakind(hand)
        if hand_score[2] < 8:
            new_hand = []
            for card in hand:
                if card[0] == hand_score[1]:
                    new_hand.append(card)
            return new_hand
        return hand
    if twopairs(hand):
        #try for a better off-card if it is low
        hand_score = twopairs(hand)
        if hand_score[3] < 8:
            new_hand = []
            for card in hand:
                if card[0] == hand_score[1] or card[0] == hand_score[2]:
                    new_hand.append(card)
            return new_hand
        return hand
    if onepair(hand):
        #throw away all off-pair cards
        hand_score = onepair(hand)
        new_hand = []
        for card in hand:
            if card[0] == hand_score[1]:
                new_hand.append(card)
        return new_hand
    else: #high card
        #throw away everything except for the high card
        hand_score = highcard(hand)
        new_hand = []
        for card in hand:
            if card[0] == hand_score[1]:
                new_hand.append(card)
                return new_hand
