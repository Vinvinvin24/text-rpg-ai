from player import Player


def town_menu(player):

    while True:

        print("\n===== TOWN =====")

        print("1. Explore")

        print("2. Rest")

        print("3. Character")

        print("4. Quit")

        choice = input("Choice: ")

        if choice == "1":

            print("\nYou walk outside the town...")
            print("Nothing happens yet.")

        elif choice == "2":

            print("You take a short rest.")

        elif choice == "3":

            player.show_stats()

        elif choice == "4":

            print("Goodbye!")

            break

        else:

            print("Invalid option.")


name = input("Enter your name: ")

player = Player()

player.name = name

print(f"\nWelcome to the town, {player.name}!")

town_menu(player)