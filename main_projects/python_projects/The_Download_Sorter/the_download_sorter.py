import os
import shutil
from builtins import input

# Version alpha_0.0.2-0006
# Variables (Global)
divider_lines = "================================================================================="
codername = "DarkRedITBrat"

# Lists
correct_answers_file_creation = ["yes", "no"]

def main():
    """
    The main function of the script.
    It executes the necessary steps to sort files into corresponding folders.
    """
    file_creation = getting_file_creation_input()
    if file_creation:
        create_new_files()
    else:
        getting_file_data()
        compare_file_suffix()
        add_keyword()
        move_file()
    print_sorted_file_list()
    export_printed_dict()
    print_completion_status()

def getting_file_creation_input() -> bool:
    """
    This function asks the user if a new sorting folder should be created.
    It will repeat the question until a valid answer is given (either 'yes' or 'no').
    If the user enters an invalid answer more than twice, the function will return False.

    Returns:
    bool: True if the user wants to create a new sorting folder, False otherwise.
    """
    for _ in range(2):  # Loop runs up to 2 times
        user_input = input("Should new sorting folders be created? (yes/no): ").lower()

        if user_input in correct_answers_file_creation:
            print("That's the correct answer!")
            return user_input == "yes"  # Return True if user_input is 'yes', False otherwise
        else:
            print("Sadly, this was the wrong answer. Please try again.")

    print("You have entered an invalid answer too many times. Exiting the program.")
    return False  # Return False if the loop ends without a valid answer

def create_new_files():
    """
    Creates new files based on user input.
    """
    # Implementation of creating new files
    pass

def getting_file_data():
    """
    Gets data of files for further processing.
    """
    # Implementation of getting file data
    pass

def compare_file_suffix():
    """
    Compares the file suffixes for further processing.
    """
    # Implementation of comparing file suffix
    pass

def add_keyword():
    """
    Adds a keyword to the files for further processing.
    """
    # Implementation of adding keyword
    pass

def move_file():
    """
    Moves the files to the corresponding folders.
    """
    # Implementation of moving file
    pass

def print_sorted_file_list():
    """
    Prints the sorted file list.
    """
    # Implementation of printing sorted file list
    pass

def export_printed_dict():
    """
    Exports the printed dictionary.
    """
    # Implementation of exporting printed dict
    pass

def print_completion_status():
    """
    Prints the final completion message to the user.
    """
    print(divider_lines)
    print("All Files have been sorted into the corresponding folders, \n       Unknown file types can be found in the 'Unknown File Types'-Folder!\n")
    print(f"This Script ends now! \n          - Thank you for using my scripts, your {codername}!")
    print(divider_lines)

if __name__ == "__main__":
    main()