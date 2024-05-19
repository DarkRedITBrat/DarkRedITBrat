#definition des Haupt codes als function: main()
def main():
    name=input("What's your Name? ")
    hello(name)

#Definition einer neuen function.
def hello(to="world"):
    print("hello,", to)

#call der function main() um den code ausführen.
main()