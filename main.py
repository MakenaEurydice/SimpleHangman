import random
from art import stages

# select a random word
chosen_word = random.choice(open("words.txt").read().split())
word_length = len(chosen_word)

display = []
for i in range(word_length):
    display += '_'

end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("Already guessed.Try another letter")

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    # Let user know if guessed letter is not in the word
    if guess not in chosen_word:
        print("Letter you've guessed is not in the word.You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"Oops,you lose.The word was {chosen_word}")

    # Print elements in the list as a string
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
