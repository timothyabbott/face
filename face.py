from tkinter import colorchooser
import turtle
import tkinter as tk
from tkinter import ttk 
 
class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Your Face!")
        self.canvas = tk.Canvas(master)
        self.canvas.config(width=600, height=600)
        self.canvas.pack(side=tk.LEFT)
        self.screen = turtle.TurtleScreen(self.canvas)
        self.faceColour = (0,'#FFC0CB')
        print(type(self.faceColour[1]))
        self.eyeColour = "blue"
        self.mouthColour = "red"
        self.screen.colormode(255)
        
        # button
        tk.Button(self.master, text="Draw Face", command=self.drawFace).pack()
          # label 
        self.faceColourCombo = ttk.Label(root, text = "Select the Month :", 
            font = ("Times New Roman", 10))
        self.faceColourCombo.pack()
        
        # Combobox creation 
        n = tk.StringVar() 
        self.monthchoosen = ttk.Combobox(root, width = 27, textvariable = n) 
        self.turtle = turtle.RawTurtle(self.screen, shape="turtle")
        self.turtle.color("green")

  
        tk.Button(self.master, text="Choose face colour", command=self.chooseFaceColour).pack()
        tk.Button(self.master, text="Choose eye colour", command=self.chooseEyeColour).pack()
        tk.Button(self.master, text="Choose mouth colour", command=self.chooseMouthColour).pack()  
    
    
    def chooseFaceColour(self):
        self.faceColour = colorchooser.askcolor(title ="Choose colour")
    def chooseEyeColour(self):
        self.eyeColour = colorchooser.askcolor(title ="Choose colour")
    def chooseMouthColour(self):
        self.mouthColour = colorchooser.askcolor(title ="Choose colour")
        print(type(self.mouthColour[1]))
        print (self.mouthColour[1])
    def drawFace(self):
        
        self.turtle.fillcolor(self.faceColour[1])
        self.turtle.begin_fill()
        self.turtle.circle(100)
        self.turtle.end_fill()
        self.turtle.up()

        #  eyes
        self.turtle.goto(-40, 120)
        circle(self,'white', 15)
        self.turtle.goto(-40, 125)
        
        circle(self,self.eyeColour(1), 5)

        self.turtle.goto(40, 120)
        circle(self,'white', 15)
        self.turtle.goto(40, 125)
        circle(self,self.eyeColour, 5)

        # nose
        self.turtle.goto(0, 75)
        circle(self,'black', 8)

        # mouth
        self.turtle.goto(-40, 85)
        self.turtle.down()
        self.turtle.right(90)
        self.turtle.circle(40, 180)
        self.turtle.up()

        # tongue
        self.turtle.goto(-10, 45)
        self.turtle.down()
        self.turtle.right(180)
        self.turtle.fillcolor('red')
        self.turtle.begin_fill()
        self.turtle.circle(10, 180)
        self.turtle.end_fill()
        self.turtle.hideturtle()
    

    # def choose_color(self,colourVariable):
 
    #     # variable to store hexadecimal code of color
    #     colourVariable = colorchooser.askcolor(title ="Choose color") 
    #     print(colourVariable)
        

        

def circle(self,col, rad):
    self.turtle.down()
    self.turtle.fillcolor(col)
    self.turtle.begin_fill()
    self.turtle.circle(rad)
    self.turtle.end_fill()
    self.turtle.up()

 
if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
 
