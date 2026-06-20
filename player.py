class Player:

    def __init__(self):

        self.name = "Hero"
        self.level = 1
        self.max_hp = 100
        self.hp = self.max_hp
        self.attack = 15
        self.defense = 5
        self.gold = 0
        self.exp = 0
        self.exp_to_next_level = 100
        self.inventory = {
            "Health Potion": 3
        }


    def show_stats(self):

        print("\n===== CHARACTER =====")

        print("Name:", self.name)

        print("Level:", self.level)

        print(f"HP: {self.hp}/{self.max_hp}")

        print("Attack:", self.attack)

        print("Defense:", self.defense)

        print("Gold:", self.gold)

        print(
            f"EXP: "
            f"{self.exp}/{self.exp_to_next_level}"
        )

        print("\n===== INVENTORY =====")

        for item, quantity in self.inventory.items():

            print(f"{item}: {quantity}")

        print("=====================")
        
    
    def show_inventory(self):

        print("\n===== INVENTORY =====")

        for item, quantity in self.inventory.items():

            print(f"{item}: {quantity}")

        print("=====================")


    def gain_exp(self, amount):

        self.exp += amount

        print(f"You gained {amount} EXP!")

        if self.exp >= self.exp_to_next_level:

            self.level_up()

    
    def level_up(self):

        self.level += 1

        self.max_hp += 20

        self.attack += 5

        self.hp = self.max_hp

        self.exp = 0

        self.exp_to_next_level += 50

        print("\n*** LEVEL UP! ***")

        print(f"You reached Level {self.level}!")

        print("HP increased!")

        print("Attack increased!")


    def use_potion(self):

        if self.inventory["Health Potion"] <= 0:

            print("You have no potions!")

            return

        if self.hp == self.max_hp:

            print("Your HP is already full!")

            return

        old_hp = self.hp

        heal_amount = 50

        self.hp += heal_amount

        if self.hp > self.max_hp:

            self.hp = self.max_hp

        self.inventory["Health Potion"] -= 1

        print(
            f"You recovered some HP!\n"
            f"{old_hp} -> {self.hp}"
        )