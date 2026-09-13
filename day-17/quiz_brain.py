class QuizBrain:
    def __init__(self, question_list):
        self.question_number: int = 0
        self.question_list: list = question_list
        self.score: int = 0

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.strip().lower() == correct_answer.lower():
            print("You got it correct")
            self.score += 1
        else:
            print("Nope!")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print() ## print("\n") would add two lines. Every print() call automatically appends its own newline character at the end (that's the default end="\n" parameter)
