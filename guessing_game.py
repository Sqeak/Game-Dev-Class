import random
number = 0
guess = 0
numRange = 100
running = True
numberOfGuesses = 0

while running:
    number = random.randrange(1, numRange+1)
    print("I'm picking a number between 1 and " + str(numRange) + ". Let's see if you can guess it!")
    input("Press the enter button to start!")
    while guess != number:
        try:
            guess = int(input("What is your guess? "))
        except ValueError:
            print("That's not a valid input!")
            break
        numberOfGuesses += 1
        if guess == number:
            print("Correct! you did it in " + str(numberOfGuesses) + " guesses!")
            
            if input("Do you wanna play again? (y/n) ") == "n":
                running = False
            
        else:
            if guess < number:
                print("I'm sorry, that's too low")
            else:
                print("I'm sorry, that's too high")
                
        

        