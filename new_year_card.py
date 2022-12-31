from tkinter import *
from PIL import ImageTk
from random import randint

# We set the parameter that prohibits resizing the opened window.

root = Tk()
root.title('С Новым Годом!')
root.resizable(width=False, height=False)

width = 1100
height = 600

s =  Canvas(root, width=width, height=height, bg='#002665')
s.pack()

# We insert a file that contains the image we need.

image = ImageTk.PhotoImage(file='...')
s.create_image(90, 70, image=image, anchor=NW)

# We set a function where the text is specified, its color, font and size.

def create_text():
    
    text = ("""
    ...
    """)

    s.create_text(width * 2 / 3, height / 2, text=text, fill='yellow', font='Arial 16 bold')    


# We set functions that indicate the amount of snow, its color,
# as well as the parameters for its exit from the window and updating.


def create_snow(t, n):
    for i in range(400):
        x = randint(1, width)
        y = randint(-height * n - 8, height * (1 - n))
        w = randint(3, 8)
        s.create_oval(x, y, x + w, y + w, fill='white', tag=t)
    
    
def motion():
    global indicator_count, indicator
    s.move('tag1', 0, 1)
    s.move('tag2', 0, 1)
    s.move(indicator, 0, 1)
    if s.coords(indicator)[1] < height + 1:
        root.after(20, motion)
    else:
        s.move(indicator, 0, -height - 5)
        root.after(20, motion)
        if indicator_count == 0:
            s.delete('tag1')
            create_snow('tag1', 1)
            indicator_count = 1
        else:
            s.delete('tag2')
            create_snow('tag2', 1)
            indicator_count = 0
    
    
# We set a common function that calls all the others, specifying everything necessary.    
    
    
def call():
    
    global indicator, indicator_count
    indicator = s.create_oval(23, -5, 28, 0, fill='white')
    
    indicator_count = 0
    
    create_text()
    create_snow('tag1', 0)
    create_snow('tag1', 1)
    
    motion()
    
call()

root.mainloop()