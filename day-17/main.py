from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

def question_bank_generator() -> list[Question]:
    question_list: list[Question] = []
    for question in question_data:
        question_list.append(Question(question["question"], question["correct_answer"]))
    return question_list

if __name__ == "__main__":
    quiz = QuizBrain(question_bank_generator())
    while quiz.still_has_questions():
        quiz.next_question()
    else:
        print("You have completed the quiz n stuff")
        print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}")
