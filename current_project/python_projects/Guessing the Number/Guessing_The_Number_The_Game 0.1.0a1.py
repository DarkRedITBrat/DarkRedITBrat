from random import randint as ri # Importing the randint function from the random module

# Version 0.1.0a1

# Variables
random_number = ri(1,10) # Random number between 1 and 10
counter = 0 # Counter for the number of guesses

def main(): 
    """
    The main function that runs the Guessing The Number Game.
    """
    greeting()
    get_username()
    guessing_game()
    final_score()
    farewell()
    end_program()

def greeting(): 
    """
    Prints a welcome message to the user.
    """
    print("Welcome to the Guessing The Number Game!")


def get_username(): 
    """
    Prompts the user to enter their name and stores it in the global variable 'username'.
    """
    global username
    username = input("Enter your name: ")

def guessing_game(): 
    raise NotImplementedError("The guessing_game function is not implemented yet.")

def final_score(): 
    """
    Prints a message based on the number of guesses made by the user.
    """

    if counter == 1:
        print("You are a genius! You guessed the number in 1 try!") 
            # If the user guessed the number in 1 try
    elif counter < 10:
        print("Congratulations! You guessed the number in", counter, "tries! You might be a psychic!") 
            # If the user guessed the number in less than 10 tries
    elif counter <20:
        print("You have done an outstanding job and mastered the task brilliantly!")        
            # If the user guessed the number in less than 20 tries
    elif counter < 30:
        print("Very good performance, only a few minor details need improvement.")
            # If the user guessed the number in less than 30 tries
    elif counter < 40:
        print("A good job with some weaknesses, but overall satisfactory.")    
            # If the user guessed the number in less than 40 tries
    elif counter < 50:
        print("The performance is acceptable, but there are several areas that need improvement.")
            # If the user guessed the number in less than 50 tries
    elif counter >51 and counter <60:
        print("Unfortunately, there are many errors, and significant improvement is needed.")
            # If the user guessed the number in more than 51 tries
    else:
        print("The task was not solved satisfactorily, and there are considerable deficiencies.")
            # If the user guessed the number in more than 60 tries

def farewell(): 
    """
    Prints a farewell message to the user.
    """
    print("Thank you for playing the Guessing The Number Game!")

def end_program(): 
    """
    Prints a goodbye message and exits the program.
    """
    print("Goodbye!")
    exit()

if __name__ == "__main__":
    main()