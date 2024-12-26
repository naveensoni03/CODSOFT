

from tkinter import *

imaginary_root = Tk()
imaginary_root.title("Simple calculator")
imaginary_root.geometry("570x600+100+200")
imaginary_root.resizable(False,False)
imaginary_root.configure(bg="black")

equation=""

def show (value):
    global equation
    equation+=value
    Label_result.config(text=equation)
    
def clear():
    global equation
    equation = ""
    Label_result.config(text=equation)
    
def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result= eval(equation)
        except:
            result= "error"
            equation = ""
    Label_result.config(text=result)
        


Label_result=Label(imaginary_root,width=25,height=2,text="",font=("arial",30))
Label_result.pack()
# for uppor buttons
Button(imaginary_root,text="C",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda: clear()).place(x=10,y=100)
Button(imaginary_root,text="/",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("/")).place(x=150,y=100)
Button(imaginary_root,text="%",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("%")).place(x=290,y=100)
Button(imaginary_root,text="*",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("*")).place(x=430,y=100)
# Label_result.pack()

# for middle buttons
Button(imaginary_root,text="7",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d20",command=lambda: show("7")).place(x=10,y=200)
Button(imaginary_root,text="8",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d20",command=lambda: show("8")).place(x=150,y=200)
Button(imaginary_root,text="9",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d20",command=lambda: show("9")).place(x=290,y=200)
Button(imaginary_root,text="-",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d20",command=lambda: show("-")).place(x=430,y=200)

# for second middle button
Button(imaginary_root,text="6",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d20",command=lambda: show("6")).place(x=10,y=300)
Button(imaginary_root,text="5",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d20",command=lambda: show("5")).place(x=150,y=300)
Button(imaginary_root,text="4",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d20",command=lambda: show("4")).place(x=290,y=300)
Button(imaginary_root,text="+",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d20",command=lambda: show("+")).place(x=430,y=300)

# second last button
Button(imaginary_root,text="1",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d20",command=lambda: show("1")).place(x=10,y=400)
Button(imaginary_root,text="2",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d20",command=lambda: show("2")).place(x=150,y=400)
Button(imaginary_root,text="3",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d20",command=lambda: show("3")).place(x=290,y=400)
Button(imaginary_root,text="0",width="11",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d20",command=lambda: show("0")).place(x=10,y=500)

# for last buttons
Button(imaginary_root,text=".",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d20",command=lambda: show(".")).place(x=290,y=500)
Button(imaginary_root,text="=",width="5",height="3",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#fe9037",command=lambda: calculate()).place(x=430,y=400)


imaginary_root.mainloop()

