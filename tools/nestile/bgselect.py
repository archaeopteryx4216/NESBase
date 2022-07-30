import tkinter as tk
from colorselect import ColorSelect

class BGSelect(tk.Frame):
    def _setcolor(self, cvar, csel):
        color = ColorSelect(self).selection
        csel.configure(bg=color)
        cvar.set(color)

    def __init__(self, main=None, cvar=None):
        tk.Frame.__init__(self, main)
        if not cvar or not isinstance(cvar, tk.StringVar):
            raise(ValueError("BGSelect widget must be created with a StringVar to hold the color of the background."))
        # Save references to the stringvar
        self._cvar = cvar
        self._cvar.set("#000000")
        # Pack ColorSelect button onto the frame
        tk.Label(self, text="BG Color").grid(row=0, column=0)
        self._csel = tk.Button(self, width="10")
        self._csel.configure(bg=self._cvar.get(), command=lambda cvar=self._cvar, csel=self._csel: self._setcolor(cvar, csel))
        self._csel.grid(row=0, column=1, sticky=tk.E)

if __name__ == "__main__":
    def test():
        root = tk.Tk()
        color = tk.StringVar()
        BGSelect(root, color).pack()
        root.mainloop()
    test()
