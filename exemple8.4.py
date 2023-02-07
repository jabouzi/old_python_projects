from Tkinter import *

root = Tk()

def key(event):    
    frame.focus_set()
    print "pressed", repr(event.keysym)

##def callback(event):
##    frame.focus_set()
##    print "clicked at", event.x, event.y

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
#frame.bind("<Button-1>", callback)
frame.pack()
frame.focus_force()

root.mainloop()
