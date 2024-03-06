from art import logo
import random
from replit import clear

def deal_card():
    return random.choice(cards)

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
