import os

def display_greeting():
    os.system("clear")
    print("==============================================")
    print("WELCOME!! LETS PLAY HANGMAN AND GUESS THE WORD")
    print("==============================================")

def display_word(answer, guessed_letters_index):
    display_string = ""
    for index, guessed in enumerate(guessed_letters_index):
        if guessed :
            display_string += answer[index] + " "
        else:
            display_string +="_ "
    print(display_string)

def show_remaining_letters(remaining_letters):
    print ("Remaining letters:")
    print(*remaining_letters, sep= " ")

def prompt_guess(remaining_letters, guessed_letters_index, answer):
    print("\n\n\n")
    display_word(answer, guessed_letters_index)
    print("\n")
    show_remaining_letters(remaining_letters)
    return input("\nTYPE A LETTER AND PRESS ENTER>> ").strip().lower()

def end_game(status, answer):
    os.system("clear")
    if status:
        answer_str = ""
        for letter in answer:
            answer_str += letter + " "

        print(f"\n\n{answer_str}\n\nVictory")
    else:
        print(f"You lost!!! The answer was {answer.upper()}")

def display_hang_man(attempts_remaining):
    hangman_drawings = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    os.system("clear")
    hangman_index = 6 - attempts_remaining
    print(f"You have {attempts_remaining} attempts left")
    if hangman_index >= 0:
        print(hangman_drawings[hangman_index])
