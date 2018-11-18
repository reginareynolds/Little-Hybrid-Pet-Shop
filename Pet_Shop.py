import pyxel
import random
import time
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
        self.submenu_select = [False, False, False]
        self.menu = [((7/30) * self.width, (1/3) * self.height, 0, 63), ((41/120)*self.width, (5/12) * self.height, 66, 38)]
        self.played = False
        self.dialogue = [0, 0, ""]
        self.dialogue_count = 0
        # self.npc_frame = [[0, 8, 0, 16, 0, 16, 16, 7], [0, 8, 0, 32, 0, 16, 16, 7], [0, 8, 0, 16, 0, 16, 16, 7]]
        self.npc_frame = [0, 8, 0, 16, 0, 16, 16, 7]

        pyxel.mouse(True)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.update_menu()

        self.update_game()

        # New game clicked, main menu inactive
        if self.submenu_select[0] and not self.menu_active:
            self.update_npc()
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
                    if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                        self.menu_active = False
                        self.submenu_select[i] = True
                        self.submenu_hover[i] = False

                # Cursor has stopped hovering over a menu option
                if(self.submenu_hover[i]):
                    # Deactivate hover effect
                    if(pyxel.mouse_x>(x+diff) or pyxel.mouse_x<x or pyxel.mouse_y > (y+6) or pyxel.mouse_y < y):
                        self.submenu[i][1] = self.submenu[i][1] + 2
                        self.submenu_hover[i] = False

                    # Play de-hover sound?

    def update_game(self):
        pass



    def update_npc(self):
        # Has user hit continue?
        # TODO: Check for key release, this keeps incrementing for the duration that spacebar is held down
        if(pyxel.btn(pyxel.KEY_SPACE)):
            self.listened = True
            self.dialogue_count = self.dialogue_count + 1


        # play voice sound
        if(self.played is False):
            # 120 speed is 1 second per tone, figure out a way to time the sound lengths based on their speed
            start = time.time()
            print("start")
            pyxel.play(0, 4)
            end = time.time()
            print("end")
            print(end-start)
            self.played = True

        if(self.listened is False):
            self.dialogue = [[5, 56, "Today is your first day\nrunning the pet shop."], [5, 56, "I'll go over some of the responsibilities."]]
            # I'm going to go over some of the responsibilities really quickly before I leave you to it.
            # Click a pet to see more information about it.
            # Click two pets to mate them.
            # See what crazy combos you can come up with!
            # play animation
            if (self.test < self.animRate):
                self.npc_frame = [0, 8, 0, 16, 0, 16, 16, 7]
                self.test = self.test + 1
            elif (self.test < (2 * self.animRate)):
                self.npc_frame = [0, 8, 0, 32, 0, 16, 16, 7]
                self.test = self.test + 1
            elif (self.test == (2 * self.animRate)):
                self.npc_frame = [0, 8, 0, 16, 0, 16, 16, 7]
                # self.test = 0


    def draw(self):
        # Clear screen
        pyxel.cls(13)

        # Main menu
        if(self.menu_active):

            # Title
            for x, y, imgX, imgX2 in self.menu:
                pyxel.blt(x, y, 0, imgX, 24, imgX2, 6, 0)

            # Sub menu
                for x, y, message in self.submenu:
                    pyxel.text(x, y, message, 7)
        else:
            # Menu is closed, redirect based on button selection
            if (self.submenu_select[0]):  # New game
                x, y, img, u, v, w, h, col = self.npc_frame

                pyxel.blt(x, y, img, u, v, w, h, col)

                x, y, message = self.dialogue[self.dialogue_count]
                pyxel.text(x, y, message, 7)


            elif (self.submenu_hover[1]):  # Save game
                 pass
            elif (self.submenu_hover[2]):  # Load game
                pass

            # # reset hovering
            # for i in range(len(self.submenu_hover)):
            #     self.submenu_hover[i] = False

        # else:
        #     pyxel.line(self.width / 2, 0, self.width / 2, self.height, 0)

        print(pyxel.mouse_x, pyxel.mouse_y)




Game()
