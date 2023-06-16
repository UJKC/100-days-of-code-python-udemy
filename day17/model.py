import data
from model_question import question_initial_data
from brain_of_quiz import Quiz_Brain

question_bank = []
for question in data.question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = question_initial_data(question_text, question_answer)
    question_bank.append(new_question)

quiz = Quiz_Brain(question_bank)
while quiz.stillhasquestions():
    quiz.next_question1()
print("You have completed the quiz")
print(f"You score is {quiz.score}/{len(question_bank)}")