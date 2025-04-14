import gamefunctions_

def main():
    hp = 30
    gold = 50
    inventory = []
    equipped = None
    running = True

    print("Welcome to the Adventure Game!")

    while running:
        print(f"\nHP: {hp}, Gold: {gold}")
        print("1) Fight Monster")
        print("2) Sleep (5 gold to heal)")
        print("3) Shop")
        print("4) Equip Weapon")
        print("5) Quit")

        choice = input("Choose: ")

        if choice == "1":
            hp, gold = gamefunctions_.fight_monster(hp, gold, inventory, equipped)
        elif choice == "2":
            if gold >= 5:
                hp = 30
                gold -= 5
                print("You feel rested.")
            else:
                print("Not enough gold.")
        elif choice == "3":
            item = input("Buy sword (30g) or orb (20g): ").lower()
            gold = gamefunctions_.buy_item(item, gold, inventory)
        elif choice == "4":
            equipped = gamefunctions_.equip_weapon(inventory)
        elif choice == "5":
            running = False
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
