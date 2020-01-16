from tkinter import *

def auto():
    """test functie voor rood (wel een auto) of groen (geen auto) in het parkeervak"""
    if user_input.get() == "rood":
        user_input.delete(0, END)
        aantal_plekken["text"] = "0"
    elif user_input.get() == "groen":
        user_input.delete(0, END)
        aantal_plekken["text"] = "1"
    else:
        user_input.delete(0, END)
        aantal_plekken["text"] = "vul in: rood of groen"


root = Tk()

width = 50
height = 50

#fullscreen
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

main_frame = Frame(root, relief='raised', borderwidth=3)
main_frame.pack(fill=BOTH, expand=YES)

photo = PhotoImage(file="pr.png")
b, l = photo.width(), photo.height()

background_label = Label(main_frame, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


center_frame = Frame(main_frame, relief='raised', borderwidth=3)
center_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

aantal_plekken = Label(center_frame,
                       text="rood/groen",
                       font=('Helvetica', 34, 'bold italic'),
                       fg="blue",
                       height=6
                       )
aantal_plekken.pack()

user_input = Entry(center_frame, )
user_input.pack()

button = Button(center_frame,
                width=20,
                text="click",
                command=auto
                )
button.pack()

root.update()
root.state('zoomed')
root.resizable(0, 0)
mainloop()
