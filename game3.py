import gamefunctions3

def main():
    print("Welcome to the Adventure Game!")
    print("1) New Game")
    print("2) Load Game")
    choice = input("Choose: ")

    if choice == "2":
        filename = input("Enter save filename: ")
        hp, gold, inventory, equipped = gamefunctions3.load_game(filename)
    else:
        hp = 30
        gold = 50
        inventory = []
        equipped = None

    running = True

    while running:
        print(f"\nHP: {hp}, Gold: {gold}")
        print("1) Fight Monster")
        print("2) Sleep (5 gold)")
        print("3) Shop")
        print("4) Equip Weapon")
        print("5) Save and Quit")

        choice = input("Choose: ")

        if choice == "1":
            hp, gold = gamefunctions3.fight_monster(hp, gold, inventory, equipped)
        elif choice == "2":
            if gold >= 5:
                hp = 30
                gold -= 5
                print("You are fully healed.")
            else:
                print("Not enough gold.")
        elif choice == "3":
            item = input("Buy 'sword' (30g) or 'orb' (20g): ").lower()
            gold = gamefunctions3.buy_item(item, gold, inventory)
        elif choice == "4":
            equipped = gamefunctions3.equip_weapon(inventory)
        elif choice == "5":
            filename = input("Enter filename to save: ")
            gamefunctions3.save_game(filename, hp, gold, inventory, equipped)
            running = False
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
