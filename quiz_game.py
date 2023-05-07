print("Welcome to my computer quiz!")

playing = input("Do you want to play? (yes/no) ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

questions = [
    Question("What does CPU stand for?", "central processing unit"),
    Question("What does GPU stand for?", "graphics processing unit"),
    Question("What does RAM stand for?", "random access memory"),
    Question("What does PSU stand for?", "power supply")
]

# play the game
score = 0
question_count = len(questions)
for question in questions:
    answer = input(f"{question.text} ")
    if answer.lower() == question.answer:
        print("Correct!")
        score += 1
    else:
        print(f"I'm sorry, that answer isn't correct...  The correct answer is '{question.answer}'")

print(f"Your score is {score} out of a potential {question_count}.")
print(f"That's {(score/question_count)*100}%.")