class Player:

    def __init__(self):

        self.name = "Hero"
        self.level = 1
        self.hp = 100
        self.attack = 15
        self.defense = 5
        self.gold = 0
        self.exp = 0
        self.exp_to_next_level = 100

    def show_stats(self):

        print("\n===== CHARACTER =====")

        print("Name:", self.name)

        print("Level:", self.level)

        print("HP:", self.hp)

        print("Attack:", self.attack)

        print("Defense:", self.defense)

        print("Gold:", self.gold)

        print("EXP:", self.exp)

        print("Next Level:", self.exp_to_next_level)

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