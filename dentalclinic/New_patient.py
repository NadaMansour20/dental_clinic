from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
from tkinter import messagebox
import Use
import Option
import dentaldb
import DashBoard


def test1():
       def save():
               if  id_txt.get() == '' or name_txt.get() == '' or age_txt.get() == '' or phone_txt.get() == '' or rbtn_var .get() == '':

                       messagebox.askokcancel('System', 'please fill all data required for Patient')
               else:
                       dentaldb.addPatient(
                           id_txt.get(),
                           name_txt.get(),
                           age_txt.get(),
                           rbtn_var.get(),
                           phone_txt.get(),
                           combo1.get()
                       )
               id_txt.delete(0,END)
               name_txt.delete(0, END)
               age_txt.delete(0, END)
               phone_txt.delete(0, END)
               rbtn_var.set(1)
               combo1.set('')

       def optionn():     #return option
                root_new.destroy()
                Option.test()

       root_new=Tk()
       root_new.title("New Patient")

       Use.center(root_new)

       phot = PhotoImage(file="photo/Screenshot 2023-08-19 191248.png")
       ph = Label(root_new, image=phot)
       ph.place(x=0,y=0)

       ff =Frame(root_new)
       labl=Label(ff,text="New_patient",font=Use.FONT,bg="#023e8a",fg="white")
       labl.grid(row=0,column=0)
       ff.place(relx=0.1,rely=0.05)

       f=Frame(root_new)
       lbl_id=Label(f,text="Patient ID",fg="#023e8a",font=Use.FONT)
       id_txt=Entry(f,font=Use.FONT)
       lbl_name=Label(f,text="Name",fg="#023e8a",font=Use.FONT)
       name_txt=Entry(f,font=Use.FONT)
       lbl_age=Label(f,text="Age",fg="#023e8a",font=Use.FONT)
       age_txt=Entry(f,font=Use.FONT)
       lbl_male_female = Label(f, text='Gender : ',fg="#023e8a", font=Use.FONT)
       lbl_phone=Label(f,text="Phone number",fg="#023e8a",font=Use.FONT)
       phone_txt=Entry(f,font=Use.FONT)

       rbtn_var = IntVar()
       rbtn_var.set(1)

       rbtn_male = Radiobutton(f, text='Male', value=1, variable=rbtn_var,fg="#023e8a", font=Use.FONT)
       rbtn_female = Radiobutton(f, text='Female', value=2, variable=rbtn_var,fg="#023e8a", font=Use.FONT)

       btnop=Button(f,text="return option",bg="#023e8a",fg="white",font=Use.FONT,command=optionn) #return option
       btnop.grid(row=10,column=2)

       #to save
       btnSave=Button(f,text="Save",bg="#023e8a",fg="white",font=Use.FONT,command=save)

       data= ['Displaced','Implantology','Endodontics','Crown','Orthodontics','Whitening'] #data

       combo1=Combobox(f,values=data,state='readonly')
       lbl_Dis=Label(f,text="Diseases",fg="#023e8a",font=Use.FONT)

       lbl_id.grid(row=1,column=1, padx=Use.padingx, pady=Use.padingy)
       id_txt.grid(row=1,column=2, padx=Use.padingx, pady=Use.padingy)
       lbl_name.grid(row=2,column=1, padx=Use.padingx, pady=Use.padingy)
       name_txt.grid(row=2,column=2, padx=Use.padingx, pady=Use.padingy)
       lbl_age.grid(row=3,column=1, padx=Use.padingx, pady=Use.padingy)
       age_txt.grid(row=3,column=2, padx=Use.padingx, pady=Use.padingy)
       lbl_phone.grid(row=4,column=1,padx=Use.padingx, pady=Use.padingy)
       phone_txt.grid(row=4,column=2,padx=Use.padingx, pady=Use.padingy)
       lbl_male_female.grid(row=5, column=1, padx=Use.padingx, pady=Use.padingy)
       rbtn_male.grid(row=6, column=1, padx=Use.padingx, pady=Use.padingy)
       rbtn_female.grid(row=6, column=2, padx=Use.padingx, pady=Use.padingy)
       lbl_Dis.grid(row=7,column=1)
       combo1.grid(row=8,column=1)
       btnSave.grid(row=9,column=2,padx=Use.padingx,pady=Use.padingy)

       f.place(relx=0.7,rely=0.5,anchor="center")

       root_new.mainloop()
