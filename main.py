from word_bank import get_word
import display

def init_guessed_letters(length):
    guessed_letters = []
    for index in range(0,length):
        guessed_letters.append(False)
    return guessed_letters

# def check_guess(guessed_letters, guess, answer):
#     if guess in answer:
#         update_guessed_letters(guessed_letters, answer, guess)
        
def check_for_win(guessed_letters):
    return False not in guessed_letters

def update_guessed_letters(guessed_letters, answer, guess):
    for index, letter in enumerate(guessed_letters):
        if guess == answer[index]:
            guessed_letters[index] = True
        

remaining_attempts = 7
game_over = False
game_won = False
remaining_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
answer = get_word()
guessed_letters = init_guessed_letters(len(answer))

display.display_greeting()

while not game_over:
    guess = display.prompt_guess(remaining_letters, guessed_letters, answer)
    if guess not in remaining_letters:
        print("You already guessed that! Pick another letter")
        # print(f"You have {remaining_attempts} attempts left")
    else:
        remaining_letters.remove(guess)
        if guess not in answer:
            remaining_attempts -= 1
            if remaining_attempts <= 0:
                game_over = True
        else:
            update_guessed_letters(guessed_letters, answer, guess)
            if check_for_win(guessed_letters):
                game_over = True
                game_won = True
    # elif guess not in remaining_letters and guess not in answer:
    #     print(f"You have {remaining_attempts} attempts left")
    # else:
    #     remaining_attempts -= 1
    #     if remaining_attempts <= 0:
    #         game_over = True
    if not game_won:
        display.display_hang_man(remaining_attempts)

        
display.end_game(game_won, answer) 







