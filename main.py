from question_model import Question
from data import question_data
from quiz_brain import Quiz_brain

question_list = []

for one_question in question_data:
    question_t = one_question["question"]
    question_a = one_question["correct_answer"]
    new_question = Question(question_t, question_a)
    question_list.append(new_question)


quiz = Quiz_brain(question_list)
while quiz.has_questions() == True:
    quiz.next_question()
print("Dokončili jste kvíz")
print(f"Vaše celkové skóre je: {quiz.score} / {quiz.question_number}")