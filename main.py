import random


def main():
    spielt_spiel = True
    while spielt_spiel:
        print("Willkommen beim Spiel \"Galgenmännchen\"!\n"
              "Sie haben 6 Versuche, das Wort zu erraten.\n")

        ary_string = wortliste()
        wort_index = random.randint(0, len(ary_string) - 1)
        wort = ary_string[wort_index].lower()
        buchstaben = list(wort)
        benutzer_versuch = ['_'] * len(buchstaben)

        spiel(buchstaben, benutzer_versuch)

        for buchstabe in buchstaben:
            print(buchstabe, end='')
        print()

        spielt_spiel = naechstes_spiel()

    print("Danke für das Spiel!")


def wortliste():
    wortliste = [
        "Rekrutierung", "Staatlichkeit", "Abgeordneter", "polemisch", "Spekulant",
        "Rapier", "Holzklotz", "Feuchtigkeit", "Raffinade", "Narbe", "Leuchten",
        "MORALIST", "TROCKENRAUM", "Brücke", "Funktion"
    ]
    return wortliste


def spiel(buchstaben, benutzer_versuch):
    versuche = 6
    schleife = True
    fehler = True

    while schleife:
        if versuche == 0:
            print("Deine Versuche sind aufgebraucht! \nWort: ")
            break

        print(' '.join(benutzer_versuch))
        print("Geben Sie einen Buchstaben ein: ", end='')
        benutzer = gueltig()

        for i in range(len(buchstaben)):
            if buchstaben[i] == benutzer:
                benutzer_versuch[i] = benutzer
                fehler = False

        if buchstaben == benutzer_versuch:
            print("Du hast das Wort erraten!")
            schleife = False
        elif fehler:
            print(f"Dieser Buchstabe ist nicht im Wort. Versuche übrig: {versuche}")
            versuche -= 1
            galgenmann_zeichnen(6 - versuche)
        else:
            fehler = True


def gueltig():
    gueltig = '0'
    benutzer_buchstabe = ""
    fehlschlag = "Geben Sie einen Buchstaben ein: "
    schleife = True

    while schleife:
        benutzer_buchstabe = input()
        if len(benutzer_buchstabe) != 1:
            print(fehlschlag, end='')
        else:
            gueltig = benutzer_buchstabe[0]
            if gueltig.isalpha():
                schleife = False
            else:
                print(fehlschlag, end='')

    return gueltig


def galgenmann_zeichnen(fehler):
    galgenmaenner = [
        "  ______\n" +
        "  |    |\n" +
        "       |\n" +
        "       |\n" +
        "       |\n" +
        "       |\n" +
        "       |\n" +
        "_______|",

        "  ______\n" +
        "  |    |\n" +
        "  O    |\n" +
        "       |\n" +
        "       |\n" +
        "       |\n" +
        "       |\n" +
        "_______|",

        "  ______\n" +
        "  |    |\n" +
        "  O    |\n" +
        "  |    |\n" +
        "       |\n" +
        "       |\n" +
        "       |\n" +
        "_______|",

        "  ______\n" +
        "  |    |\n" +
        "  O    |\n" +
        " /|    |\n" +
        "       |\n" +
        "       |\n" +
        "       |\n" +
        "_______|",

        "  ______\n" +
        "  |    |\n" +
        "  O    |\n" +
        " /|\\   |\n" +
        "       |\n" +
        "       |\n" +
        "       |\n" +
        "_______|",

        "  ______\n" +
        "  |    |\n" +
        "  O    |\n" +
        " /|\\   |\n" +
        " /     |\n" +
        "       |\n" +
        "       |\n" +
        "_______|",

        "  ______\n" +
        "  |    |\n" +
        "  O    |\n" +
        " /|\\   |\n" +
        " / \\   |\n" +
        "       |\n" +
        "       |\n" +
        "_______|"
    ]

    print(galgenmaenner[fehler])


def naechstes_spiel():
    naechstes_spiel = True
    angebot = "Möchten Sie noch einmal spielen? (ja/nein): "
    print(angebot)
    antwort = ""

    while True:
        antwort = input()
        if antwort.lower() == "ja":
            return naechstes_spiel
        elif antwort.lower() == "nein":
            naechstes_spiel = False
            return naechstes_spiel
        else:
            print(angebot)


if __name__ == "__main__":
    main()
