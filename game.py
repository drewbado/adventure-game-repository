import gamefunctions_

def main():
    hp = 30
    gold = 10
    running = True

    gamefunctions_.print_welcome()

    while running:
        gamefunctions_.display_town_menu(hp, gold)
        choice = input("Enter choice (1-3): ")

        if choice == "1":
            hp, gold = gamefunctions_.fight_monster(hp, gold)
            if hp <= 0:
                print("Game Over.")
                running = False
        elif choice == "2":
            hp, gold = gamefunctions_.sleep(hp, gold)
        elif choice == "3":
            print("Thanks for playing!")
            running = False
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
