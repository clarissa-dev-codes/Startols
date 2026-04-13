"this is the logic for taking care of the pet. It's the name, species(what startol it is), hunger and cleanliness. Will"
"be adding more to this as things go on. I need to make the egg timer though because it's like three irl days"
"Need to figure out how many seconds that is because that is a lot of seconds and Python is particular about that"

# 3 days = 259200 seconds
# 4 days = 345600 seconds
# 5 days = 432000 seconds

#50 xp a day

import pygame
import json
import datetime
import random


RARITIES =["Common", "Rare", "Legendary"]
WEIGHTS = [70, 20, 10]

SPECIES_DATABASE = {
    "Common": ["Fire", "Water", "Plants", "Earth", "Metal", "Bubble", "Ice", "Lightning", "Light", "Dark"],
    "Rare": ["Crystal", "Book", "Butterfly", "Coffee", "Dice", "Pearl", "Digital"],
    "Legendary": ["Star", "Moon", "Sun"]
}

def pick_new_startol():
    rarity = random.choices(RARITIES, weights=WEIGHTS, k=1)[0]
    species = random.choices(SPECIES_DATABASE[rarity])

    return rarity, species


#this is so each instance has its own stuff
class Startol:
    def __init__(self, name=None):
        rarity, species = pick_new_startol()

        self.stats = {
            "name": name if name else f"New {species}",
            "species": species,
            "rarity": rarity,
            "hunger": 50,
            "happiness": 100,
            "cleanliness": 100,
            "xp": 0,
            "stage": "Egg",
            "last_login": str(datetime.date(2000,1,1))
        }
        self.load_game()
        self.check_daily_xp()

    def check_evolution_common(self):
        if self.stats["xp"] >= 150 and self.stats["stage"] == "Egg":
            self.stats["stage"] = "Axolotl"
            return True
        elif self.stats["xp"] >= 1500 and self.stats["stage"] == "Axolotl":
            self.stats["stage"] = "Startol"
            return True
        return False

    def check_evolution_rare(self):
        if self.stats["xp"] >= 200 and self.stats["stage"] == "Egg":
            self.stats["stage"] = "Axolotl"
            return True
        elif self.stats["xp"] >= 1500 and self.stats["stage"] == "Axolotl":
            self.stats["stage"] = "Startol"
            return True
        return False

    def check_evolution_legend(self):
        if self.stats["xp"] >= 250 and self.stats["stage"] == "Egg":
            self.stats["stage"] = "Axolotl"
            return True
        elif self.stats["xp"] >= 1500 and self.stats["stage"] == "Axolotl":
            self.stats["stage"] = "Startol"
            return True
        return False

    def check_daily_xp(self):
        today = datetime.date.today()
        last_date = datetime.datetime.strptime(self.stats["last_login"], "%Y-%m-%d").date()

        if today > last_date:
            self.stats["xp"] += 50
            self.stats["last_login"] = str(today)
            self.save_game()

    def save_game(self):
        with open("save_data.json", "w") as f:
            json.dump(self.stats, f)

    def load_game(self):
        try:
            with open("save_data.json", "r") as f:
                self.stats = json.load(f)
        except FileNotFoundError:
            self.save_game()


    def feed(self, amount=20):
        self.stats["hunger"] = min(100, self.stats["hunger"] + amount)
        self.stats["xp"] = min(100, self.stats["xp"] + 10)

    def clean(self):
        self.stats["cleanliness"] = 100
        self.stats["happiness"] = min(100, self.stats["happiness"] + 10)
        self.stats["xp"] = min(100, self.stats["xp"] + 10)

    def update_vitals(self):
        now = pygame.time.get_ticks()

        if now - self.stats["last_update"] > 5000:
            self.stats["hunger"] = max(0, self.stats["hunger"] -2)
            self.stats["cleanliness"] = max(0, self.stats["cleanliness"] - 1)
            self.stats["happiness"] = max(0, self.stats["happiness"] - 1)
            self.stats["last_update"] = now