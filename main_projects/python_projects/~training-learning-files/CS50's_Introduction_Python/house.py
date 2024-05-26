name = input("What's vour name?: ")

match name:
    case "Harry"|"Hermione"|"Ron":
        print("Griff.")
    case "Draco":
        print("Slith.")
    case _:
        print("Who?")