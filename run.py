
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
