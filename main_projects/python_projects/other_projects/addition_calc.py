def main():
    first=input("First:")
    second=input("Second:")
    if first == int() or float() and second == int() or float():
        calculation()
    else: 
        print("Your Input wasnt recognized. Programm Ending!")


def calculation(to):
    x=float("first")
    y=float("second")
    #Frage ob die Userin addieren, subtrahieren, multiplizieren oder dividiren will.
    type=input("Do you wanna add, subtract, multiply or divide?: Please type A for Add, S for Subtract, M for Multiply or D for Divide: ")
    # den entsprechenden rechenpfad gehen.
    if type == 'A':
        z = y+x
        print("Sum =", z )
    if type == 'S':
        z = x-y
        print("Sum =", z )
    if type == 'M':
        z = y*x
        print("Sum =", z )
    if type == 'D':
        z = x/y
        print("Sum =", z )
    else: 
        print("Your Input wasnt recognized. Programm Ending!")