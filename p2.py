#GUI

from tkinter import *
root=Tk()
root.title("Even Odd Finder by Soham")
root.geometry("800x500")
f=("Ink Free",40,"bold")

def find():
	try:
		num = int(ent_num.get())
		if num % 2 == 0:
			msg= "Even"
		else:
			msg= "Odd"
		lab_msg.configure(text=msg)
	except ValueError:
		msg= "You should enter integers only"
		lab_msg.configure(text=msg)
lab_num = Label(root,text="Enter Integer",font=f)
ent_num = Entry(root,font=f)
btn_find = Button(root,text="Find",font=f,command=find)
lab_msg = Label(root,font=f)

lab_num.pack(pady=5)
ent_num.pack(pady=5)
btn_find.pack(pady=5)
lab_msg.pack(pady=5)

root.mainloop()