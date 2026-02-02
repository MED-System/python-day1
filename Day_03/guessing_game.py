secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

# The loop runs as long as the guess is wrong AND they haven't run out of tries
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

# Final check to see if they won or lost
if out_of_guesses:
    print("Out of guesses, YOU LOSE!")
else:
    print("You win!")