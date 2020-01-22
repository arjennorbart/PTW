from tkinter import *
from RequestDATA import *

result = fetch_constant()


def auto():
    """test functie"""
    res2 = next(result)
    available_parking_spaces["text"] = res2


root = Tk()

# fullscreen
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (width, height))

main_frame = Frame(root, relief='raised', borderwidth=3)
main_frame.pack(fill=BOTH, expand=YES)

photo = PhotoImage(file="pr.png")

background_label = Label(main_frame, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

center_frame = Frame(main_frame, relief='raised', borderwidth=3)
center_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

available_parking_spaces = Label(center_frame,
                                 text="",
                                 font=('Helvetica', 34, 'bold italic'),
                                 fg="blue",
                                 height=6
                                 )
available_parking_spaces.pack()

button = Button(center_frame,
                width=20,
                text="click",
                command=auto
                )
button.pack()

mainloop()

