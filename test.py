from tkinter import *
window = Tk()
window.title('GitHub Desktop')
window.geometry('600x500')

lbl01 = Label(window, text='Sign Up', font = ('Helvetica', 35),fg = 'Gray')
lbl01.grid(column = 0,row = 0)

txt01 = Entry(window, width = 50)
txt01.grid(column = 0, row = 5)

lbl02 = Label(window, text = 'Username', font = ('Helvetica', 10), fg = 'Black')
lbl02.grid(column = 2, row = 5)

txt02 = Entry(window, width = 50)
txt02.grid(column = 0, row = 10)

lbl03 = Label(window, text='Password', font = ('Helvetica', 10),fg = 'Black')
lbl03.grid(column = 2,row = 10)

lbl0 = Label(window, text='.', font = ('Arial', 1), fg = 'White')
lbl0.grid(column= 0, row = 100)


def clicked2():
	lbl01.configure(text='Sign In', font = ('Helvetica', 35),fg = 'Gray')
	lbl01.grid(column = 0,row = 0)

	txt01.configure(width = 50)
	txt01.grid(column = 0, row = 5)

	lbl02.configure(text = 'Username', font = ('Helvetica', 10), fg = 'Black')
	lbl02.grid(column = 2, row = 5)

	txt02.configure(width = 50)
	txt02.grid(column = 0, row = 10)

	lbl03.configure(text='Password', font = ('Helvetica', 10),fg = 'Black')
	lbl03.grid(column = 2,row = 10)


	def clicked():
		if txt01.get() == txt01 and txt02.get() == txt02:
			lbl0.configure(text="Hello!", font = ('Helvetica', 20),fg = 'Gray')
			lbl0.grid(column = 0, row = 40)  
		else:
			lbl0.configure(text='Login or password is not correct', font = ('Helvetica', 15),fg = 'Red')
			lbl0.grid(column = 0, row = 80)

	btn01.configure(text = 'Sign In',fg = 'Black', bg = 'Gray85', command=clicked)
	btn01.grid(column = 0, row = 18)

btn02 = Button(window, text = 'Already have an account?', font = ('Helvetica'), fg = 'Cyan', bg = 'Blue',command = clicked2)
btn02.grid(column = 4, row = 80)

def clicked1():
	lbl01.configure(text='Sign In', font = ('Helvetica', 35),fg = 'Gray')
	lbl01.grid(column = 0,row = 0)

	txt01.configure(width = 50)
	txt01.grid(column = 0, row = 5)

	lbl02.configure(text = 'Username', font = ('Helvetica', 10), fg = 'Black')
	lbl02.grid(column = 2, row = 5)

	txt02.configure(width = 50)
	txt02.grid(column = 0, row = 10)

	lbl03.configure(text='Password', font = ('Helvetica', 10),fg = 'Black')
	lbl03.grid(column = 2,row = 10)

	def clicked3():
		if txt01.get() == txt01 and txt02.get() == txt02:
			lbl0.configure(text="Hello!", font = ('Helvetica', 20),fg = 'Gray')
			lbl0.grid(column = 0, row = 40)  
		else:
			lbl0.configure(text='Login or password is not correct', font = ('Helvetica', 15),fg = 'Red')
			lbl0.grid(column = 0, row = 80)

	btn01.configure(text = 'Sign In',fg = 'Black', bg = 'Gray85', command=clicked3)
	btn01.grid(column = 0, row = 18)

	

btn01 = Button(window, text = 'Sign Up', font = ('Helvetica'), fg = 'Black', bg = 'Gray85', command = clicked1)
btn01.grid(column = 0, row = 18)


window.mainloop()
