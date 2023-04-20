import os
from Question import Question

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
            print(f"\n\nYour score is {score}")
            print("\n\nWelcome to level 2!")
            print("________________________")
            you_win = True
        elif score < 3:
            print(f"\nYour score = {score}")
            print(f"\nWrong answer: {wrong_answer}")

    # #returnera om funktionen har gått bra eller dåligt
    return you_win, score


# #level 2 in game
def run_test_2():
    secret_number = int("8")
    guess = ""
    guess_count = 0
    guess_limit = 10
    # lose_test_2 = 0
    out_of_guesses = False
    you_win = False
    print("\nLEVEL 2!")

    while guess != secret_number and not (out_of_guesses):
        try:
            if guess_count < guess_limit:
                print("\nCan you guess the right number between 0-15? ")
                guess = int(input("enter guess: "))
                guess_count += 1
            else:
                out_of_guesses = True
        except ValueError:
            print("\nInvalid number, must be a number 0-15")

    if out_of_guesses:
        # lose_test_2 += 1
        print("\nYOU LOSE!")
        print("\nTry again....")
        print("________________________")
        run_test_2()
    else:
        you_win = True
        os.system('clear')
        print("\nCorrect!")
        print(f"\nyou guessed {guess_count} times")
        # print(lose_test_2)
        print("\nWelcome to level 3!")
        print("________________________")
        print()

    return you_win, guess_count
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
    loop thrue the questions in level3

    """
    print("\nLEVEL 3!")
    print()
    score = 0
    for question in level3:
        answer = input(question.prompt)
        if answer == question.answer:
            score = score + 1
            os.system('clear')
    print("\nYou got " + str(score) + "/" + str(len(level3)) + " Correct in level 3")

    return score


def play_game():
    you_win_level_1 = False
    you_win_level_2 = False
    score = 0
    total_number_of_failures = 0
    number_of_failures_level_1 = 0
    number_of_failures_level_2 = 0
    number_of_failures_level_3 = 0

    while not you_win_level_1:
        # Call the function level_one
        # Return the value of you_win
        # If you win the loop breaks
        # Or else a new try on level 1
        you_win_level_1, score = level_one(level_1_questions)
        if you_win_level_1:
            break
        else:
            number_of_failures_level_1 = number_of_failures_level_1 + 1
            print("\nyou need to answer all questions correctly to move to next level")
            print("\ntry again")

    while not you_win_level_2:
        # Call the function run_test_2
        # Return the value of you_win
        # If you win the loop breaks
        # Or else a new try on level 1
        you_win_level_2, guess_count = run_test_2()
        if you_win_level_1:
            break
        else:
            number_of_failures_level_2 = number_of_failures_level_2 + 1
            
        
    # while not you_win_level_2:
    #     # anropa funktion level 1 som retunerar ett värde om
    #     # funktionen har gått bra eller dåligt
    #     # har den gått bra avbryts while loopen
    #     # annars nytt försök på level 1
    #     you_win_level_2, guesses_level_2 = run_test_2()
    #     number_of_failures_level_2 = number_of_failures_level_2 + 1
    #     total_number_of_failures = total_number_of_failures + 1
    #     if you_win_level_2:
    #         break

    # guesses_level_2 = run_test_2()
    run_test_3(level3)

    os.system('clear')


    print("\nThank you for playing, here is your result:")
    print(f"\nnumber of failed attempts level 1: {number_of_failures_level_1}")
    print(f"\nnumber of failed attempts level 2: {number_of_failures_level_2}")
    print(f"\nnumber of wrong answer level 3: {number_of_failures_level_3}")
    
    print(score)


play_game()
