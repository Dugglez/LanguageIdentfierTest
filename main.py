import os
import random
from googletrans import Translator


def main():
    sentences = []
    languages = ['en', 'ar', 'zh-cn', 'nl', 'fr', 'de', 'el', 'he', 'it', 'ga', 'ja', 'pl', 'ru',
                 'sr', 'es', 'vi', 'tr', 'sv']
    language_longform = ['English', 'Arabic', 'Chinese (simplified)', 'Dutch', 'French', 'German', 'Greek',
                         'Hebrew', 'Italian', 'Irish', 'Japanese', 'Polish', 'Russian', 'Serbian', 'Spanish',
                         'Vietnamese', 'Turkish', 'Swedish']
    print("Welcome to the Language Identifier Test. Sentences will be shown to you, and your job")
    print("is to identify the language used in the sentences. Please select a difficulty:")
    print("Easy: 3 language options to choose from, or Hard: 5 language options to choose from.")
    print("Type 1 for Easy or 2 for Hard.")
    game_mode = input("")
    while game_mode not in ["1", "2"]:
        print("Type 1 for Easy or 2 for Hard.")
        game_mode = input("")
    # pick a bunch of random sentences then run them through google translate.
    with open("sentences.txt", "r") as file:
        for line in file:
            sentences.append(line)
    round_number = 1
    score = 0
    translator = Translator()
    print("How many rounds would you like to play? (max 10)")
    game_length = input("")
    while game_length not in ["1", "2", "3", "4" , "5", "6", "7", "8", "9", "10"]:
        print("Type a number between 1 and 10.")
        game_length = input("")
    game_length_int = int(game_length)
    for i in range(game_length_int):
        os.system("cls")
        print(f"This is round number {round_number}. Your score is {score}/{round_number-1}. Here is the next sentence.")
        rand_sentence = random.choice(sentences)
        rand_language = random.choice(languages)
        translated_sentence = translator.translate(rand_sentence, dest=rand_language, src='en')
        print(translated_sentence.text)
        randwrong1 = random.choice(languages)
        randwrong2 = random.choice(languages)
        randwrong3 = random.choice(languages)
        randwrong4 = random.choice(languages)
        while languages.index(randwrong1) == languages.index(rand_language):
            randwrong1 = random.choice(languages)
        while languages.index(randwrong2) == languages.index(rand_language) or languages.index(randwrong2) == languages.index(randwrong1):
            randwrong2 = random.choice(languages)
        while languages.index(randwrong3) == languages.index(rand_language) or languages.index(randwrong3) == languages.index(randwrong1) or languages.index(randwrong3) == languages.index(randwrong2):
            randwrong3 = random.choice(languages)
        while languages.index(randwrong4) == languages.index(rand_language) or languages.index(randwrong4) == languages.index(randwrong1) or languages.index(randwrong4) == languages.index(randwrong2) or languages.index(randwrong4) == languages.index(randwrong3):
            randwrong4 = random.choice(languages)
        if game_mode == "1":
            answers = [rand_language, randwrong1, randwrong2]
            random.shuffle(answers)
            print(f"Is this sentence in (1): {language_longform[languages.index(answers[0])]},"
                  f" (2): {language_longform[languages.index(answers[1])]}"
                  f" or (3): {language_longform[languages.index(answers[2])]}?")
            print("Use the numbers in the brackets to make your choice.")
            choice = input("")
            while choice not in ["1", "2", "3"]:
                print("Make a valid choice")
                choice = input("")
            int_choice = int(choice)
            if languages.index(answers[int_choice-1]) == languages.index(rand_language):
                score += 1
                print(f"Correct! The language was {language_longform[languages.index(rand_language)]}. "
                      f"Your score is now {score}.")
                input("Press enter to continue.")
            else:
                print(f"Incorrect. The language was {language_longform[languages.index(rand_language)]}.")
                input("Press enter to continue.")
        if game_mode == "2":
            answers = [rand_language, randwrong1, randwrong2, randwrong3, randwrong4]
            random.shuffle(answers)
            print(f"Is this sentence in (1): {language_longform[languages.index(answers[0])]}, "
                  f"(2): {language_longform[languages.index(answers[1])]}, "
                  f"(3): {language_longform[languages.index(answers[2])]}, "
                  f"(4): {language_longform[languages.index(answers[3])]} or "
                  f"(5): {language_longform[languages.index(answers[4])]}?")
            print("Use the numbers in the brackets to make your choice.")
            choice = input("")
            while choice not in ["1", "2", "3", "4", "5"]:
                print("Make a valid choice")
                choice = input("")
            int_choice = int(choice)
            if languages.index(answers[int_choice-1]) == languages.index(rand_language):
                score += 1
                print(f"Correct! The language was {language_longform[languages.index(rand_language)]}. Your score is now {score}.")
                input("Press enter to continue.")
            else:
                print(f"Incorrect. The language was {language_longform[languages.index(rand_language)]}.")
                input("Press enter to continue.")
        round_number += 1
    print(f"The game is over. You scored {score}/{game_length_int}.")
    input("Press enter to exit.")


if __name__ == '__main__':
    main()
