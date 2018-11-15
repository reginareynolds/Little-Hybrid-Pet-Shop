import pyxel
from pyxel import constants
import random
from pyxel import editor

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
        self.width = 120
        self.height = 90

        pyxel.init(self.width, self.height, caption="Little Hybrid Pet Shop", scale=10)

        pyxel.load("Assets/pet_shop.pyxel")

        self.menu_active = True
        self.test = 0
        self.animRate = 4
        self.listened = False
        self.submenu = [[(9/24)*self.width, (17/30)*self.height, "New Game"], [(53/120)*self.width, (2/3)*self.height, "Save"], [(53/120)*self.width, (23/30)*self.height, "Load"]]
        self.submenu_hover = [False, False, False]
        self.menu = [((7/30) * self.width, (1/3) * self.height, 0, 63), ((41/120)*self.width, (5/12) * self.height, 66, 38)]
        pyxel.mouse(True)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.update_menu()

    #     self.update_npc()
    #

    # Implement hover effect for menu buttons
    def update_menu(self):
        if(self.menu_active):  # Menu is open
            for i in range(3):
                x = self.submenu[i][0]
                y = self.submenu[i][1]
                diff = 14 if i else 30

                # Cursor is hovering over a menu option
                if((x <= pyxel.mouse_x <= (x+diff)) and (y <= pyxel.mouse_y <= (y+4))):
                    if not self.submenu_hover[i]:
                        # Activate hover effect
                        self.submenu[i][1] = self.submenu[i][1] - 2
                        self.submenu_hover[i] = True

                        # Play hover sound
                        pyxel.play(0, 3)

                    # User has clicked menu option
                    if pyxel.btnp(constants.MOUSE_LEFT_BUTTON):
                        self.menu_active = False

                # Cursor has stopped hovering over a menu option
                if(self.submenu_hover[i]):
                    # Deactivate hover effect
                    if(pyxel.mouse_x>(x+diff) or pyxel.mouse_x<x or pyxel.mouse_y > (y+6) or pyxel.mouse_y < y):
                        self.submenu[i][1] = self.submenu[i][1] + 2
                        self.submenu_hover[i] = False

                    # Play de-hover sound?

        # Redirect based on button selection

    def update_npc(self):
        if(pyxel.btn(pyxel.KEY_SPACE)):
            self.listened = True

    def draw(self):
        pyxel.cls(13)

        # Main menu
        if(self.menu_active):
            # Title
            for x, y, imgX, imgX2 in self.menu:
                pyxel.blt(x, y, 0, imgX, 24, imgX2, 6, 0)

            # Sub menu
                for x, y, message in self.submenu:
                    pyxel.text(x, y, message, 7)
        # else:
        #     pyxel.line(self.width / 2, 0, self.width / 2, self.height, 0)

        # print(pyxel.mouse_x, pyxel.mouse_y)

        # if(self.test < self.animRate):
        #     pyxel.blt(0, 8, 0, 16, 0, 16, 16, 7)
        #     self.test = self.test + 1
        # elif(self.test < (2 * self.animRate)):
        #     pyxel.blt(0, 8, 0, 32, 0, 16, 16, 7)
        #     self.test = self.test + 1
        # elif(self.test == (2 * self.animRate)):
        #     pyxel.blt(0, 8, 0, 16, 0, 16, 16, 7)
        #     self.test = 0


Game()
