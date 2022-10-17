#Guess the number
#If n=18 , user need to guess that number.
#Number of guesses 9 , print no.of guesses left
#Number of guesses he took to finish
# game over


n=18
print("Kindly guess the number from 1 to 20/n Number of guesses is limited to only 9 times:")
no_of_guesses =1
while(no_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if (guess_number < 18):
        print("You have guessed the lesser number")
        continue
    elif (guess_number > 18):
        print("You have guessed the greater number")
        continue
    else:
        print("You won")
        print("Number of guesses he took to finish", no_of_guesses)
        break
print("No. of guesses left",9 - no_of_guesses)
no_of_guesses = no_of_guesses + 1

if (no_of_guesses > 9):
    print("Game Over")

