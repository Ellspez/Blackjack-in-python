import random
import time

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

def get_card_value(card):
    if card in ["Jack", "Queen", "King"]:
        return 10
    elif card == "Ace":
        return 11
    else:
        return int(card)

def calculate_total(hand):
    total = sum(get_card_value(card) for card in hand)
    aces = hand.count("Ace")
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

wallet = 500
playing = True

print("==================================")
print("     WELCOME TO PYTHON CASINO     ")
print(f"      Starting Balance: ${wallet}     ")
print("==================================")

while playing:
    if wallet <= 0:
        print("\nYou are completely out of money! The casino kicked you out. 😭")
        break

    player_hand = [random.choice(cards), random.choice(cards)]
    dealer_hand = [random.choice(cards), random.choice(cards)]

    print(f"\nYour current balance: ${wallet}")
    while True:
        try:
            bet = int(input("How much do you want to bet? $"))
            if bet <= 0:
                print("You must bet at least $1!")
            elif bet > wallet:
                print(f"You don't have enough money! You only have ${wallet}.")
            else:
                break
        except ValueError:
            print("Please enter a valid whole number.")

    print("------------------------------")
    print(f"Your cards: {', '.join(player_hand)} (Total: {calculate_total(player_hand)})")
    print(f"Dealer's face-up card: {dealer_hand[0]}")
    print("------------------------------")
    time.sleep(1)

    player_bust = False
    while calculate_total(player_hand) < 21:
        choice = input("Do you want to (h)it or (s)tand? ").lower()
        if choice == 'h':
            new_card = random.choice(cards)
            player_hand.append(new_card)
            print(f"You drew a {new_card}. Total: {calculate_total(player_hand)}")
            if calculate_total(player_hand) > 21:
                print("You went over 21! Bust! :( ")
                player_bust = True
                break
        elif choice == 's':
            break
        time.sleep(0.5)

    player_total = calculate_total(player_hand)

    if not player_bust:
        print("\n--- Dealer's Turn ---")
        print(f"Dealer reveals full hand: {', '.join(dealer_hand)}")
        print(f"Dealer's total: {calculate_total(dealer_hand)}")
        time.sleep(1.5)

        while calculate_total(dealer_hand) < 17:
            new_card = random.choice(cards)
            dealer_hand.append(new_card)
            print(f"Dealer hits and draws a {new_card}. Total: {calculate_total(dealer_hand)}")
            time.sleep(1.5)

    dealer_total = calculate_total(dealer_hand)
    print("------------------------------")

    if player_bust:
        wallet -= bet
        print(f"You lost your ${bet}. Balance: ${wallet}")
    elif dealer_total > 21:
        wallet += bet
        print("----WINNER----")
        print(f"Dealer busted! You won: ${bet} | New Balance: ${wallet}")
    elif player_total == 21 and len(player_hand) == 2 and not (dealer_total == 21 and len(dealer_hand) == 2):
        blackjack_profit = int(bet * 1.5)
        wallet += blackjack_profit
        print("----NATURAL BLACKJACK----")
        print(f"You won: ${blackjack_profit} | New Balance: ${wallet}")
    elif player_total > dealer_total:
        wallet += bet
        print("----WINNER----")
        print(f"You beat the dealer! You won: ${bet} | New Balance: ${wallet}")
    elif dealer_total > player_total:
        wallet -= bet
        print(f"Dealer wins with {dealer_total}. You lost your ${bet}. Balance: ${wallet}")
    else:
        print(f"It's a push (Tie)! Both had {player_total}. Your ${bet} bet was returned. Balance: ${wallet}")

    print("------------------------------")
    time.sleep(1)
    
    again = input("Do you want to play another hand? (y/n): ")
    if again.lower() != 'y':
        playing = False
        print(f"\nYou walked away from the table with: ${wallet}")
        print("Thanks for playing!")
