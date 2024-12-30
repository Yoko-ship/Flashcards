from collections import Counter

class Hangman:
    def play(self,word,hint):
        print("Ваша задача угадать слово с помощью подсказки которая на русском \n Вы должны ответить на английском")
        running = True
        answer = []
        true_answer = []
        tries = 10
        for size in range(1,len(word) +1):
            true_answer.append("_")
        while running:
            print(f" Попытки: {tries}")
            print(f"Подсказка: {hint}")
            if tries == 0:
                print("У вас закончились попытки")
                running = False
            texted = "".join(answer)
            print(true_answer)
            if Counter(texted) == Counter(word):
                print(f"вы успешно угадали слово {word}")
                running = False


            else:
                user_input = input("Введите букву: ")
                if user_input in word:
                        print(f"Вы угадали букву: {user_input}")
                        answer.append(user_input)
                        indexOfStr = word.index(user_input)
                        true_answer.pop(indexOfStr)
                        true_answer.insert(indexOfStr,user_input)
                else:
                    tries -= 1

