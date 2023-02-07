# -*- coding: cp1252 -*-
import Tkinter
import sys
def DrawOval(Event):
    # Event.widget will be the main canvas:
    Event.widget.create_oval(Event.x-5,Event.y-5,Event.x+5,Event.y+5)
def DrawRectangle(Event):
    Event.widget.create_rectangle(Event.x-5,Event.y-5,Event.x+5,Event.y+5)
def MoveButton(Side):
    # The methods pack_forget() and grid_forget() unpack
    # a widget, but (unlike the destroy() method)
    # do not destroy it; it can be re-displayed later.
    QuitButton.pack_forget()
    QuitButton.pack(side=Side)
root=Tkinter.Tk()
MainCanvas=Tkinter.Canvas(root)
MainCanvas.bind("<Button-1>",DrawOval)
MainCanvas.bind("<Button-3>",DrawRectangle)
MainCanvas.pack(fill=Tkinter.BOTH,expand=Tkinter.YES)
QuitButton=Tkinter.Button(MainCanvas,text="Quit",command=sys.exit)
QuitButton.pack(side=Tkinter.BOTTOM)
root.bind("<Up>",lambda e:MoveButton(Tkinter.TOP))
root.bind("<Down>",lambda e:MoveButton(Tkinter.BOTTOM))
root.bind("<Left>",lambda e:MoveButton(Tkinter.LEFT))
root.bind("<Right>",lambda e:MoveButton(Tkinter.RIGHT))
root.geometry("300x300") # Set minimum window size
root.mainloop()
