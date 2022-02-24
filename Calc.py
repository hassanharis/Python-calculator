from tkinter import *
root = Tk()



# define buttons
button_1 = Button(root, text='1', padx=40,pady=20)
button_2 = Button(root, text='2', padx=40,pady=20)
button_3 = Button(root, text='3', padx=40,pady=20)
button_4 = Button(root, text='4', padx=40,pady=20)
button_5 = Button(root, text='5', padx=40,pady=20)
button_6 = Button(root, text='6', padx=40,pady=20)
button_7 = Button(root, text='7', padx=40,pady=20)
button_8 = Button(root, text='8', padx=40,pady=20)
button_9 = Button(root, text='9', padx=40,pady=20)
button_0 = Button(root, text='0', padx=40,pady=20)
button_add = Button(root, text='+', padx=40,pady=20)
button_equal = Button(root, text='=', padx=40,pady=20)
button_division = Button(root, text='÷', padx=40,pady=20)
button_clear = Button(root, text='Clear', padx=40,pady=20)
button_minus = Button(root, text='−', padx=40,pady=20)
button_multiply = Button(root, text='x', padx=40,pady=20)
button_dot = Button(root, text='.', padx=40,pady=20)
button_plusminus = Button(root, text='+/−', padx=40,pady=20)

#button placement on screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=4,column=0)
button_5.grid(row=4,column=1)
button_6.grid(row=4,column=2)
button_7.grid(row=5,column=0)
button_8.grid(row=5,column=1)
button_9.grid(row=5,column=2)
button_0.grid(row=6,column=1)

button_plusminus.grid(row=6,column=0)
button_dot.grid(row=6,column=2)
button_division.grid(row=3,column=4)
button_multiply.grid(row=4,column=4)
button_minus.grid(row=5,column=4)
button_add.grid(row=6,column=4)


root.mainloop()