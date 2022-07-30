import tkinter as tk
from paletteselect import PaletteSelect
from bgselect import BGSelect

class PainterPalette(tk.Frame):
    def _set_selected_color(self, rbtn, color_var):
        self._selected_color.set(color_var.get())
        rbtn.select()

    def __init__(self, main=None, selected_color=None):
        if not selected_color or not isinstance(selected_color, tk.StringVar):
            raise(ValueError("PainterPalette needs to be initialized with a string var to hold the selected color."))
        tk.Frame.__init__(self, main)
        self._rbtn_selection = tk.IntVar(self)
        self._selected_color = selected_color
        self._bg_color = tk.StringVar(self, "#000000")
        self._selected_color.set(self._bg_color.get())
        self._pal_color = [tk.StringVar(self, "#000000"), tk.StringVar(self, "#000000"), tk.StringVar(self, "#000000")]
        tk.Label(self, text="Select Color").grid(row=0, column=0, columnspan=2)
        bg_rbtn = tk.Radiobutton(self, variable=self._rbtn_selection, value=0)
        bg_rbtn.configure(command=lambda rbtn=bg_rbtn, cvar=self._bg_color: self._set_selected_color(rbtn, cvar))
        bg_rbtn.grid(row=1, column=0)
        BGSelect(self, self._bg_color).grid(row=1, column=1, sticky=tk.E)
        pal_rbtn = []
        pal_rbtn.append(tk.Radiobutton(self, variable=self._rbtn_selection, value=1))
        pal_rbtn[-1].configure(command=lambda rbtn=pal_rbtn[-1], cvar=self._pal_color[0]: self._set_selected_color(rbtn, cvar))
        pal_rbtn[-1].grid(row=2, column=0)
        pal_rbtn.append(tk.Radiobutton(self, variable=self._rbtn_selection, value=2))
        pal_rbtn[-1].configure(command=lambda rbtn=pal_rbtn[-1], cvar=self._pal_color[1]: self._set_selected_color(rbtn, cvar))
        pal_rbtn[-1].grid(row=3, column=0)
        pal_rbtn.append(tk.Radiobutton(self, variable=self._rbtn_selection, value=3))
        pal_rbtn[-1].configure(command=lambda rbtn=pal_rbtn[-1], cvar=self._pal_color[2]: self._set_selected_color(rbtn, cvar))
        pal_rbtn[-1].grid(row=4, column=0)
        PaletteSelect(self, self._pal_color[0], self._pal_color[1], self._pal_color[2]).grid(row=2, column=1, rowspan=3, sticky=tk.E)

if __name__ == "__main__":
    def test():
        root = tk.Tk()
        selected_color = tk.StringVar()
        PainterPalette(root, selected_color).pack()
        root.mainloop()
    test()