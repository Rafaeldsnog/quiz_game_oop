class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        print(f"SCORE: {self.score} / {self.question_number - 1 }")
        choice = input(f"Q.{self.question_number}: {current_question.question} ? (TRUE or FALSE) => ")
        self.check_answer(choice, current_question.answer)

    def check_answer(self, choice, answer):
        if choice.lower() == answer.lower():
            self.score +=1
            print("You got it right!")
        else:
            print("You got it wrong.")

    def final_result(self):
        print("Thanks for playing!")
        print(f"Your final score is: {self.score} / {len(self.question_list)}")


