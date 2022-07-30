import json
import tkinter as tk
from tkinter.simpledialog import *
from paletteselect import PaletteSelect
from bgselect import BGSelect





class PaletteMultiSelect(Dialog):
    @staticmethod
    def _palette_init():
        palette = {
            "background": tk.StringVar(),
            "palettes": [
                [tk.StringVar(), tk.StringVar(), tk.StringVar()],
                [tk.StringVar(), tk.StringVar(), tk.StringVar()],
                [tk.StringVar(), tk.StringVar(), tk.StringVar()]
            ]
        }
        palette["background"].set("#000000")
        for palno in range(3):
            for colno in range(3):
                palette["palettes"][palno][colno].set("#000000")
        return palette

    @staticmethod
    def _palette_to_json_str(palette):
        js = {
            "background" : palette["background"].get(),
            "palettes": list(map(lambda l: list(map(lambda p: p.get(), l)), palette["palettes"]))
        }
        return json.dumps(js)

    def __init__(self, main):
        super().__init__(main, "NES Palette Picker")

    def body(self, main):
        self._main = main
        self._palette = self._palette_init()
        self.selection = None
        # Add background color picker
        tk.Label(self, text="Background").pack()
        BGSelect(self, self._palette["background"]).pack()
        # Palette pickers 1, 2, and 3
        tk.Label(self, text="Palette 1").pack()
        PaletteSelect(self, self._palette["palettes"][0][0], self._palette["palettes"][0][1], self._palette["palettes"][0][2]).pack()
        tk.Label(self, text="Palette 2").pack()
        PaletteSelect(self, self._palette["palettes"][1][0], self._palette["palettes"][1][1], self._palette["palettes"][1][2]).pack()
        tk.Label(self, text="Palette 3").pack()
        PaletteSelect(self, self._palette["palettes"][2][0], self._palette["palettes"][2][1], self._palette["palettes"][2][2]).pack()

    def apply(self):
        self.selection = self._palette_to_json_str(self._palette)

if __name__ == "__main__":
    def test():
        root = tk.Tk()
        def doit(root=root):
            selected_palette = PaletteMultiSelect(root).selection
            print(f"Selected color is: {selected_palette}")
        t = tk.Button(root, text='Test', command=doit)
        t.pack()
        q = tk.Button(root, text='Quit', command=t.quit)
        q.pack()
        root.mainloop()
    test()
