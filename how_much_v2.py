# Functions go here...
def num_check (question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    whole not valid:
        try:
            # Ask the question...
            response = int(input(question))
            # If the amount is too low / too high give
            if low < response <= high:
                return response

            # Output an error...
            else:
                print(error)
        except ValueError:
            print(error)

# Main routine goes here...

