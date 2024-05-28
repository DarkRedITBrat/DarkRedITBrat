quotes = { "1": "Ich liebe den Geruch von Napalm am Morgen.",
        "2": "Sozialismus oder Barbarei. Das sind die beiden Möglichkeiten.",
        "3": "Die Demokratie ist die schlechteste Regierungsform, ausgenommen alle anderen Formen, die von Zeit zu Zeit ausprobiert worden sind."}
correct_answers = { "1": "Apocalypse Now", "2": "Rosa Luxemburg", "3": "Winston Churchill"}

def main():
    greeting()
    run_quiz(quotes, correct_answers)
    player_score()
    fare_well()
    end_of_game()

def greeting():
    print("Willkommen zum Quotes Quiz!")
    global user_name
    user_name = input("Wie heißt du? ")
    print("Hallo " + user_name + "!")

def run_quiz(quotes, correct_answers):
    print("Willkommen zum Quotes Quiz!")
    print("Hier sind die Zitate:")
    for key, value in quotes.items():
        print(value)
        answer = input("Wer hat das gesagt? ")
        if answer == correct_answers[key]:
            print("Richtig!")
        else:
            print("Falsch! Die richtige Antwort ist: " + correct_answers[key])

def player_score():
    global score
    score = 0
    for key, value in quotes.items():
        answer = input("Wer hat das gesagt? ")
        if answer == correct_answers[key]:
            score = score + 1
    print("Du hast " + str(score) + " von " + str(len(quotes)) + " Fragen richtig beantwortet.")

def end_of_game():
    print("Danke fürs Mitspielen!")
    if score == 3:
        print("Perfekt! Du hast alle Fragen richtig beantwortet!")
    elif score == 2:
        print("Gut gemacht! Du hast die meisten Fragen richtig beantwortet!")
    elif score == 1:
        print("Nicht schlecht! Du hast eine Frage richtig beantwortet!")
    else:
        print("Schade! Du hast keine Frage richtig beantwortet!")

def fare_well():
    print("Auf Wiedersehen " + user_name + "!")
    print("Bis zum nächsten Mal!")

def end_of_game():
    print("Das Programm endet nun.")

if __name__ == "__main__":
    main()
