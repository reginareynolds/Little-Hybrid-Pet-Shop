# Different possible breeds, organized into classes

# Imported libraries and modules
import random


# Pick size from allowable range
def set_size(options):
    choice = random.randint(0, (len(options)-1))

    return(options[choice])


# Pick weight from allowable range
def set_weight(options):
    return(random.uniform(options[0], options[1]))


class Bouncer:
    def __init__(self):
        # Create initial ranges
        self.size = ["Small", "Medium"]
        self.weight = [5.0, 30.0]

        # Constant breed values
        # self.shape = TODO: pixel shape coordinates
        # self.sound = TODO: creature sound
        self.base_value = 50  # TODO: affected by heritage? purebred could be more valuable

    def set_values(self):
        self.size = set_size(self.size)
        self.weight = set_weight(self.weight)


class Crawler:
    def __init__(self):
        self.size = ["Small", "Medium", "Large"]
        self.weight = [5.0, 90.0]

        # Constant breed values
        # self.shape =
        # self.sound =
        self.base_value = 10

    def set_values(self):
        self.size = set_size(self.size)
        self.weight = set_weight(self.weight)


class Hopper:
    def __init__(self):
        self.size = ["Medium", "Large"]
        self.weight = [30.0, 90.0]

        # Constant breed values
        # self.shape =
        # self.sound =
        self.base_value = 20

    def set_values(self):
        self.size = set_size(self.size)
        self.weight = set_weight(self.weight)


class Swimmer:
    def __init__(self):
        self.size = ["Small", "Medium", "Large"]
        self.weight = [5.0, 90.0]

        # Constant breed values
        # self.shape =
        # self.sound =
        self.base_value = 35

    def set_values(self):
        self.size = set_size(self.size)
        self.weight = set_weight(self.weight)

# TODO: Characteristic inherit function?
# TODO: Add breed abilities
