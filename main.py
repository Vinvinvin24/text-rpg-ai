from player import Player
from enemy import Enemy
from random import choice
from random import randint

def combat(player, enemy):

    while player.hp > 0 and enemy.hp > 0:

        print("\n------")

        print(f"{player.name}: {player.hp} HP")

        print(f"{enemy.name}: {enemy.hp} HP")

        print("------")

        input("Press Enter to attack...")

        enemy.hp -= player.attack

        print(
            f"You hit the {enemy.name} "
            f"for {player.attack} damage!"
        )

        if enemy.hp <= 0:

            print(
                f"You defeated the {enemy.name}!"
            )

            player.gain_exp(
                enemy.exp_reward
            )

            player.gold += enemy.gold_reward

            

            print(
                f"You received "
                f"{enemy.gold_reward} gold!"
            )

            drop_chance = randint(1, 100)

            if drop_chance <= 30:

                player.inventory[
                    "Health Potion"
                ] += 1

                print(
                    "The enemy dropped "
                    "a Health Potion!"
                )

            break

        player.hp -= enemy.attack

        print(
            f"The {enemy.name} hits you "
            f"for {enemy.attack} damage!"
        )

    if player.hp <= 0:

        print("\nYou were defeated...")


def explore(player):

    enemies = [

        Enemy(
            "Goblin",
            30,
            8,
            25,
            10
        ),

        Enemy(
            "Wolf",
            40,
            10,
            40,
            20
        ),

        Enemy(
            "Slime",
            20,
            5,
            15,
            5
        )

    ]

    enemy = choice(enemies)

    print("\nYou leave town...")

    print(f"A {enemy.name} appears!")

    combat(player, enemy)


def inventory_menu(player):

    while True:

        print("\n===== INVENTORY =====")

        print("1. View Items")

        print("2. Use Health Potion")

        print("3. Back")

        choice = input("Choice: ")

        if choice == "1":

            player.show_inventory()

        elif choice == "2":

            player.use_potion()

        elif choice == "3":

            break

        else:

            print("Invalid option.")

            

def town_menu(player):

    while True:

        print("\n===== TOWN =====")

        print("1. Explore")

        print("2. Rest")

        print("3. Character")

        print("4. Inventory")

        print("5. Quit")

        choice = input("Choice: ")

        if choice == "1":

            explore(player)

        elif choice == "2":

            print("You take a short rest.")

        elif choice == "3":

            player.show_stats()

        elif choice == "4":

            inventory_menu(player)

        elif choice == "5":

            print("Goodbye!")

            break

        else:

            print("Invalid option.")


name = input("Enter your name: ")

player = Player()

player.name = name

print(f"\nWelcome to the town, {player.name}!")

town_menu(player)