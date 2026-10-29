monster_health = 150
player_damage = 25
attacks = 0
while monster_health > 0:
    monster_health -= player_damage
    if monster_health <= 0:
        print(f"monster verslagen in {attacks} aanvallen")
        monster_health = 0

    else:
        attacks += 1
        print(f"het monster heeft nog {monster_health} health")


print()
print()
print()
#=======================
attacks = 0

monsters = [
    {"naam": "goblin", "health": 50},
    {"naam": "ork", "health": 100},
    {"naam": "draak", "health": 150},
]




for monster in monsters:
        attacks = 0
        monster_health = monster["health"]
        monster_naam = monster["naam"]
        print(f"de {monster_naam} heeft {monster_health} health")
        while monster_health > 0:
            monster_health -= player_damage
            attacks += 1
            if monster_health <= 0:
                monster_health = 0
                print(f"{monster_naam} verslagen in {attacks} aanvallen")
                print()
                print()
                print()
            else:
                print(f"de {monster_naam} heeft nog {monster_health} health")