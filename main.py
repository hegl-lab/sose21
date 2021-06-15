#!/usr/bin/env python
# -*- coding: utf-8 -*-

from canvas import Canvas
import tkinter

class Window:
    def __init__(self):
        self.top = tkinter.Tk()
        self.top.title("Hyperbolic tilings")
        self.canvas = Canvas(self.top)
        self.top.bind("<Button-1>", self.mouse_click)
    
    def mouse_click(self, event):
        self.canvas.mouse_click(event)
        
    def run(self):
        self.top.mainloop()

if __name__ == "__main__":
    main_window = Window()
    z1=0.3+0.1j
    z2=-0.1-0.2j
    main_window.canvas.draw_H2_segment(z1, z2, "green")
    z1=0.5+0.5j
    z2=-0.5-0.5j
    main_window.canvas.draw_H2_segment(z1, z2, "orange")
    main_window.run()