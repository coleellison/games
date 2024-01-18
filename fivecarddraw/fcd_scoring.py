"""
We will arbitarily assign point scores to each hand type for comparison purposes:

Royal flush: 9
Straight flush: 8
Four of a kind: 7
Full house: 6
Flush: 5
Straight: 4
Three of a kind: 3
Two pair: 2
One pair: 1
High card: 0
"""

#separate cards into their suits and numeric values
suits = lambda hand: [i[1] for i in hand]
nums = lambda hand: [i[0] for i in hand]

def royalflush(hand):
    #10, J, Q, K, A of the same suit
    s = suits(hand)
    flush = True
    for i in range(4):
        if s[i] != s[i + 1]:
            flush = False
    if not flush:
        return False
    n = nums(hand)
    n.sort()
    if n != [10,11,12,13,14]:
        return False
    return [9]

def straightflush(hand):
    #five consecutive cards of the same suit
    s = suits(hand)
    flush = True
    for i in range(4):
        if s[i] != s[i + 1]:
            flush = False
    if not flush:
        return False
    n = nums(hand)
    n.sort()
    straight = True
    if n == [2,3,4,5,14]:
        return [8, 5]
    for i in range(4):
        if n[i] + 1 != n[i + 1]:
            straight = False
    if not straight:
        return False
    return [8, n[-1]]
    
def fourofakind(hand):
    #four of the same number
    n = nums(hand)
    counts = [(n.count(i), i) for i in range(2,15)]
    counts.sort(reverse=True)
    if counts[0][0] == 4:
        return [7, counts[0][1], counts[1][1]]
    return False

def fullhouse(hand):
    #three of the same number, two of the same number
    n = nums(hand)
    counts = [(n.count(i), i) for i in range(2,15)]
    counts.sort(reverse=True)
    if (counts[0][0] == 3 and counts[1][0] == 2):
        return [6, counts[0][1], counts[1][1]]
    return False

def flush(hand):
    #all suits the same
    s = suits(hand)
    for i in range(4):
        if s[i] != s[i + 1]:
            return False
    n = nums(hand)
    n.sort(reverse=True)
    n.insert(0, 5)
    return n

def straight(hand):
    #five consecutive cards
    n = nums(hand)
    n.sort()
    straight = True
    if n == [2,3,4,5,14]:
        return [8, 5]
    for i in range(4):
        if n[i] + 1 != n[i + 1]:
            straight = False
    if not straight:
        return False
    return [4, n[-1]]

def threeofakind(hand):
    #three of the same number
    n = nums(hand)
    counts = [(n.count(i), i) for i in range(2,15)]
    counts.sort(reverse=True)
    if counts[0][0] == 3:
        output = [3, counts[0][1]]
        while counts[0][1] in n:
            n.remove(counts[0][1])
        n.sort(reverse=True)
        for i in n:
            output.append(i)
        return output
    return False

def twopairs(hand):
    #two groups of two matching numbers
    n = nums(hand)
    counts = [(n.count(i), i) for i in range(2,15)]
    counts.sort(reverse=True)
    if (counts[0][0] == 2 and counts[1][0] == 2):
        return [2, counts[0][1], counts[1][1], counts[2][1]]
    return False

def onepair(hand):
    #two matching numbers
    n = nums(hand)
    counts = [(n.count(i), i) for i in range(2,15)]
    counts.sort(reverse=True)
    if (counts[0][0] == 2 and counts[1][0] == 1):
        return [1, counts[0][1], counts[1][1], counts[2][1], counts[3][1]]
    return False

def highcard(hand):
    #nothing better :/
    n = nums(hand)
    n.sort(reverse=True)
    n.insert(0,0)
    return n

def score(hand):
    """scores hand according to type, then value

    Parameters
    ----------
    hand : list
        input hand

    Returns
    -------
    list
        a list containing all data needed to rank the hand
    """
    if royalflush(hand):
        return royalflush(hand)
    if straightflush(hand):
        return straightflush(hand)
    if fourofakind(hand):
        return fourofakind(hand)
    if fullhouse(hand):
        return fullhouse(hand)
    if flush(hand):
        return flush(hand)
    if straight(hand):
        return straight(hand)
    if threeofakind(hand):
        return threeofakind(hand)
    if twopairs(hand):
        return twopairs(hand)
    if onepair(hand):
        return onepair(hand)
    return highcard(hand)

card_names = { #for show_score
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
    11: "Jack",
    12: "Queen",
    13: "King",
    14: "Ace"
}

def show_score(hand):
    """conveys a relevant and abridged score to user

    Parameters
    ----------
    hand : list
        input hand
    """
    val = score(hand)
    hand_names = {
    9: f"Royal flush!",
    8: f"Straight flush: {card_names[val[1]]} high",
    7: f"Four of a kind: {card_names[val[1]]}s",
    6: f"Full house: {card_names[val[1]]}s and {card_names[val[2]]}s",
    5: f"Flush: {card_names[val[1]]} high",
    4: f"Straight: {card_names[val[1]]} high",
    3: f"Three of a kind: {card_names[val[1]]}s",
    2: f"Two pair: {card_names[val[1]]}s and {card_names[val[2]]}s",
    1: f"Pair of {card_names[val[1]]}s",
    0: f"{card_names[val[1]]} high"
}
    return hand_names[val[0]]
