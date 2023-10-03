from tkinter import *
import Use
import New_patient
import Old_patient
import DashBoard
import dentaldb

def test():
    def neww():
        root_option.destroy()
        New_patient.test1()

    def oldd():
        root_option.destroy()
        Old_patient.test2()

    def dashh():
        root_option.destroy()
        DashBoard.test3()

    root_option=Tk()

    root_option.title("Option")
    root_option.configure(background="#023e8a")
    Use.center(root_option)

    labl=Label(root_option,text="Option",font=Use.FONT)
    labl.place(relx=0.45,rely=0)

    lblnew=Label(root_option,text="New_Patient")
    photo_new=PhotoImage(file="photo/dental-record2.png")
    btn_new=Button(root_option,image=photo_new,command=neww)

    btn_new.place(relx=0.1,rely=0.2)
    lblnew.place(relx=0.15,rely=0.5)

    lblold=Label(root_option,text="Old_Patient")
    photo_old=PhotoImage(file="photo/dental-checkup.png")
    btn_old=Button(root_option,image=photo_old,command=oldd)

    btn_old.place(relx=0.7,rely=0.2)
    lblold.place(relx=0.75,rely=0.5)


    lbldash=Label(root_option,text="DashBoard")
    photo_dash=PhotoImage(file="photo/Screenshot 2023-08-18 214418 - Copy.png")
    btn_Dash=Button(root_option,image=photo_dash,command=dashh)

    btn_Dash.place(relx=0.4,rely=0.6)
    lbldash.place(relx=0.45,rely=0.85)

    root_option.mainloop()


