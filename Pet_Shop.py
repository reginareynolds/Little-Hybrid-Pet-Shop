import pyxel
import random
from pyxel import editor
# from screeninfo import get_monitors
#
# for m in get_monitors():
#     print(str(m))

# pyxel.init(160, 120)
#
#
# def update():
#     if pyxel.btnp(pyxel.KEY_Q):
#         pyxel.quit()
#
#
# def draw():
#     pyxel.cls(0)
#     pyxel.rect(10, 10, 20, 20, 11)
#
# #
# class Shop:
#     def __init__(self):

# class Pet:
#     color = ""
#     characteristics = ""
#     personality = ""
#     lineage = []
#     breed = ""
#     sex = ""
#
#     def characterize(self):
#         # Determine sex of pet
#         if(random.uniform(0.0, 1.0) <  0.5):
#             self.sex = "XY"
#         else:
#             self.sex = "XX"
#
#         # Determine family tree
#         # if(lineage[0]==)


class Game:
    def __init__(self):
        pyxel.init(40, 30, caption= "Little Hybrid Pet Shop")

        pyxel.load("Assets/pet_shop.pyxel")
        # pyxel.image(0).load(0, 0, "Assets/pet_shop.pyxel")
        # self.x = 0
        self.test = 0


        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    #     self.update_npc()
    #
    # def update_npc(self):



    def draw(self):
        pyxel.cls(7)

        if(self.test <10):
            pyxel.blt(0, 8, 0, 16, 0, 16, 16, 7)
            self.test = self.test + 1
        elif(self.test < 20):
            pyxel.blt(0, 8, 0, 32, 0, 16, 16, 7)
            self.test = self.test + 1
        elif(self.test == 20):
            pyxel.blt(0, 8, 0, 16, 0, 16, 16, 7)
            self.test = 0

        # pyxel.rect(self.x, 0, self.x + 7, 7, 9)

Game()