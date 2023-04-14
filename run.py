
score = 0
wrong_answer = 0

print("Welcome to this game!")

name = input("\nEnter your name: ")
print(f"\nHello {name}")

play = input("\nDo you like to play, yes or no?")

if play == "yes":
    print("\nLet's do this!")
    print("________________________")
elif play == "no":
    print("Goodbye..")
else:
    print("invalid choice, try again!") 

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


print(f"Your score = {score}")
print(f"Wrong answer: {wrong_answer}")
