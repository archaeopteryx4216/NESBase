import tkinter as tk
from paletteselect import PaletteSelect
from bgselect import BGSelect

class PainterPalette(tk.Frame):

    def __init__(self, main=None, selected_color=None, col_bg=None, col_1=None, col_2=None, col_3=None):
        if (not selected_color or not isinstance(selected_color, tk.IntVar) or
            not col_bg or not isinstance(col_bg, tk.StringVar) or
            not col_1 or not isinstance(col_1, tk.StringVar) or
            not col_2 or not isinstance(col_2, tk.StringVar) or
            not col_3 or not isinstance(col_3, tk.StringVar)):
            raise(ValueError("PainterPalette needs to be initialized with an integer var to hold the selected color as well as four string vars to hold the available colors."))
        tk.Frame.__init__(self, main)
        self._selected_color = selected_color
        self._selected_color.set(0)
        self._bg_color = col_bg
        self._bg_color.set("#000000")
        self._pal_color = [col_1, col_2, col_3]
        for col in self._pal_color:
            col.set("#000000")
        tk.Label(self, text="Select Color").grid(row=0, column=0, columnspan=2)
        bg_rbtn = tk.Radiobutton(self, variable=self._selected_color, value=0)
        bg_rbtn.grid(row=1, column=0)
        BGSelect(self, self._bg_color).grid(row=1, column=1, sticky=tk.E)
        pal_rbtn = []
        pal_rbtn.append(tk.Radiobutton(self, variable=self._selected_color, value=1))
        pal_rbtn[-1].grid(row=2, column=0)
        pal_rbtn.append(tk.Radiobutton(self, variable=self._selected_color, value=2))
        pal_rbtn[-1].grid(row=3, column=0)
        pal_rbtn.append(tk.Radiobutton(self, variable=self._selected_color, value=3))
        pal_rbtn[-1].grid(row=4, column=0)
        PaletteSelect(self, self._pal_color[0], self._pal_color[1], self._pal_color[2]).grid(row=2, column=1, rowspan=3, sticky=tk.E)

if __name__ == "__main__":
    def test():
        root = tk.Tk()
        selected_color = tk.IntVar()
        colors = [tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()]
        PainterPalette(root, selected_color, colors[0], colors[1], colors[2], colors[3]).pack()
        root.mainloop()
    test()