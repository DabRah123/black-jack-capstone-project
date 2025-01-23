# black-jack-capstone-project
**Blackjack Game 🃏**
Welcome to the Blackjack Game, a fun and interactive command-line implementation of the classic card game!

**Features**
Fully functional Blackjack game with dealer logic.
Randomly shuffled deck for every game.
Automatic hand value calculation, including proper handling of Aces.
ASCII art for added style.

**How to Play**
Run the script to start the game.
You’ll be dealt two cards, and the dealer will also get two cards (one face-down).
Choose whether to:
Hit (draw another card)
Stand (end your turn)
Your goal is to have a hand value closer to 21 than the dealer without exceeding 21.
If your hand value exceeds 21, you lose (bust).
The dealer must draw cards until their hand value is 17 or higher.

**Game Rules**
Number cards (2-10) are worth their face value.
Face cards (J, Q, K) are worth 10.
Aces can be worth 1 or 11, depending on the hand’s total value.
Requirements
Python 3.6 or higher
Standard Python libraries (no external dependencies)

**Algorithm for the Blackjack Game**

Initialize the Game:

Create a deck of cards with all ranks and suits.
Shuffle the deck randomly.
Deal Initial Cards:

Deal two cards each to the player and the dealer.
Display the player's cards and the total value.
Show only one of the dealer's cards (the other remains face-down).
Player's Turn:

Prompt the player to choose between:
Hit: Add a card to the player's hand.
Stand: End the player's turn.
If the player's total hand value exceeds 21, they bust and lose the game.
Continue the player's turn until they choose to stand or bust.
Dealer's Turn (if the player hasn’t busted):

Reveal the dealer's hidden card.
The dealer must draw cards until their hand value reaches at least 17.
Display the dealer's hand and total value after each draw.
Compare Hands:

Calculate the total value of the player's and dealer's hands.
Determine the winner based on these rules:
If the dealer busts, the player wins.
If the player's hand value is higher than the dealer's, the player wins.
If the player's hand value is equal to the dealer's, it's a tie.
Otherwise, the dealer wins.
End of Game:

Ask the player if they want to play again:
Yes: Restart the game from step 1 with a new deck.
No: Exit the game and thank the player.
Exit:

Clear the screen and display a goodbye message.
