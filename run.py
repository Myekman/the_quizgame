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


#level 1 in game
questions = [
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

def level_one(questions):
  score = 0
  wrong_answer = 0
  you_win = False
  
  for question in questions:
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
      print("Good job, you got the highest score!")
      print("\n\nWelcome to level 2!")
      print("________________________")
      you_win = True
    elif score < 3:
      print(f"\nYour score = {score}")
      print(f"\nWrong answer: {wrong_answer}")

  while you_win == False:
    print("\nyou need ... to move to next level")
    print("\ntry again")
    level_one(questions)
    if you_win:
      break


#level 2
def run_test_2():
    secret_number = int("8")
    guess = ""
    guess_count = 0
    guess_limit = 10
    out_of_guesses = False
    print("\nLEVEL 2!")

    while guess != secret_number and not(out_of_guesses):
      if guess_count < guess_limit:
        print("\nCan you guess the right number between 0-15? ")
        guess = int(input("enter guess: "))
        guess_count += 1
      else:
        out_of_guesses = True

    if out_of_guesses:
      print("\nYOU LOSE!")
      print("\nTry again....")
      print("________________________")
      run_test_2()
    else:
      print("\nCorrect!")
      print("Welcome to level 3!")
      print("________________________")
      print()
  

# #level 3 in game

question_prompts = [
  "What color are apples?\n(a) Red\n(b) Purple\n(c) Orange\n\n",
  "What color are oranges?\n(a) Red\n(b) Yellow\n(c) Orange\n\n",
  "What color are bananas?\n(a) Red\n(b) Yellow\n(c) Orange\n\n",
]

level3 = [
  Question(question_prompts[0], "a"),
  Question(question_prompts[1], "c"),
  Question(question_prompts[2], "b"),
]

def run_test_3(level3):
  print("LEVEL 3!")
  print()
  
  score = 0
  for question in level3:
    answer = input(question.prompt)
    if answer == question.answer:
      score = score + 1
  print("You got " + str(score) + "/" + str(len(level3)) + " Correct")


level_one(questions)
run_test_2()
run_test_3(level3)