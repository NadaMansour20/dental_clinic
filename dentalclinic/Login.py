from tkinter import *
from tkinter import messagebox
import Use
import Option
import dentaldb

root_splash=Tk()
root_splash.overrideredirect(True)   #remove title bar
photosplash=PhotoImage(file="photo/Screenshot 2023-08-19 161959.png")
lblsplash=Label(root_splash,image=photosplash)
lblsplash.place(x=0,y=0)
Use.center(root_splash)

def main_screen():
    def check():
        username = txt_username.get()
        password = txt_password.get()
        valid_username = "nada"
        valid_password = "12345"
        if valid_username == username and valid_password == password:
            root_Login.destroy()
            Option.test()
        else:
            messagebox.showerror('Error','Invalid Username Or password')

    root_splash.destroy()
    root_Login = Tk()
    photologin = PhotoImage(file="photo/Screenshot 2023-08-13 190901.png")
    lbllogin = Label(root_Login,image=photologin)
    lbllogin.place(x=0, y=0)
    root_Login.title("Login")
    Use.center(root_Login)
    f = Frame(root_Login)
    lbl_username = Label(f, text='Username', fg="#03045e", font=Use.FONT)
    txt_username = Entry(f, font=Use.FONT)
    lbl_password = Label(f, text='Password', fg="#03045e", font=Use.FONT)
    txt_password = Entry(f, show='*', font=Use.FONT)

    btn_login = Button(f, text='Login', fg='white', bg='#03045e', font=Use.FONT,command=check)
    lbl_username.grid(row=2, column=4, padx=Use.padingx, pady=Use.padingy)
    txt_username.grid(row=2, column=5, padx=Use.padingx, pady=Use.padingy)
    lbl_password.grid(row=3, column=4, padx=Use.padingx, pady=Use.padingy)
    txt_password.grid(row=3, column=5, padx=Use.padingx, pady=Use.padingy)
    btn_login.grid(row=6, column=4, columnspan=2, padx=Use.padingx, pady=Use.padingy)
    f.place(relx=0.7,rely=0.5,anchor="center")
    root_Login.mainloop()



root_splash.after(2000,main_screen)

root_splash.mainloop()








