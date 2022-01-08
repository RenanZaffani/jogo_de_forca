import random


def hangman():
    welcome()
    secret_word = read_secret_word()
    right_letter = start_right_letter(secret_word)
    print(right_letter)

    hang = False
    right = False
    wrong_guesses = 0

    while not hang and not right:
        user_letter = give_user_letter()
        if user_letter in secret_word:
            mark_right_guesses(secret_word, user_letter, right_letter)
        else:
            wrong_guesses += 1
            draw_hang(wrong_guesses)

        hang = wrong_guesses == 6
        right = "_" not in right_letter

        print(right_letter)

    if right:
        message_win()
    else:
        message_lose(secret_word)


def welcome():
    print("***********************************")
    print("****Welcome to the Hangman Game****")
    print("***********************************")


def read_secret_word():
    archive = open("word.txt", "r")
    word = []

    for line in archive:
        line = line.strip()
        word.append(line)

    archive.close()

    number = random.randrange(0, len(word))
    secret_word = word[number].upper()
    return secret_word


def start_right_letter(secret_word):
    return ["_" for letter in secret_word]


def give_user_letter():
    user_letter = input("What letter? ").strip().upper()
    return user_letter


def mark_right_guesses(secret_word, user_letter, right_letter):
    index = 0

    for letter in secret_word:
        if user_letter.upper() == letter.upper():
            # print(f"I found the letter {user_letter} in the position {index}.")
            right_letter[index] = letter
        index += 1


def message_win():
    print("Congratulations, YOU WON!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def message_lose(secret_word):
    print("Well... You was hang!")
    print(f"The word was {secret_word}.")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def draw_hang(wrong_guesses):
    print("  _______     ")
    print(" |/      |    ")

    if wrong_guesses == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if wrong_guesses == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if wrong_guesses == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if wrong_guesses == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if wrong_guesses == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if wrong_guesses == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if wrong_guesses == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    hangman()
