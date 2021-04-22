
import tkinter as tk
from .. import game_of_life # Causes build error 
# removed following commands from build.sh until error debugged:
#cd src/gui
#python3 gui.py
from tkinter import Canvas, Frame, Button
from tkinter import BOTH, W, NW, SUNKEN, TOP, X, FLAT, LEFT, N


class App(tk.Tk):
    def play(self, live_cells):
        # print("Started")
        if not live_cells:
            return
        else:

            self.live_cells = next_generation(live_cells)
            for row, col in live_cells:
                tile = self.tiles[row, col]
                self.canvas.itemconfigure(tile, fill="red")

            self.play(self.live_cells)

    def __init__(self, rows, columns, live_cells, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=1000, height=1000, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.rows = rows
        self.columns = columns
        self.tiles = {}
        self.canvas.bind("<Configure>", self.redraw)
        self.status = tk.Label(self, anchor="w")
        self.status.pack(side="bottom", fill="x")
        self.live_cells = live_cells
        button1 = Button(self, text="QUIT", command=self.quit, anchor=N)
        button1.configure(width=10, activebackground="white")
        button1_window = self.canvas.create_window(10, 10, anchor=NW, window=button1)
        button2 = Button(self, text="START",command=lambda : self.play(self.live_cells), anchor=N)

        button2.configure(width=10, activebackground="white")
        button2_window = self.canvas.create_window(100, 10, anchor=NW, window=button2)

    def redraw(self, event=None):
        self.canvas.delete("rect")
        cellwidth = int(self.canvas.winfo_width() / self.columns)
        cellheight = int(self.canvas.winfo_height() / self.columns)
        for column in range(self.columns):
            for row in range(self.rows):
                x1 = column * cellwidth
                y1 = row * cellheight
                x2 = x1 + cellwidth
                y2 = y1 + cellheight
                tile = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", tags="rect")
                self.tiles[row, column] = tile
                self.canvas.tag_bind(tile, "<1>", lambda event, row=row, column=column: self.clicked(row, column))



    def clicked(self, row, column):
        self.live_cells.append([row, column])
        tile = self.tiles[row, column]
        tile_color = self.canvas.itemcget(tile, "fill")
        new_color = "white" if tile_color == "red" else "red"
        self.canvas.itemconfigure(tile, fill=new_color)
        self.status.configure(text="you clicked on %s/%s" % (row, column))
        print(self.live_cells)

# 
# if __name__ == "__main__":
#     app = App(15, 15, [])
#     app.mainloop()