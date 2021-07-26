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
    print("The rules of the game go here")
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


# Main routine goes here...
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()


# Ask user how much they want to play with...

