from tkinter import *

class Application(Frame):
    def say_hi(self):
        print("Run")
        root.quit()

    def say_hi1(self):
        print("Spell")
        root.quit()

    def say_hi2(self):
        print("Attack")
        root.quit()

    def createWidgets(self):
        self.run = Button(self)
        self.run["text"] = "Run",
        self.run["command"] = self.say_hi

        self.run.pack({"side": "left"})


        self.spell = Button(self)
        self.spell["text"] = "Spell",
        self.spell["command"] = self.say_hi1

        self.spell.pack({"side": "left"})

        self.attack = Button(self)
        self.attack["text"] = "Attack",
        self.attack["command"] = self.say_hi2

        self.attack.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
#thigns before button is pressed
app.mainloop()
#things after button is pressed
root.destroy()
