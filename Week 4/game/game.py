import random
import sys

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass


def ask():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                return guess
        except ValueError:
            pass


n = random.randint(1, level)

while True:
    try:
        guess = ask()
        if n == guess:
            print("Just right!")
            break
        elif n > guess:
            print("Too small!")
            pass
        else:
            print("Too large!")
            pass
    except:
        pass
