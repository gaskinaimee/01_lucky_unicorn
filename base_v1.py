import random

# Functions go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or response =="n":
            response = "no"
            return response
        else:
            print("Please answer with either yes or no.")

def instructions():
    print("***** How to Play *****")
    print()
    print("Choosing a starting amount (minimum $1, maximum $10).")
    print("Then press <enter> to play. You will get either a horse, a zebra, a donkey or a unicorn.")
    print("It cost $1 per round. Depending on your prize, you might win some of the money back." \
          " Here's the payout amount...")
    print("Unicorn: $5 (balance increases by $4)")
    print("Horse: $0.50 (balance decreases by $0.50)")
    print("Zebra: $0.50 (balance decreases by $0.50)")
    print("Donkey: $0.00 (balance decreases by $1)")
    print()
    return instructions

def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10.\n"
    valid = False
    while not valid:
        try:
            # Ask the question.
            response = int(input(question))
            # If the amount is too low/too high give
            if low < response <= high:
                return response

            # Output an error
            else:
                print(error)

        except ValueError:
            print(error)

def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

# Main routine goes here...
statement_generator("Welcome to the Lucky Unicorn Game", "*")
print()

played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()

print()

# Ask user how much they want to play with...
how_much = num_check("How much would you like to play with?", 0, 10)

import random

# Set balance for testing purposes.
balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    # Increase number of rounds played.
    rounds_played += 1

    # Print round number
    print("*** Round #{} ***".format(rounds_played))

    chosen_num = random.randint(1, 100)

    # Adjust balance
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        prize_decoration = "!"
        balance += 4
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        prize_decoration = "D"
        balance -= 1
    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
            prize_decoration = "H"

        else:
            chosen = "zebra"
            prize_decoration = "Z"
        balance -= 0.5
    outcome = "You got a {}. Your balance is " \
          "${:.2f}".format(chosen, balance)

    statement_generator(outcome, prize_decoration)

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press enter to play again or xxx to quit.")

print()
print("Final balance: {}".format(balance))
print("Thank you for playing.")

