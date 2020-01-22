from time import sleep
from tkinter import *
from RequestDATA import *

result = fetch_constant()
res_tuple = next(result)
res_int = res_tuple[0]
show_availability = "{}/250 spaces available".format(res_int)

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
                                 text=show_availability,
                                 font=('Helvetica', 34, 'bold italic'),
                                 fg="blue",
                                 height=6,
                                 )
available_parking_spaces.pack()


def refresh():
    res_tuple = next(result)
    res_int = res_tuple[0]
    show_availability = "{}/250 \nspaces available".format(250 - res_int)
    available_parking_spaces["text"] = show_availability
    root.after(500, refresh)


refresh()
mainloop()
