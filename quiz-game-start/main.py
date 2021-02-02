from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# print(question_data[0]['text'])

question_bank = []

for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))

quiz = QuizBrain(question_bank)


while quiz.still_have_question():
    quiz.next_question()
print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{len(quiz.question_list)}")









