# step 2: Import data list and question model

from question_model import Question 
from data import question_data 

from quiz_brain import QuizBrain


# step 3: create a question bank using the question_data that has been imported 

# 3a. Place to store our questions

question_bank = []

# 3b. loop thru question_data

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]

    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz", f"Your final score was: {quiz.score}/{quiz.question_number}")   