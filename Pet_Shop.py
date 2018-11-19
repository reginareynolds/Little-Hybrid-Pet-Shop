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
        self.animLoop = 0
        self.animRate = 4
        self.submenu = [[(9/24), (17/30), "New Game"], [(53/120), (2/3), "Save"], [(53/120), (23/30), "Load"]]
        self.submenu_hover = [False, False, False]
        self.submenu_select = [False, False, False]
        self.menu = [((7/30), (1/3), 0, 63), ((41/120), (5/12), 66, 38)]
        self.played = False
        self.start = 1
        self.listened = False
        self.dialogue = ["Today is your first day\nrunning the pet shop.",
                         "I'll go over some of the\nresponsibilities.",
                         "Click a pet to see more\ninformation about it.",
                         "Click two pets to mate them.",
                         "See what crazy combos\nyou can come up with!",
                         "Okay, I'll leave you to it!"]
        self.dialogue_count = 0
        self.npc_frame = [0, 8, 0, 16, 0, 16, 16, 7]

        pyxel.mouse(True)

        # Play theme song
        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)

        # TODO: Keep theme song from conflicting with sound effects like menu hover

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.update_menu()

        self.update_game()

        # New game clicked, main menu inactive
        if self.submenu_select[0] and not self.menu_active:
            self.update_npc()

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
                    if(pyxel.mouse_x > (x+diff) or pyxel.mouse_x < x or pyxel.mouse_y > (y+6) or pyxel.mouse_y < y):
                        self.submenu[i][1] = self.submenu[i][1] + 2
                        self.submenu_hover[i] = False

    def update_game(self):
        pass

    def update_npc(self):
        # Has user hit continue?
        if(pyxel.btnr(pyxel.KEY_SPACE)):
            # Set dialogue
            self.dialogue_count = self.dialogue_count + 1

            # Reset event flags
            self.played = False
            self.listened = False
            self.animLoop = 0

            # Stop playing dialogue sound to prevent possible overlap
            pyxel.stop(0)

        # play voice sound
        if(self.played is False):
            # Duration of one tone (s) = rating/120
            pyxel.play(0, 4)
            self.start = time.time()
            self.played = True

        # play animation
        if(self.listened is False):
            # Sound has finished, stop animating
            if((time.time() - self.start) >= (77/60)):
                self.npc_frame = [0, 8, 0, 16, 0, 16, 16, 7]
                self.listened = True

            else:  # Sound is still playing, continue animating
                if (self.animLoop < self.animRate):
                    self.npc_frame = [0, 8, 0, 16, 0, 16, 16, 7]
                    self.animLoop = self.animLoop + 1
                elif ((self.animLoop) < (2 * self.animRate)):
                    self.npc_frame = [0, 8, 0, 32, 0, 16, 16, 7]
                    self.animLoop = self.animLoop + 1
                elif (self.animLoop == ((2 * self.animRate))):
                    self.npc_frame = [0, 8, 0, 16, 0, 16, 16, 7]
                    self.animLoop = 0

    def draw(self):
        # Clear screen
        pyxel.cls(6)

        # Main menu
        if(self.menu_active):
            # Title
            for x, y, imgX, imgX2 in self.menu:
                pyxel.blt(x * self.width, y * self.height, 0, imgX, 24, imgX2, 6, 0)

            # Sub menu
            for x, y, message in self.submenu:
                pyxel.text(x * self.width, y * self.height, message, 7)
        else:
            # Menu is closed, redirect based on button selection
            if (self.submenu_select[0]):  # New game
                x, y, img, u, v, w, h, col = self.npc_frame

                # draw NPC
                pyxel.blt(x, y, img, u, v, w, h, col)

                # draw dialogue
                pyxel.text(5, 56, self.dialogue[self.dialogue_count], 7)

            elif (self.submenu_hover[1]):  # Save game
                pass
            elif (self.submenu_hover[2]):  # Load game
                pass

            # # reset hovering
            # for i in range(len(self.submenu_hover)):
            #     self.submenu_hover[i] = False

        # else:
        #     pyxel.line(self.width / 2, 0, self.width / 2, self.height, 0)

        # print(pyxel.mouse_x, pyxel.mouse_y)




Game()
