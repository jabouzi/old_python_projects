from Tkinter import *

def onKeyPress(event):
    widget.delete(ALL)    
    txt = 'Got key press: '+ event.keysym
    widget.create_text(200,200,text = txt ,justify = CENTER)
    print txt

tkroot = Tk()
widget = Canvas(tkroot, bg = 'white')                
widget.pack(expand=YES, fill=BOTH)
widget.focus_set()
widget.bind('<KeyPress>',onKeyPress)
tkroot.title('Keyboard')
tkroot.mainloop()
