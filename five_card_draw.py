from scoring import *
from deck import *
from display import *
from five_card_cpu import *

if __name__ == "__main__":
    status = input("Press Enter to start")
    while status.lower() != "q" and status.lower() != "quit":
        print("\n" * 50)
        p1, p2, curr_deck = initiate_round()
        print("Select which cards to keep:\n")
        print(show_hand(p1))
        for i in range(1,6):
            print(" " * 7, f"({i})", " " * 7, end = "")
        
        choice = input("\n\n")
        keep = set()
        for i in range(1,6):
            if str(i) in choice:
                keep.add(i - 1)
        new_hand = []
        for i in keep:
            new_hand.append(p1[i])
        p1 = new_hand
        p1draw = 5 - len(p1)
        p2choice = cpu_choice(p2)
        p2draw = 5 - len(p2)
        totaldraw = p1draw + p2draw

        drawn_cards, curr_deck = draw(totaldraw, curr_deck)
        p1 += drawn_cards[:p1draw]
        p2 += drawn_cards[p1draw:]

        print("\n\n\n")
        if score(p1) > score(p2):
            print("You won :)")
        elif score(p1) < score(p2):
            print("You lost :(")
        else:
            print("You tied :|")

        print("\nYour hand:")
        print(show_hand(p1))
        print(show_score(p1))
        print("\n CPU's hand:")
        print(show_hand(p2))
        print(show_score(p2),"\n\n\n")

        status = input("Press Enter to play again, or q to quit\n")