import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()


def exit_application():
    msg_box = tk.messagebox.askquestion('Ghattekulo Bravery', 'DO you think you can kill me?',
                                        icon='warning')
    if msg_box == 'yes':
      tk.messagebox.showinfo('Return', "NO you can't kill me :)")

    else:
      root.destroy()


button1 = tk.Button(root, text='Hey!! Ghattekulo 32', command=exit_application, bg='brown', fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()
