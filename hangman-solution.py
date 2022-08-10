import random

word_list = ["grape", "pear", "apple", "banana", "berries"]

class Hangman():
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = list('-'*len(self.word))
        self.num_letters = len(set(self.word))

def check_letter(self, letter) ->None:
    letter = input("pick a letter").lower()
    self.letter = letter
    pass
    for index, letter in enumerate(self.word):
        if letter in self.word:
            print(str.replace('_', letter))
        elif letter in self.word:
            print((self.num_letter)-1)
        elif letter not in self.word:
            print((self.num_lives) -1)

def ask_letter(self):
    letter = input(str("insert a later")).lower()
    while True:
        if letter in self.num_letters:
            print(f"{letter}, letter has already been tried")
            break
        else:
            print("not a valid letter")
            break
def play_game(word_list):
    for letter in word_list:
        if letter in word_list:
            print("congratulation you won")
        else:
            num_lives -= 1
            print("You run out of live")
            

game = Hangman(word_list, num_lives=5)