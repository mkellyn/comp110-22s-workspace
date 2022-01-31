"""A step towards wordle by creating a wordle with one shot."""

__author__ = 730308418

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
# given constants
secret_word: str = "python"
secret_index: int = 0
guess_word: str = input(f"What is your {len(secret_word)}-letter guess?")
guess_index: int = 0
box_emoji: str = ""
character_found: bool = False
# all my variables listed at the top, the guess word has to be inputted by the user
# I used an f-string to make sure the number used in the input for the guess equals the number of characters in the secret word
while len(guess_word) != len(secret_word):
    guess_word = input(f"That was not {len(secret_word)}-letters! Try again:")
# first have to check if the length of the guessed word == the length of the secret word, if not the loop has to keep going based on the new input

while guess_index < len(guess_word):
    character_found = False
    secret_index = 0
    # have to reset these two variables each time so that you can go through the loop again
    # straight from directions in COMP 110 website
    while character_found is not True and secret_index < len(secret_word):
        if guess_word[guess_index] == secret_word[secret_index]:
            # if the two characters are the same
            if guess_index == secret_index:
                # if the two indices are the same
                box_emoji = box_emoji + GREEN_BOX
                character_found = True
                # above stops the loop
            else:
                if guess_word[guess_index] != secret_word[guess_index]:
                    box_emoji = box_emoji + YELLOW_BOX
                    character_found = True
                else:
                    secret_index = secret_index + 1
                # so the character is found, but not at the same index, then the index of the secret word is increased so the next character is checked
        else:
            secret_index = secret_index + 1
            if secret_index == len(secret_word):
                box_emoji = box_emoji + WHITE_BOX
                # this came from guess and check. if line 44 is not indented, then white boxes show up each time two characters are checked and don't match
    guess_index = guess_index + 1   
print(box_emoji)
    
if guess_word != secret_word:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")