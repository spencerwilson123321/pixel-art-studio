#!/usr/bin/env python3
import tkinter
from tkinter import colorchooser

import PIL.Image


def hex_string_to_rgb_tuple(hexstring):
    r = int("0x"+hexstring[1:3], 0)
    g = int("0x"+hexstring[3:5], 0)
    b = int("0x"+hexstring[5:7], 0)
    rgb = (r, g, b)
    return rgb


class Pixel:
    def __init__(self, root, app, x, y):
        self.root = root
        self.app = app
        self.color = "#ffffff"
        self.width = 20
        self.height = 20
        self.position = (x, y)
        self.frame = tkinter.Frame(self.root, width=self.width, height=self.height, background=self.color,
                                   borderwidth=1, relief="solid")
        self.frame.bind("<Button-1>", self.onclick)
        self.display()

    def onclick(self, event):
        # Ask the app which color is selected.
        self.color = self.app.selected_color
        if self.color is None:
            self.color = "#ffffff"
        self.display()

    def display(self):
        self.frame.configure(background=self.color)
        self.frame.grid(row=self.position[1], column=self.position[0])


class PixelArtStudio:

    def __init__(self):
        # Main Window
        self.window = tkinter.Tk()
        self.window.title("Pixel Art Studio")
        self.window.minsize(640, 480)

        # Pixel Grid
        self.pixels = []
        self.grid_width = 16
        self.grid_height = 16
        self.grid_frame = tkinter.Frame(self.window)
        self.default_color = "#ffffff"
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                self.pixels.append(Pixel(root=self.grid_frame, app=self, x=x, y=y))
        self.grid_frame.pack()

        # Color Chooser
        self.selected_color = "#ffffff"
        self.color_button = tkinter.Button(self.window, text="Choose a color")
        self.color_button.bind("<Button-1>", self.open_color_chooser)
        self.color_button.pack()

        # Save Button
        self.save_button = tkinter.Button(self.window, text="Save to PNG")
        self.save_button.bind("<Button-1>", self.save_to_png)
        self.save_button.pack()

    def save_to_png(self, event):
        image = PIL.Image.new("RGB", (16, 16), "white")
        for i, pixel in enumerate(self.pixels):
            image.putpixel(pixel.position, hex_string_to_rgb_tuple(pixel.color))
        image.save("sprite.png")

    def open_color_chooser(self, event):
        _, new_color = colorchooser.askcolor(title="Choose a color")
        if new_color is not None:
            self.selected_color = new_color

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    art_studio = PixelArtStudio()
    art_studio.run()
