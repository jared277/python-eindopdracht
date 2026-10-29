player_class = {
    "warrior",
    "mage",
    "archer",
    "rogue",
    "knight",
    "sorcerer"
}

chosen_class = input("kies klasse ")
if chosen_class in player_class:
    match chosen_class:
        case "warrior":
            health = 150
            damage = 20
        case "mage":
            health = 80
            damage = 35
        case "archer":
            health = 100
            damage = 25
        case "rogue":
            health = 90
            damage = 30
        case "knight":
            health = 200
            damage = 15
        case "sorcerer":
            health = 50
            damage = 75
        case _:
            print("er ging iets mis")
    print(f" Gekozen klasse: {chosen_class} \n Gezondheid: {health} \n schade: {damage}")
else:
    print('er ging iets mis')

