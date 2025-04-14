def buy_item(item, gold, inventory):
    if item == "sword" and gold >= 30:
        inventory.append({"name": "sword", "type": "weapon", "durability": 3})
        print("You bought a sword!")
        return gold - 30
    elif item == "orb" and gold >= 20:
        inventory.append({"name": "orb", "type": "magic"})
        print("You bought a magic orb!")
        return gold - 20
    else:
        print("Not enough gold or invalid item.")
        return gold

def equip_weapon(inventory):
    for item in inventory:
        if item["type"] == "weapon":
            print(f"You equipped {item['name']}")
            return item
    print("No weapon to equip.")
    return None

def fight_monster(hp, gold, inventory, equipped):
    print("\nYou encounter a monster!")

    for item in inventory:
        if item["type"] == "magic":
            print("You used your magic orb and instantly won!")
            inventory.remove(item)
            gold += 10
            return hp, gold

    print("Fighting monster...")

    if equipped and equipped["durability"] > 0:
        print(f"You used your {equipped['name']} to win.")
        equipped["durability"] -= 1
        gold += 10
    else:
        print("You had no weapon. You lost 10 HP.")
        hp -= 10

    return hp, gold
