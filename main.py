import pyshorteners
from tkinter import *

win=Tk()
win.geometry("350x270")
win.configure(bg="yellow")

#BUtton function
def short():
    url=entry1.get()
    s=pyshorteners.Shortener().tinyurl.short(url)

    entry2.insert(END,s)

#creating label for entering usr url
Label(win,text="Enter your URL link",font="impack 17 bold",bg="black",fg="white").pack(fill="x")
#creating entry box
entry1 = Entry(win,font="10",bd=3,width=40)
entry1.pack(pady=30)
#creating button
Button(win,text="Click Here",font="impack 12 bold",bg="red",fg="white",width="15",command=short).pack()
#Entry
entry2=Entry(win,font="impack 16 bold",bg="yellow",width=24,bd=0)
entry2.pack(pady=31)
mainloop()
