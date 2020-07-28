from random import choice


def get_word():
    return choice(word_list)


words = open("words.txt", "r")
word_list = []

for word in words:
    word_list.append(word.strip())

