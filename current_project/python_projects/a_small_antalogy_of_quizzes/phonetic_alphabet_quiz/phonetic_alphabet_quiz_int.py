questions = [
    ("A", "Alpha"),
    ("B", "Bravo"),
    ("C", "Charlie"),
    # Add more questions here
]

def main():
    """
    The main function of the program.
    """
    user_name = get_user_name()
    begin_quiz(user_name)
    score = run_quiz(questions)
    user_score(user_name, score)
    end_program(user_name)

def get_user_name():
    """
    Prompt the user to enter their name and return it.
    """
    return input("Please enter your name: ")

def begin_quiz(user_name):
    """
    Display the welcome message and instructions for the quiz.
    """
    print("Welcome to the Phonetic Alphabet Quiz, " + user_name + "!")
    print("You will be presented with " + str(len(questions)) + " questions, one for each letter of the alphabet.")
    print("Please enter the phonetic alphabet word for each letter.")
    print("Good luck!")

def run_quiz(questions):
    """
    Run the quiz and return the user's score.
    """
    counter = 0
    score = 0
    for letter, answer in questions:
        counter += 1
        user_input = input("What is the phonetic alphabet word for the letter " + letter + "? ").capitalize()
        if user_input == answer:
            score += 1
        else:
            print("Incorrect. The correct answer is " + answer + ".")
            print("But that's not a problem, let's move on to the next question. Good luck!")
    return score

def user_score(user_name, score):
    """
    Display the user's final score.
    """
    print("Congratulations " + user_name + "! You have completed the quiz.")
    print("Your final score is " + str(score) + " out of " + str(len(questions)) + ".")
    print("Thank you for taking part in the Phonetic Alphabet Quiz.")

def end_program(user_name):
    """
    Display the goodbye message.
    """
    print("Goodbye " + user_name + "!")

main()
