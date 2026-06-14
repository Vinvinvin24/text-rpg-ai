class Player:

    def __init__(self):

        self.name = "Hero"
        self.level = 1
        self.hp = 100
        self.attack = 15
        self.defense = 5
        self.gold = 0

    def show_stats(self):

        print("\n===== CHARACTER =====")

        print("Name:", self.name)

        print("Level:", self.level)

        print("HP:", self.hp)

        print("Attack:", self.attack)

        print("Defense:", self.defense)

        print("Gold:", self.gold)

        print("=====================")