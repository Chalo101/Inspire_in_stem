from tkinter import *

# root=Tk()
# # root.geometry="700x700"
# login_name =Label(root,text="Name" , font="Arial 20 bold").pack()
# login_pass= Label(root,text="Password" , font="Arial 20 bold").pack()
# # login_name.grid( column =60 , row =120)
# # login_pass.grid(column=60 , row=180)
# login_box=Entry(root, width=60).pack()
# # login_box.grid(column=100 , row=120)

# register =Label(root,text="Name" , font="Arial 20 bold")
# # register.grid( column =60 , row =180)
# register_box=Entry(root, width=60)
# # register_box.grid(column=100 , row=120)

granted =False
def grant():
    global granted
    granted = True
def login(name,password):
    success = False
    file = open("user_details.txt","r")
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        if(a==name and b==password):
            success = True
            break
    file.close()
    if(success):
        print("Login Successful!!!")
        grant()
    else:
        print("Wrong name or password"+"\n")
def register(name,password):
    file = open("user_details.txt" ,"a")
    file.write("\n"+name+","+password)
    grant()
    file.close()

def access(option):
    global name
    if (option=="login"):
        name = input ("Emter your name: ")
        password = input("Enter our password: ")
        login(name,password)
    else:
        print("To register, enter your name and password")
        name = input("Enter your name: ")
        password = input ("Enter your password: ")
        register(name,password)

def begin():
    global option
    print("Welcome to Chalo's System")
    option = input("Either login or register with us(login,register): ")
    if(option!="login") and (option!="register"):
        begin()
begin()
access(option)

if(granted):
    print("Welcome to Chalo's prgram")
    print("Username: ",name)