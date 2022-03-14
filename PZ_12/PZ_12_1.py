from tkinter import *


root = Tk()
root.title('Zookeeper form')
root.geometry('505x680+200+200')
root["bg"] = "white"
Label(text="Zoo Keeper Application Form", width=25, fg='black', bg="white", font='arial 25').place(x=-30,y=0)
Label(text="Please complete the form. Mandatory fields are maked withh a*", width=70, fg='black', bg="white", font='courier 8').place(x=-28, y=36)


Label(text="Contact Details", width=20, fg='black', bg="white", font='Georgia 14',).place(x=-25, y=65)
Label(text="Name", width=15, fg='black', bg="white", font='courier 12').place(x=-25, y=110)
Label(text="Telephone", width=15, fg='black', bg="white", font='courier 12').place(x=0, y=140)
Label(text="Email ", width=15, fg='black', bg="white", font='courier 12').place(x=-15, y=170)
Entry(width=30, font='arial 12').place(x=150, y=110)
Entry(width=30, font='arial 12').place(x=150, y=140)
Entry(width=30, font='arial 12').place(x=150, y=170)


Label(text="Personal information", width=30, fg='black', bg="white", font='Georgia 14').place(x=-52, y=220)
Label(text="Age", width=15, fg='black', bg="white", font='courier 12').place(x=-25, y=270)
Label(text="Gender", width=15, fg='black', bg="white", font='courier 12').place(x=-10, y=300)
Label(text="When did you", width=15, fg='black', bg="white", font='courier 12').place(x=20, y=330)
Label(text="first know you", width=15, fg='black', bg="white", font='courier 11').place(x=28, y=350)
Label(text="wanted to be a", width=15, fg='black', bg="white", font='courier 11').place(x=28, y=369)
Label(text="zoo-keeper?", width=15, fg='black', bg="white", font='courier 11').place(x=15, y=387)

root.mainloop()