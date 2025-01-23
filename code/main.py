import random
from art import asciiart  

def create_deck():
    """Creates and returns a deck of cards."""
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append({"rank": rank, "suit": suit})
    return deck

def shuffle_deck(deck):
    """Shuffles the deck."""
    random.shuffle(deck)

def calculate_hand_value(hand):
    """Calculates the value of a hand."""
    value = 0
    aces = 0
    for card in hand:
        if card["rank"] in ["J", "Q", "K"]:
            value += 10
        elif card["rank"] == "A":
            value += 11
            aces += 1
        else:
            value += int(card["rank"])

    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value

def display_hand(player, hand):
    """Displays the player's hand."""
    print(f"{player}'s hand:")
    for card in hand:
        print(f"{card['rank']} of {card['suit']}")
    print(f"Total value: {calculate_hand_value(hand)}\n")

def play_game():
    """Main function for the Blackjack game."""

    print(asciiart)  
    while True:
        deck = create_deck()
        shuffle_deck(deck)

        player_hand = [deck[0], deck[1]]
        dealer_hand = [deck[2], deck[3]]

        print("Welcome to Blackjack!\n")

        while True:
            display_hand("Player", player_hand)
            if calculate_hand_value(player_hand) > 21:
                print("You busted! Dealer wins!")
                break

            choice = input("Do you want to (h)it or (s)tand? ").lower()
            if choice == 'h':
                player_hand.append(deck[len(player_hand) + len(dealer_hand)])
            elif choice == 's':
                break
            else:
                print("Invalid choice. Please enter 'h' or 's'.")

        if calculate_hand_value(player_hand) <= 21:
            print("Dealer's turn:\n")
            while calculate_hand_value(dealer_hand) < 17:
                dealer_hand.append(deck[len(player_hand) + len(dealer_hand)])
                display_hand("Dealer", dealer_hand)

        player_value = calculate_hand_value(player_hand)
        dealer_value = calculate_hand_value(dealer_hand)

        display_hand("Player", player_hand)
        display_hand("Dealer", dealer_hand)

        if dealer_value > 21 or player_value > dealer_value:
            print("Congratulations! You win!")
        elif player_value == dealer_value:
            print("It's a tie!")
        else:
            print("Dealer wins! Better luck next time!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\n" * 20)
            print("Thank you for playing!")
            break

play_game()
