import random
import re

SIZE_TXT = 854
HANGMANPICS = ['''
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
         /|\\  |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|\\  |
         /    |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        =========''']


def driver():
    used_letters = []
    num_incorrect_guesses = 0
    correct_spots = []
    word_guessed = False
    num_correct_guesses = 0

    print("Lets play Hangman!")

    word = pick_random_word()

    for element in range(len(word)):
        correct_spots.append(False)

    while num_incorrect_guesses < 6 and not word_guessed:
        print(HANGMANPICS[num_incorrect_guesses])
        print_spots_guessed(correct_spots, word)
        print_used_letters(used_letters)
        user_guess = get_user_guess(used_letters)

        num_occurrences_of_word = matching_words(user_guess, word, correct_spots)
        if num_occurrences_of_word == 0:
            num_incorrect_guesses += 1
        else:
            num_correct_guesses += num_occurrences_of_word

        if num_correct_guesses == len(word):
            word_guessed = True

    if word_guessed:
        print("You Win!!!")
    else:
        print(HANGMANPICS[6])
        print("GAME OVER")
        print("The correct word was: " + word)


def matching_words(user_guess, word, correct_spots):
    """
    This method will check the user guess with the word.
    :param correct_spots: the correct spots that the user has guessed.
    :param user_guess: the guess that the user has entered
    :param word: the word that the user is trying to guess
    :return: the number of words that matched.
    """
    res = [i.start() for i in re.finditer(user_guess, word)]

    if len(res) != 0:
        for x in res:
            correct_spots[x] = True

    return len(res)


def print_letters_used(used_letters):
    """
    :param used_letters: the letters that have been used.
    :return: nothing
    """
    for x in used_letters:
        print(x)


def get_user_guess(used_letters):
    """
    This method will get the user guess and ensure that is is valid (not already been guessed and is a letter)
    and will return that value after adding it to used letters list.

    :param used_letters: the letters that have already been used.
    :return: the user guess (character)
    """
    while True:
        user_input = input("Please enter a guess: ")
        user_input = user_input.lower()
        if not (len(user_input) == 1):
            print("Please enter only 1 character")
        elif not (user_input.isalpha()):
            print("Please enter a letter.")
        elif user_input in used_letters:
            print("You've already guessed that!")
        else:
            used_letters.append(user_input)
            return user_input


def print_spots_guessed(correct_spots, word):
    """
    This method will print out all of the correct spots that the user has currently guessed.
    :param word: the word that the user is trying to guess
    :param correct_spots:
    :return: nothing.
    """
    print()
    for x in range(len(correct_spots)):
        if not (correct_spots[x]):
            print("_ ", end=" ")
        else:
            print(word[x], end=" ")
    print("\n")


def print_used_letters(used_letters):
    """
    This method will print out all the letters the user has used so far.
    :param used_letters:
    :return: nothing.
    """
    print("Used Letters: ", end=" ")
    print(",".join(used_letters))


def pick_random_word():
    """
    This method will pick a random word for us from the word bank.
    :return: the word randomly chosen.
    """
    # hard coded limits to end because we know the text file size and we can save iterating through the file.
    index = random.randint(1, SIZE_TXT)
    file = open("RandomWords.txt", "r")
    for x in range(index - 1):
        file.readline()

    word = file.readline().strip()
    file.close()
    return word


# Run the driver code
driver()
