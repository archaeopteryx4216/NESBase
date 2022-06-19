from tkinter import *
from tkinter.simpledialog import *
import json

CFG = None
with open("config.json") as config:
    CFG = json.load(config)

class ColorSelect(Dialog):
    def __init__(self, main):
        super().__init__(main, "NES Color Picker")
    def body(self, main):
        self._color = StringVar()
        self.selection = None
        for j,color_row in enumerate(CFG["colorPalette"]):
            for i,color in enumerate(color_row):
                Radiobutton(main, variable=self._color, value=color, fg="#000000",
                            bg=color, activebackground=color,
                            activeforeground="#000000", selectcolor="#ffffff"
                            ).grid(column=i, row=j)
    def apply(self):
        self.selection = self._color.get()

if __name__ == "__main__":
    def test():
        root = Tk()
        def doit(root=root):
            selected_color = ColorSelect(root).selection
            print(f"Selected color is: {selected_color}")
        t = Button(root, text='Test', command=doit)
        t.pack()
        q = Button(root, text='Quit', command=t.quit)
        q.pack()
        t.mainloop()
    test()
