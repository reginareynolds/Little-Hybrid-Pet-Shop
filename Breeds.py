# Different possible breeds, organized into classes
import random


# Pick size from allowable range
def set_size(options):
    choice = random.randint(0, (len(options)-1))

    return(options[choice])


class Bouncer:
    def __init__(self):
        # Create initial ranges
        self.size = ["Small", "Medium"]
        self.weight = [5.0, 30.0]
        # self.abilities =
        # self.shape = TODO: pixel shape coordinates
        # self.sound = TODO: creature sound
        self.base_value = 0  # TODO: affected by heritage? purebred could be more valuable

    def characterize(self):
        self.size = set_size(self.size)



class Crawler:
    def __init__(self):
        self.size = ["Small", "Medium", "Large"]
        self.weight = [5.0, 90.0]
        # self.abilities =
        # self.shape =
        # self.sound =
        self.base_value = 0


class Hopper:
    def __init__(self):
        self.size = ["Medium", "Large"]
        self.weight = [30.0, 90.0]
        # self.abilities =
        # self.shape =
        # self.sound =
        self.base_value = 0


class Swimmer:
    def __init__(self):
        self.size = ["Small", "Medium", "Large"]
        self.weight = [5.0, 90.0]
        # self.abilities =
        # self.shape =
        # self.sound =
        self.base_value = 0

# TODO: Characteristic inherit function?
