from tkinter import *
from tkinter.ttk import *
import Use
import Option
import dentaldb
from tkinter import messagebox


def test3():
    root_Dash = Tk()
    ft = Frame(root_Dash)
    column = ['id', 'name', 'age', 'gender', 'phone', 'disease']
    table = Treeview(ft, column=column, show='headings')

    table.heading('id', text='Id patient')
    table.heading('name', text='Name')
    table.heading('age', text=' Age')
    table.heading('gender', text='Gender')
    table.heading('phone', text='Phone Number')
    table.heading('disease', text='Disease')
    table.column('id', width=50, anchor='center')
    table.column('name', width=60, anchor='center')
    table.column('age', width=50, anchor='center')
    table.column('gender', width=85, anchor='center')
    table.column('phone', width=130, anchor='center')
    table.column('disease', width=70, anchor='center')

    def displayButton():
        result = dentaldb.showAllpatient()
        for row in result:
            table.insert('', END, values=row)

    def option():
        root_Dash.destroy()
        Option.test()


    root_Dash.title("DashBoard")
    Use.center(root_Dash)
    root_Dash.configure(background="#03045e")


    phot = PhotoImage(file="photo/Screenshot 2023-08-19 205652.png")
    ph = Label(root_Dash, image=phot)
    ph.place(x=0, y=0)

    ff = Frame(root_Dash)
    labl = Label(ff, text="DashBoard", font=Use.FONT)
    labl.grid(row=0, column=0)
    ff.place(relx=0.1, rely=0.05)

    table.grid(row=0, column=0)
    ft.place(relx=0.36, rely=0)

    fr = Frame(root_Dash)
    btnd = Button(fr, text="return option",command=option)
    btnd.grid(row=10, column=2)
    fr.place(relx=0.85, rely=0.9)

    fsh=Frame(root_Dash)
    btnshow=Button(fsh,text="Show",command=displayButton)
    btnshow.grid(row=10,column=1)
    fsh.place(relx=0.7, rely=0.9)


    root_Dash.mainloop()

