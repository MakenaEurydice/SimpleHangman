import random
from art import stages

chosen_word = random.choice(open("words.txt").read().split())
word_length = len(chosen_word)

end_of_game = False
lives = 6

display = []
for i in range(word_length):
    display += '_'

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("Letter already guessed")

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print("Letter you've guessed is not in the word.You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Oops,you lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
