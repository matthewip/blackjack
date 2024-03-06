############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run
from art import logo
import random
from replit import clear

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.


def deal_card():
    return random.choice(cards)


#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().


#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.
def calculate_score(list_of_cards):
    if list_of_cards == [11, 10] or list_of_cards == [10, 11
                                                      ]:  # check for blackjack
        return 0
    else:
        score = sum(list_of_cards)
        if 11 in list_of_cards:
            if score > 21:
                list_of_cards.remove(11)
                list_of_cards.append(1)
                score -= 10
        return sum(list_of_cards)


def compare(score_for_user, score_for_computer):
    if score_for_user == score_for_computer:
        return "Draw."
    elif score_for_computer == 0:
        return "You lose. Computer got blackjack."
    elif score_for_user == 0:
        return "You win. You got blackjack!"
    elif score_for_user > 21:
        return "You lose. You went over."
    elif score_for_computer > 21:
        return "You win. Computer went over."
    else:
        user_wins = score_for_user > score_for_computer
        if user_wins:
            return "You win. You are closer to 21 than the computer!"
        else:
            return "You lose. Computer is closer to 21 than you!"


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def play():

    user_cards = []
    computer_cards = []

    for _ in range(0, 2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    user_play_blackjack = True

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    if computer_score == 0:
        user_play_blackjack = False

    while user_play_blackjack:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        if user_score == 0 or computer_score == 0 or user_score > 21:  # user gets blackjack or computer gets  blackjack or user goes over
            # game ends
            user_play_blackjack = False
        else:
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")
            user_draws_another_card = True if input(
                "Type 'y' to get another card, type 'n' to pass: "
            ) == "y" else False
            if user_draws_another_card:
                user_cards.append(deal_card())
            else:
                # game ends
                user_play_blackjack = False

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"Computer's final hand: {computer_cards}, final score: {computer_score}"
    )

    blackjack_final_result = compare(score_for_user=user_score,
                                     score_for_computer=computer_score)
    print(blackjack_final_result)

    user_wants_to_restart_blackjack = True if input(
        "Do you want to restart the game? Type 'y' for yes, otherwise type 'n'.: "
    ) == 'y' else False
    if user_wants_to_restart_blackjack:
        clear()
        play()


user_wants_to_play_blackjack = True if input(
    "Do you want to play a game of blackjack? Type 'y' for yes, otherwise type 'n'.: "
) == "y" else False
if user_wants_to_play_blackjack:
    clear()
    print(logo)
    play()

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
