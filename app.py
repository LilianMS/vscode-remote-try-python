#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)
import random

@app.route("/")
def hello():
    return app.send_static_file("index.html")

#criando jogo pedra papel tesoura em python no console
#criando jogo pedra papel tesoura em python no console

def game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Please choose to continue...")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")
    userChoice = int(input("Please enter your choice: "))
    if userChoice == 1:
        print("You chose Rock!")
    elif userChoice == 2:
        print("You chose Paper!")
    elif userChoice == 3:
        print("You chose Scissors!")
    elif userChoice == 4:
        print("Thank you for playing!")
        exit()
    else:
        print("I don't understand your choice.")
    compChoice = random.randint(1, 3)
    if compChoice == 1:
        print("Computer chose Rock!")
    elif compChoice == 2:
        print("Computer chose Paper!")
    elif compChoice == 3:
        print("Computer chose Scissors!")
    if userChoice == compChoice:
        print("It's a tie!")
    elif userChoice == 1 and compChoice == 2:
        print("Paper covers Rock. You lose!")
    elif userChoice == 1 and compChoice == 3:
        print("Rock smashes Scissors. You win!")
    elif userChoice == 2 and compChoice == 1:
        print("Paper covers Rock. You win!")
    elif userChoice == 2 and compChoice == 3:
        print("Scissors cut Paper. You lose!")
    elif userChoice == 3 and compChoice == 1:
        print("Rock smashes Scissors. You lose!")
    elif userChoice == 3 and compChoice == 2:
        print("Scissors cut Paper. You win!")
    playAgain = input("Would you like to play again? (Y/N) ")
    if playAgain == "Y" or playAgain == "y":
        game()
    else:
        print("Thank you for playing!")
        exit()

game()
