""" created 05/09/2016
author: marcello
version: 0.1

Graphic user interface using tkinter.
"""

import tkinter as tk
import PIL.Image
import PIL.ImageTk
from constants import GAME_NAME
from constants import BLACK, WHITE
from constants import IMAGES_PATH
import os

# functions

def get_image_path(img_name):
    return os.path.join(IMAGES_PATH, img_name)


class Gui():
    """Draws the GUI."""

    def __init__(self, parent):

        # menues

        self.menu = tk.Menu(parent)
        self.menu_file = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='File', menu=self.menu_file)
        self.menu_file.add_command(label='Exit', command=parent.quit)
        parent.config(menu=self.menu)

        # canvas

        self.map = tk.Canvas(parent, width=640, height= 400, bg=BLACK)
        self.map.pack(expand=tk.YES, fill=tk.BOTH)

    def draw_map(self, engine):
        """Paint the GUI map canvas with the objects in engine."""



def main():
    root = tk.Tk()
    root.title(GAME_NAME.title())
    gui = Gui(root)
    root.mainloop()


if __name__ == '__main__': main()