import json
import random
from Models.AnswerModel import AnswerModel
from Models.QuestionModel import QuestionModel
from Models.CategoryModel import CategoryModel


class RandomQuestionQuiz:
    def get_all_questions_from_json(self):

        categoryyy = []

        with open('questions.json', 'r', encoding="utf-8") as file:
            data = json.load(file)

            for category in data['categories']:
                question = category['question']
                id = category['id']
                answer_list = []
                for answer in category["answers"]:
                    answer_list.append(AnswerModel(answer['option'], answer['text'], answer['correct']))

                    quest = QuestionModel(id, question, answer_list)

                categoryyy.append(CategoryModel(category['categoryName'], quest))

        return categoryyy

    def play_quiz(self):

        all_questions = self.get_all_questions_from_json()
        points = 0

        while all_questions:
            random_category = random.choice(all_questions)

            question = random_category.question

            print(question.question)
            for i in range(len(question.answer_list)):
                print(question.answer_list[i], end='')

            while True:
                user_answer = input("Wybierz poprawną odpowiedź (wpisz literę): ").strip().lower()

                for answer in question.answer_list:
                    if answer.option == user_answer:
                        if answer.correctness:
                            points += 1
                            print("Poprawna odpowiedź")
                        else:
                            print("Niepoprawna odpowiedź.")
                        break  # Zakończ pętlę for, gdy znajdziemy dopasowanie
                else:
                    print("Taka odpowiedz nie istnieje")
                    continue
                break
            all_questions.remove(random_category)

        print(f"Liczba punktów: {points}")

    def get_categories(self):
        all_questions = self.get_all_questions_from_json()

        unique_elements = set()

        for question in all_questions:
            unique_elements.add(question.categoryName)

        print(unique_elements)
