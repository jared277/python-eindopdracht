print("v7")


vakken_en_cijfers = {
    "Engels": 10,
    "Nederlands": 5,
    "Python": 1
}

def calculate():
    vak_aantal = len(vakken_en_cijfers)
    if vak_aantal == 0:
        print("je hebt geen vakken toegevoegd")
        pass
    else:
        alles_bij_elkaar = sum(vakken_en_cijfers.values())

        gemiddelde = (alles_bij_elkaar / vak_aantal)

        print(f"je gemiddelde is: {gemiddelde}")

        if gemiddelde <= 5.5:
            print("je bent gezakt")
        else:
            print("je bent geslaagd")




while True:
    command = input("voer in wat je wilt doen (voegtoe/calculeer): ")
    if command == "calculeer":
        calculate()
    elif command == "voegtoe":
        vak = input("welk vak wil je toevoegen: ")
        cijfer = input("welk cijfer wil je toevoegen: ")
        try:
            cijfer = int(cijfer)
        except ValueError:
            print("je hebt een ongeldig caracter ingevoerd")
            continue
        vakken_en_cijfers[vak] = cijfer
    else:
        print("je hebt een verkeerde input gedaan probeer het opnieuw")