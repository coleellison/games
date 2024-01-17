display_dict = {
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
    11: "J",
    12: "Q",
    13: "K",
    14: "A",
   "C": '♣',
   "D": '♦',
   "H": '♥',
   "S": '♠'
}

def card_string(card):
    """

    Helper function for show_hand

    Parameters
    ----------
    card : input card
        the card to be displayed

    Returns
    -------
    the card's appearance in multi-line string form
    """
    card_num = display_dict[card[0]]
    card_suit =  display_dict[card[1]]
    if card_num == "10":
        card_display = f"""+-------+
|{card_num}     |
|       |
|   {card_suit}   |
|       |
|     {card_num}|
+-------+"""
    else:
        card_display = f"""+-------+
|{card_num}      |
|       |
|   {card_suit}   |
|       |
|      {card_num}|
+-------+"""
    return card_display

def show_hand(hand):
    """
    Parameters
    ----------
    hand : input hand
        hand to be read

    Returns
    -------
    hand_str
        a multi-line string of all card displays, concatenated into one print statement.
    """
    display_list = []
    for card in hand:
        current_card = card_string(card).split("\n")
        display_list.append(current_card)
    hand_str = ""
    for row_id in range(7):
        for card_id in range(len(display_list)):
            hand_str += 5 * " " + display_list[card_id][row_id] + 5 * " "
        hand_str += "\n"
    hand_str = hand_str[:-2]
    return hand_str