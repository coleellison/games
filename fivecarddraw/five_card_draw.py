from fcd_scoring import *
from fcd_deck import *
from fcd_display import *
from fcd_cpu import *
from fcd_economy import *

def play_fcd():
    status = input("Press Enter to start")
    p1money = p2money = 500
    while status.lower() != "q" and status.lower() != "quit":

        #begin round
        p1, p2, curr_deck = initiate_round()
        pot = 0
        p1money, p2money, pot = ante(p1money, p2money, pot)
        print()

        #display cards, collect wagers
        for i in range(1,6):
            print(" " * 7, f"({i})", " " * 7, end = "")
        print("\n" + show_hand(p1))
        valid_wager = False
        while valid_wager == False:
            print("\nHow much would you like to wager?\nYou can wager up to", "$" + str(min(p1money, p2money)))
            wager = input("$")
            valid_wager = is_valid_wager(wager, p1money, p2money)
        wager = int(wager)
        p1money, p2money, pot = wager_update(wager, p1money, p2money, pot)

        #card selection
        print("\nSelect which cards to keep:")
        choice = input()
        keep = set()
        for i in range(1,6):
            if str(i) in choice:
                keep.add(i - 1)
        new_hand = []
        for i in keep:
            new_hand.append(p1[i])

        #draw new cards
        p1 = new_hand
        p1count = 5 - len(p1)
        if p1count > 0:
            p1draw, curr_deck = draw(p1count, curr_deck)
            p1 += p1draw
        p2choice = cpu_choice(p2)
        p2count = 5 - len(p2)
        if p2count > 0:
            p2draw, curr_deck = draw(p2count, curr_deck)

        #second betting
        print("\n" + show_hand(p1))
        valid_wager = False
        while valid_wager == False:
            print("\nHow much would you like to wager?\nYou can wager up to", "$" + str(min(p1money, p2money)), "\n")
            wager = input()
            valid_wager = is_valid_wager(wager, p1money, p2money)
        wager = int(wager)
        p1money, p2money, pot = wager_update(wager, p1money, p2money, pot)

        #scoring
        if score(p1) > score(p2):
            print("\nYou won :)")
            p1money += pot
        elif score(p1) < score(p2):
            print("\nYou lost :(")
            p2money += pot
        else:
            print("\nYou tied :|")
            p1money += pot // 2
            p2money += pot // 2

        #display score
        print("\nYour hand:")
        print(show_hand(p1))
        print(show_score(p1))
        print("\n CPU's hand:")
        print(show_hand(p2))
        print(show_score(p2))
        print("\nYour score:", p1money, "CPU score:", p2money)

        #economy check
        if min(p1money, p2money) == 0:
            if p1money == 0:
                print("\nGame over: You're out of money :( Would you like to play again? y/n")
                keep_playing = input()
            else:
                print("\nCPU ran out of money! You won :) Would you like to play again? y/n")
                keep_playing = input()
            if keep_playing.lower() == "y" or keep_playing.lower() == "yes":
                p1money = 500
                p2money = 500
                continue
            else:
                return 0

        #continue
        status = input("\nPress Enter to continue, or q to quit\n")
if __name__ == "__main__":
    play_fcd()
