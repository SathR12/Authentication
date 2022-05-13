import tkinter
from tkinter import *
import yagmail
import random

#configure gui 
menu = Tk()
menu.geometry('1000x500')
title = Label(menu, text = "Authentication", font = ('Arial', 30))
title.pack()

#sign in 
def sign():
    global menu, title, email
    menu.destroy()
    menu = Tk()
    menu.geometry('1000x500')
    
    title = Label(menu, text = "Sign-in", font = ('Arial', 30))
    email = Entry(menu, width = 50)
    email.insert(1, "Enter your gmail:")
    submit = Button(menu, text = "send verification code", command = auth)
    
    title.pack()
    email.pack()
    submit.pack()



def auth():
    global menu, title, email, random_code, code
    sent = email.get()
    if sent.endswith("gmail.com"):
        menu.destroy()
        menu = Tk()
        menu.geometry('1000x500')
        
        title = Label(menu, text = "Verification Code", font = ('Arial', 30))
        code = Entry(menu, width = 50)
        code.insert(1, "Enter code:")
        submit = Button(menu, text = "verify", command = verify_code)
        
        title.pack()
        code.pack()
        submit.pack()
        with yagmail.SMTP("enter your bot gmail", "enter app password here") as yag:
            random_code = random.randrange(100000, 999999)
            yag.send(sent, "Your sign in code", [str(random_code)])
            

def verify_code():
    global submit, random_code, menu
    if str(random_code) == code.get():
        menu.destroy()
        menu = Tk()
        menu.geometry('1000x500')
    
        title = Label(menu, text = "Successfully verified", font = ('Arial', 30))
        title.pack()
   

 
#Sign-up button
sign = Button(menu, text = "Sign up", font = ('Arial', 15), height = 5, width = 25, command = sign)
sign.pack(side = "top")


#loop
menu.mainloop()




