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
        self.width = 120
        self.height = 90

        pyxel.init(self.width, self.height, caption="Little Hybrid Pet Shop", scale=10)

        pyxel.load("Assets/pet_shop.pyxel")
        # pyxel.image(0).load(0, 0, "Assets/pet_shop.pyxel")
        # self.x = 0
        self.menu = True
        self.test = 0
        self.animRate = 4
        self.listened = False
        self.submenu = [[(45/120)*self.width, (17/30)*self.height, "New Game"], [(53/120)*self.width, (2/3)*self.height, "Save"], [(53/120)*self.width, (23/30)*self.height, "Load"]]
        self.submenu_hover = [False, False, False]
        self.menu = [((28/120) * self.width, (1/3) * self.height, 0, 63), ((41/120)*self.width, (5/12) * self.height, 66, 38)]
        pyxel.mouse(True)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.update_menu()
        # for i, v in enumerate(self.submenu):
        #     self.submenu[i]= self.update_menu(*v)
    #     self.update_npc()
    #

    def update_menu(self):
        # Implement hover effect for menu buttons
        if(self.menu): # Menu is open

            for i in range(3):
                x = self.submenu[i][0]
                y = self.submenu[i][1]
                if(i==0):
                    diff = 30
                else:
                    diff = 14

                if((x <= pyxel.mouse_x <= (x+diff)) and (y <= pyxel.mouse_y <= (y+4)) and not self.submenu_hover[i]):
                    self.submenu[i][1] = self.submenu[i][1] - 2
                    self.submenu_hover[i] = True

                # # Button has been hovered over
                # if(self.submenu_hover[0]):
                #     if(pyxel.mouse_x>75 or pyxel.mouse_x<45 or pyxel.mouse_y>(self.submenu[0][1]+4))
                # # return(x, y, message)

        # Redirect based on button selection

    def update_npc(self):
        if(pyxel.btn(pyxel.KEY_SPACE)):
            self.listened = True



    def draw(self):
        pyxel.cls(13)


        # Main menu
        if(True):
            # Title
            for x, y, imgX, imgX2 in self.menu:
                pyxel.blt(x, y, 0, imgX, 24, imgX2, 6, 0)

            # Sub menu
                for x, y, message in self.submenu:
                    pyxel.text(x, y, message, 7)

        pyxel.line(self.width/2, 0, self.width/2, self.height, 0)
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

        # pyxel.rect(self.x, 0, self.x + 7, 7, 9)

Game()