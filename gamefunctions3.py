import json

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
            print(f"You equipped the {item['name']}.")
            return item
    print("No weapons to equip.")
    return None

def fight_monster(hp, gold, inventory, equipped):
    print("A monster appears!")

    # Use orb if available
    for item in inventory:
        if item["type"] == "magic":
            print("You used a magic orb and won!")
            inventory.remove(item)
            gold += 10
            return hp, gold

    # Fight with or without weapon
    if equipped and equipped["durability"] > 0:
        print(f"You used your {equipped['name']} to win.")
        equipped["durability"] -= 1
        gold += 10
    else:
        print("You had no weapon. You lost 10 HP.")
        hp -= 10

    return hp, gold

def save_game(filename, hp, gold, inventory, equipped):
    data = {
        "hp": hp,
        "gold": gold,
        "inventory": inventory,
        "equipped": equipped
    }
    with open(filename, "w") as file:
        json.dump(data, file)
    print("Game saved.")

def load_game(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        print("Game loaded.")
        return data["hp"], data["gold"], data["inventory"], data.get("equipped")
    except FileNotFoundError:
        print("Save file not found. Starting new game.")
        return 30, 50, [], None
