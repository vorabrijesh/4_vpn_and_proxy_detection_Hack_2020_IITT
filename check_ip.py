from tkinter import * 
r = Tk() 

l1 = Label(r,text="Enter IP in the box below")
l1.pack()

e1 = Entry(r)
e1.pack()
#e1.grid(row=1,column=1)

bt = Button(r, text='Check if VPN', width=25)
bt.pack() 

l2 = Label(r,text="Output")
l2.pack()
#l2.grid(row=2)

scroll = Scrollbar(r)
scroll.pack(side = RIGHT,fill =Y)

l3 = Label(r,text="VPN")
l3.pack()

l4 = Label(r,text="Yes")
l4.pack()

r.mainloop() 