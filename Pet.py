import random
import time
from Breeds import *

# TODO:
#  Characteristics,
#  Name

# GLOBAL VARIABLES:
# Possible personalities
personalities = ['Adamant', 'Modest', 'Jolly', 'Timid', 'Impish', 'Bold', 'Careful', 'Calm', 'Lax', 'Gentle', 'Mild',
                 'Lonely', 'Rash', 'Naughty', 'Brave', 'Quiet', 'Hardy', 'Bashful', 'Docile', 'Quirky', 'Serious']

# Possible female names
f_names = ['Bella', 'Lucy', 'Molly', 'Daisy', 'Maggie', 'Sophie', 'Sadie', 'Chloe', 'Bailey', 'Lola', 'Zoe',
           'Abby', 'Ginger', 'Roxy', 'Gracie', 'Coco', 'Sasha', 'Lily', 'Angel', 'Princess', 'Emma', 'Annie',
           'Rosie', 'Ruby', 'Lady', 'Missy', 'Lilly', 'Mia', 'Katie', 'Zoey', 'Madison', 'Stella', 'Penny',
           'Belle', 'Casey', 'Samantha', 'Holly', 'Lexi', 'Lulu', 'Brandy', 'Jasmine', 'Shelby', 'Sandy', 'Roxie',
           'Pepper', 'Heidi', 'Luna', 'Dixie', 'Honey', 'Dakota']

# Possible male names
m_names = ['Bailey', 'Max', 'Charlie', 'Buddy', 'Rocky', 'Jake', 'Jack', 'Toby', 'Cody', 'Buster', 'Duke', 'Cooper',
              'Riley', 'Harley', 'Bear', 'Tucker', 'Murphy', 'Lucky', 'Oliver', 'Sam', 'Oscar', 'Teddy', 'Winston',
              'Sammy', 'Rusty', 'Shadow', 'Gizmo', 'Bentley', 'Zeus', 'Jackson', 'Baxter', 'Bandit', 'Gus', 'Samson',
              'Milo', 'Rudy', 'Louie', 'Hunter', 'Casey', 'Rocco', 'Sparky', 'Joey', 'Bruno', 'Beau', 'Dakota',
              'Maximus', 'Romeo', 'Boomer', 'Luke', 'Henry']

# Base breed possibilities
bounce = Bouncer()
crawl = Crawler()
hop = Hopper()
swim = Swimmer()

base_breeds = [bounce, crawl, hop, swim]

class Pet:
    def __init__(self, mother=None, father=None):
        self.age = None
        self.sex = self.female_or_male()

        # Initialize variables
        self.lineage = []
        self.color = []  # [R, G, B] format
        self.personality = ""  # String format
        self.breed = ""
        self.characteristics = ""  # Size?
        self.name = ""

        # Create pet
        self.characterize(mother, father)

    # Determine family tree
    def characterize(self, mom, dad):
        # CASE 1: Pet is offspring of owned pets
        if(mom and dad):  # Known parents, base values on heritage
            # Set age
            self.age = 0  # Newborn

            # Add parents to family tree
            self.lineage.append(mom)
            self.lineage.append(dad)

            # Determine color
            self.set_color()

            # Determine personality
            self.set_personality()

            # Determine breed
            self.set_breed()

            # Determine characteristics
            # TODO: Define and append characteristics

            # Determine name
            # TODO: Prompt for name
        # CASE 2: Pet is new purchase
        else:  # Unknown parents, create random heritage
            # Set age
            self.age = random.uniform(0, 10)  # Randomize age

            # Add random parents to family tree
            self.randomize_parents()

            # TODO: Randomize heritage
            # TODO: Randomize name from list of possible names

    # Determine sex of pet
    @staticmethod
    def female_or_male():
        if(random.uniform(0.0, 1.0) < 0.5):
            return("XX")  # Female
        else:
            return("XY")  # Male

    # Average R, G, B values of parents and append to color container
    def set_color(self):
        i = 0  # Loop variable

        while(i < 3):
            self.color.append((self.lineage[0].color[i] + self.lineage[1].color[i])//2)
            i = i + 1

    # Randomly select personality from weighted array of possible temperaments
    def set_personality(self):
        # 21 total personalities
        # 2 parent personalities
        # 19 (parent personalities are different) or 20 (parent personalities are identical) other personalities
        # Each parent personality chance = 1/10
        # Other personality chance = (8/10)*(1/other personalities)

        # Initialize probability array
        chances = []

        # Determine personality weights
        if(self.lineage[0].temperament == self.lineage[1].temperament):  # Parent temperaments are identical
            parent_chance = 2/10  # 20% chance to have same temperament as parent
            other_chance = (8/10) * (1/20)  # 80% chance to have different temperament than parent; 4% chance for a given different temperament
        else:  # Parent temperaments are different
            parent_chance = 1/10  # 10% chance to have same temperament as a given parent
            other_chance = (8/10) * (1/19)  # 80% chance to have different temperament than parent; 4.2% chance for a given different temperament

        # Create array of personality probabilities with preference given to parental temperaments
        for temperament in personalities:
            if(temperament == (self.lineage[0].temperament or self.lineage[1].temperament)):  # Matches parental temperament
                chances.append(parent_chance)
            else:  # Matches neither parent's temperament
                chances.append(other_chance)

        # Select temperament
        self.personality = random.choices(personalities, weights=chances)

    # Randomly select breed from parents' breeds
    def set_breed(self):
        if(random.uniform(0.0, 1.0) < 0.5):
            self.breed = self.lineage[0].breed  # Mother's breed
        else:
            self.breed = self.lineage[1].breed  # Father's breed

    def set_characteristics(self):
        pass
        # TODO: Create characteristic set function

    # Create random heritage
    def randomize_parents(self):
        self.lineage
    # Include mutation possibility
    # TODO: Create mutation function
