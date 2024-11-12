# Samuel Bird
# 11.11.2024
# Coding challenge for OIT Student Programmar position, Brigham Young University
"""The Problem
Create a game of hangman

Rules & Requirements
1. Greet the user welcoming them to the game
2. The program randomly selects a word from a list of 10 words with different lengths, you as the developer choose
the words.
3. The program indicates to the user how many letters are in the word
4. The user is asked to guess a letter
a. If the letter is in the word, the letter is displayed in the correct position of the word with all previously
guessed correct letters
b. If the letter is not in the word, display the letter indicating it is not in the word with all previously guessed
letters that are not in the word
5. The program displays how many guesses have been made, with how many correct and incorrect guesses.
6. The program continues to ask the user for guesses until all the letters in the word are guessed correctly.
7. When all letters of the word are guessed correctly,
a. the program tells the user they have correctly guessed the word
b. and indicates the number of guesses it took
8. The program then asks the user if they would like to try again or quit
a. If the user indicates they want to continue, the program chooses a different word randomly and the play
continues
b. If the user indicates they want to quit, the program thanks them for playing and quits.
9. You can choose to use a terminal interface or a web interface
Extra credit
10. Draw a gallows and person being hanged drawing a new body part each time a guess is wrong
"""
import random
    # 1.
print("Hello user! Welcome to Hang Man.")
# 2. 
def play_again():
    word_bank = ["cosmo", "cricket", "odd", "clock", "celebrate", "glasses", "trinket", "mirror", "coding", "computer"]
    word_to_guess = random.choice(word_bank)
    dashes: list[str] = []
    i = 0
    for i in range(len(word_to_guess)):
        dashes.append("-")
        i+=1
    # 3.
    print(f"there are {i} letters in your mystery word!")
    for dash in dashes:
        print(dash, end='')
    print("\n")
# 4. 
    letters_guessed: dict[str, str] = {}
    guesses = 0
    r = 0
    w = 0
    wrong_letters = []
    while "".join(dashes) != word_to_guess: # I need to change this and figure out how to correctly compare the word
        letter = input("Guess a letter!\n")
        if not letter.isalpha():
            print("This is not a letter. Plesae guess a letter")
        if letter in letters_guessed:
            print("You have already guessed that letter!")
        else:
            letters_guessed[letter] = letter
            if letter not in word_to_guess:
                wrong_letters.append(letter)
                w+=1
                guesses+=1
                print(f"{letter} is not in the word! Other letters not in the word are: ", end='')
                for wrong in wrong_letters:
                    print(wrong, ", ", end='')
                print("\n")
                for dash in dashes:
                    print(dash, end='')
                print("\n")
                print(f"Total guesses: {guesses}. \n Right: {r}\n Wrong: {w}\n")
            elif letter in word_to_guess:
                j = 0
                for l in word_to_guess:
                    if l == letter:
                        dashes[j] = letter
                    j+=1
                for dash in dashes:
                    print(dash, end='')
                print("\n")
                r+=1
                guesses+=1
                print(f"Total guesses: {guesses}. \n Right: {r}\n Wrong: {w}\n")
            else:
                print("Error: an error occured...")
    print(f"You guessed the word correctly! The word is {word_to_guess}, and it took you {guesses} guesses\n")
    again = input("Would you like to play again? Y/N\n")
    if again.capitalize() == "Y":
        play_again()
    elif again.capitalize() == "N":
        print("Thanks for playing!")
        return
play_again()