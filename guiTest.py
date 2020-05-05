#   This file contains the tkinter setup processes as well as the classes for
#   the Main Menu and crop_img screens

import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3
from DEFAULTS import SCREEN_DIMS
from global_variables import BUTTON_HEIGHT, BUTTON_WIDTH

from Button_Functions import imgTestFns, mainMenuFns
UPDATE_RATE = 1000


#   parent container for all the frames that represent the smartNode app
class SmartnodeGUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window_width = round(SCREEN_DIMS['width'])
        window_length = round(SCREEN_DIMS['height'])

        geometry_dimensions = "%dx%d+%d+%d" % (window_width, window_length, 0, 0)

        self.geometry(geometry_dimensions)

        self.title_font = tkfont.Font(family='Helvetica', size=36, weight="bold", slant="italic")
        self.buttonFont = tkfont.Font(family='Helvetica', size=-50, weight="bold")
        #self.buttonFont.metrics(linespace=0)

        # the container is where we'll stack a bunch of frames on top of each other
        # the one we want visible will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # list of all frame classes
        self.frames = {}
        frame_classes = (
            MainMenu,
            imgTest,
        )

        for F in frame_classes:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        #  for returning to previous frame from frames that are accessed from multiple other frames
        self.return_frame = "MainMenu"
        self.show_frame("MainMenu")

    #   shows
    def show_frame(self, page_name):
        # Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()

    def get_frame(self, page_name):
        return self.frames[page_name]

    def set_return_frame(self, page_name):
        self.return_frame = page_name


class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="MainMenu", font=controller.title_font)
        label.pack(side="top", fill="both", pady=1)

        #   set of commands to be assigned to each button
        main_btn_cmds = {
            'take_img': lambda: (
                print("attempting to take picture from button"),
                mainMenuFns['takeSrc'],
                #controller.set_return_frame("MainMenu"),
            ),

            'img_test': lambda: (
                print("switching to imgTest Frame"),
                controller.set_return_frame("MainMenu"),
                controller.show_frame("imgTest")
            ),

            'btn_3': lambda: (
                print("This button does nothing!"),
                #controller.set_return_frame("MainMenu"),
                '''controller.show_frame("crop_img")'''
            ),

            'quit': lambda: (
                controller.destroy()
            ),
        }

        #   actual button objecs
        main_btns = {
            'take_img': tk.Button(self, text="TAKE PICTURE"),
            'img_test': tk.Button(self, text="IMG TESTING"),
            'btn_3': tk.Button(self, text="<NULL>"),
            'quit': tk.Button(self, text="QUIT"),
        }

        #   iterate through buttons and configure them accordingly
        for btn in main_btns:
            main_btns[btn].configure(bg="#FF0000", relief="raised", font=self.controller.buttonFont)
            main_btns[btn].configure(padx=0, pady=0)
            main_btns[btn].configure(height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
            main_btns[btn].configure(command=main_btn_cmds[btn])
            main_btns[btn].pack(side="top", fill="both")


#   testing menu for demo of image functions
class imgTest(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="ImageTest", font=controller.title_font)
        label.pack(side="top", fill="both", pady=1)

        #   set of commands to be assigned to each button
        imgTest_cmds = {
            'show_img': lambda: (
                print("attempting to show image"),
                imgTestFns['showImg'],
                #controller.set_return_frame("imgTest"),
            ),

            'add_crop': lambda: (
                print("attempting to add crop"),
                imgTestFns['addCrop'],
                #controller.set_return_frame("imgTest"),
            ),

            'crop_img': lambda: (
                imgTestFns['cropImg'],
                #controller.set_return_frame("imgTest"),
                '''controller.show_frame("crop_img")'''
            ),

            'back': lambda: (
                controller.show_frame("MainMenu")
            ),
        }

        #   actual button objecs
        imgTest_btns = {
            'show_img': tk.Button(self, text="SHOW IMG"),
            'add_crop': tk.Button(self, text="ADD CROP"),
            'crop_img': tk.Button(self, text="CROP IMG"),
            'back': tk.Button(self, text="BACK"),
        }

        #   iterate through buttons and configure them accordingly
        for btn in imgTest_btns:
            imgTest_btns[btn].configure(bg="#FF0000", relief="raised", font=self.controller.buttonFont)
            imgTest_btns[btn].configure(height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
            imgTest_btns[btn].configure(command=imgTest_cmds[btn])
            imgTest_btns[btn].pack(side="top", fill="both")
