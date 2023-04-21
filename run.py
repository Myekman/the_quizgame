import gspread
from google.oauth2.service_account import Credentials

import os
from Question import Question

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('the_quizgame')

result = SHEET.worksheet('result')

final_result = []

print("Welcome to this game!")

name = input("\nEnter your name: ")
print(f"\nHello {name}!")

while True:
    play = input("\nDo you like to play? please type yes or no: ")

    if play == "yes":
        print("\nLet's do this!")
        print("________________________")
        print("\nLEVEL 1!")
        break
    elif play == "no":
        print("Goodbye..")
        exit()
    else:
        print("\nInvalid choice, try again!")


level_1_questions = [
  {
    'question': "\nA square has ___ sides?",
    'answer': '4'
  },
  {
    'question': "\nA triangle has ___ sides?",
    'answer': '3'
  },
  {
    'question': "\nA circle has ___ sides?",
    'answer': '0'
  }
]


# #level 1 in game
def level_one(level_1_questions):
    """
    get questions from level_1_questions and repeat until 3 points are achieved
    return the value of you_win to play_game() where this function is called
    """
    score = 0
    wrong_answer = 0
    you_win = False

    for question in level_1_questions:
        show_question = question.get("question")
        print(show_question)

        user_answer = input("Enter answer: ")

        correct_answer = question.get("answer")

        if user_answer == correct_answer:
            score = score + 1
            print("\nCorrect!")
        elif user_answer != correct_answer:
            wrong_answer = wrong_answer + 1
            print(f"\nIncorrect.. The right answer was: {correct_answer}")

        if score == 3:
            os.system('clear')
            print("well done, you're on to the next level!")
            print("\n\nWelcome to level 2!")
            print("\nCan you guess the right number between 0-15? ")
            print("you have 3 tries")
            print("________________________")
            you_win = True
        elif score < 3:
            print(f"\nYour score = {score}")
            print(f"\nWrong answer: {wrong_answer}")

    # #return if the game has been won or lost
    return you_win


# level 2 in game
def run_test_2():
    """
    Continue to guess a number until secret_number is guessed
    For every time you have guessed wrong three times, 
    you lose and get another try
    Return the value of you_win to play_game() where this function is called 
    """
    secret_number = int("8")
    guess = ""
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False
    you_win = False
    print("\nLEVEL 2!")

    while guess != secret_number and not (out_of_guesses):
        try:
            if guess_count < guess_limit:
                guess = int(input("enter guess: "))
                guess_count += 1  
            else:
                out_of_guesses = True
        except ValueError:
            print("\nInvalid number, must be a number 0-15")

    if out_of_guesses:
        print("\nYOU LOSE!")
        print("\nTry again....")
        print("________________________")
    else:
        you_win = True
        print("\nCorrect!")
        os.system('clear')
        print("\nWelcome to level 3!")
        print("________________________")
        print()

    return you_win


# #level 3 in game
question_prompts = [
  "Adding the numbers between 1 to 100 consecutively (1+2+3+4+…) gives you " +
  "what final answer?\n(a) 5050\n(b) 3050\n(c) 10010\n\n",
  "What is the value of Pi to four individual" +
  "decimal places?\n(a) 3.1418\n(b) 3.1426\n(c) 3.1416\n\n",
  "How many hours are there in a year (rounded to the nearest hour)?" +
  "\n(a) 9000 hours\n(b) 8760 hours\n(c) 12200 hours\n\n",
]


level3 = [
  Question(question_prompts[0], "a"),
  Question(question_prompts[1], "c"),
  Question(question_prompts[2], "b"),
]


def run_test_3(level3):
    """
    loop thrue the questions in level3 list

    """
    print("\nLEVEL 3!")
    print()
    score = 0
    for question in level3:
        answer = input(question.prompt)
        if answer == question.answer:
            score = score + 1
        else:    
            os.system('clear')

    return score


def update_worksheet(data):
    global final_result
    print("final_results", final_result)
    
    print("Updating worksheet")
    worksheet_to_update = SHEET.worksheet('result')
    worksheet_to_update.append_row(data)
    print("Result updated successfully")


def play_game():
    """
    Call all 3 levels 
    If you_win level 1 break, else try again and count number of failed tries
    If you_win level 2 break, else try again and count number of failed tries
    """
    global final_result
    you_win_level_1 = False
    you_win_level_2 = False
    you_win_level_2 = False
    number_of_failures_level_1 = 0
    number_of_failures_level_2 = 0
    # final_result = []

    while not you_win_level_1:
        # Call the function level_one
        # Return the value of you_win
        # If you win the loop breaks
        # Or else a new try on level 1
        you_win_level_1 = level_one(level_1_questions)
        if you_win_level_1:
            final_result.append(number_of_failures_level_1)
            break
        else:
            number_of_failures_level_1 = number_of_failures_level_1 + 1
            print("\nyou need to answer all questions" +
            "correctly to move to next level")
            print("\ntry again")

    while not you_win_level_2:
        # Call the function run_test_2
        # Return the value of you_win
        # If you win the loop breaks
        # Or else a new try on level 1
        you_win_level_2 = run_test_2()
        if you_win_level_2:
            final_result.append(number_of_failures_level_2)
            break
        else:
            number_of_failures_level_2 = number_of_failures_level_2 + 1

    score_result = run_test_3(level3)
    final_result.append(score_result)


    print("\nThank you for playing, here is your result:")
    print(f"\nnumber of failed attempts level 1: {number_of_failures_level_1}")
    print(f"\nnumber of failed attempts level 2: {number_of_failures_level_2}")
    print("\nYou got " + str(score_result) + "/" + str(len(level3)) +
    " Correct in level 3")

    data = result.get_all_values()
    print("data", data)

    # print("final_results", final_result)
    update_worksheet(final_result)


play_game()
