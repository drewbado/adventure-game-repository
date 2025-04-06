def print_welcome():
    print("Welcome to the game!")

def print_shop_menu():
    print("Shop Items:")
    print("1. Sword - 100 gold")
    print("2. Shield - 75 gold")
    print("3. Potion - 25 gold")

def purchase_item(item, gold):
    prices = {"sword": 100, "shield": 75, "potion": 25}
    item = item.lower()
    if item in prices:
        if gold >= prices[item]:
            print(f"You bought a {item}!")
            return gold - prices[item]
        else:
            print("Not enough gold.")
    else:
        print("Item not found.")
    return gold

def random_monster():
    return {"name": "Goblin", "hp": 15, "attack": 4}

def display_town_menu(hp, gold):
    print("\nYou are in town.")
    print(f"Current HP: {hp}, Current Gold: {gold}")
    print("What would you like to do?")
    print("1) Leave town (Fight Monster)")
    print("2) Sleep (Restore HP for 5 Gold)")
    print("3) Quit")

def sleep(hp, gold):
    if gold >= 5:
        print("You slept and restored your HP!")
        return 30, gold - 5
    else:
        print("Not enough gold to sleep.")
        return hp, gold

def fight_monster(hp, gold):
    monster = random_monster()
    monster_hp = monster["hp"]
    monster_name = monster["name"]
    print(f"\nA wild {monster_name} appears!")

    while monster_hp > 0 and hp > 0:
        print(f"\nYour HP: {hp}, {monster_name} HP: {monster_hp}")
        print("1) Attack")
        print("2) Run Away")
        action = input("Choose an action: ")
        if action == "1":
            damage = 5
            monster_hp -= damage
            print(f"You hit the {monster_name} for {damage} damage.")
            if monster_hp > 0:
                hp -= monster["attack"]
                print(f"The {monster_name} hits you for {monster['attack']} damage.")
        elif action == "2":
            print("You ran away!")
            return hp, gold
        else:
            print("Invalid input. Try again.")

    if hp <= 0:
        print("You were defeated...")
    elif monster_hp <= 0:
        print(f"You defeated the {monster_name}!")
        gold += 10
        print("You found 10 gold!")

    return hp, gold
