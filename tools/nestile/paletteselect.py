import tkinter as tk
from colorselect import ColorSelect

class PaletteSelect(tk.Frame):
    def _setcolor(self, cvar, csel):
        color = ColorSelect(self).selection
        csel.configure(bg=color)
        cvar.set(color)

    def __init__(self, main=None, cvar_1=None, cvar_2=None, cvar_3=None):
        tk.Frame.__init__(self, main)
        if (not cvar_1 or not isinstance(cvar_1, tk.StringVar) or
            not cvar_2 or not isinstance(cvar_2, tk.StringVar) or
            not cvar_3 or not isinstance(cvar_3, tk.StringVar)):
            raise(ValueError("PaletteSelect widget must be created with a StringVar to hold each color of the palette."))
        # Save references to each stringvar
        self._cvar_1 = cvar_1
        self._cvar_2 = cvar_2
        self._cvar_3 = cvar_3
        # Pack ColorSelect buttons onto the frame
        tk.Label(self, text="Color 1").grid(row=0, column=0)
        self._csel_1 = tk.Button(self, width="10")
        self._csel_1.configure(command=lambda cvar=self._cvar_1, csel=self._csel_1: self._setcolor(cvar, csel))
        self._csel_1.grid(row=0, column=1)
        tk.Label(self, text="Color 2").grid(row=1, column=0)
        self._csel_2 = tk.Button(self, width="10")
        self._csel_2.configure(command=lambda cvar=self._cvar_2, csel=self._csel_2: self._setcolor(cvar, csel))
        self._csel_2.grid(row=1, column=1)
        tk.Label(self, text="Color 3").grid(row=2, column=0)
        self._csel_3 = tk.Button(self, width="10")
        self._csel_3.configure(command=lambda cvar=self._cvar_3, csel=self._csel_3: self._setcolor(cvar, csel))
        self._csel_3.grid(row=2, column=1)

if __name__ == "__main__":
    def test():
        root = tk.Tk()
        colors = [tk.StringVar(), tk.StringVar(), tk.StringVar()]
        PaletteSelect(root, colors[0], colors[1], colors[2]).pack()
        root.mainloop()
    test()
