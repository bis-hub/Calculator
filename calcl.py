from tkinter import *
root = Tk()
root.title("Simple Calculator")
root.iconbitmap("calculator.ico")
root.geometry("581x710")
root.configure(bg="grey")
lbl = Label(root, text="Calculator", font=("Arial", 28, "bold")).grid(row=0, column=1)
e = Entry(root, width=60, borderwidth=15, fg="white", bg="black", font=("Arial", 10, "bold"))
e.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

def btn_click (num):
    source = e.get()
    e.delete(0, END)
    e.insert(0, str(source)+str(num))

def btn_clear():
    e.delete(0,END)

def btn_add():
    first_num=e.get()
    global number
    global calculator
    calculator="Addition"
    number=int(first_num)
    e.delete(0,END)

def btn_mult():
    first_num = e.get()
    global number
    global calculator
    calculator = "Multiplication"
    number = int(first_num)
    e.delete(0, END)

def btn_div():
    first_num = e.get()
    global number
    global calculator
    calculator = "Division"
    number = int(first_num)
    e.delete(0, END)

def btn_sub():
    first_num = e.get()
    global number
    global calculator
    calculator = "Subtraction"
    number = int(first_num)
    e.delete(0, END)

def btn_equal():
    second_num=e.get()
    e.delete(0,END)
    if calculator=="Addition":
        e.insert(0,number+int(second_num))
    elif calculator=="Multiplication":
        e.insert(0,number*int(second_num))
    elif calculator=="Division":
        e.insert(0,number/int(second_num))
    elif calculator=="Subtraction":
        e.insert(0,number-int(second_num))

#declaring frames and buttons

frame=Frame(root,highlightbackground="grey",highlightthickness=5,bg="black")
btn1=Button(root,text="1",bg="yellow",bd=8,font=("arial",10,"bold"),padx=82,pady=30,command=lambda : btn_click(1))
btn2=Button(root,text="2",bg="dark gray",bd=8,font=("arial",10,"bold"),padx=82,pady=30,command=lambda : btn_click(2))
btn3=Button(root,text="3",bg="orange",bd=8,font=("arial",10,"bold"),padx=82,pady=30,command=lambda : btn_click(3))

btn4=Button(root,text="4",bg="green",bd=8,font=("arial",10,"bold"),padx=82,pady=30,command=lambda : btn_click(4))
btn5=Button(root,text="5",bg="purple",bd=8,font=("arial",10,"bold"),padx=82,pady=30,command=lambda : btn_click(5))
btn6=Button(root,text="6",bg="cyan",bd=8,font=("arial",10,"bold"),padx=82,pady=30,command=lambda : btn_click(6))

btn7=Button(root,text="7",bg="gray",bd=8,font=("arial",10,"bold"),padx=82,pady=30,command=lambda : btn_click(7))
btn8=Button(root,text="8",bg="red",bd=8,font=("arial",10,"bold"),padx=82,pady=30,command=lambda : btn_click(8))
btn9=Button(root,text="9",bg="white",bd=8,font=("arial",10,"bold"),padx=82,pady=30,command=lambda : btn_click(9))

btn0=Button(root,text="0",bg="blue",bd=8,font=("arial",10,"bold"),padx=82,pady=30,command=lambda : btn_click(0))
btn_add=Button(root,text="+",bg="orange",bd=8,font=("arial",10,"bold"),padx=82,pady=30,command=btn_add)
btn_mult=Button(root,text="*",bg="light yellow",bd=8,font=("arial",10,"bold"),padx=82,pady=30,command=btn_mult)
btn_div=Button(root,text="/",bg="purple",bd=8,font=("arial",10,"bold"),padx=82,pady=30,command=btn_div)
btn_sub=Button(root,text="-",bg="light blue",bd=8,font=("arial",10,"bold"),padx=82,pady=30,command=btn_sub)
btn_equal=Button(root,text="=",bg="red",bd=8,font=("arial",10,"bold"),padx=176,pady=30,command=btn_equal)
btn_clear=Button(root,text="Clear",bg="light green",bd=8,font=("arial",10,"bold"),padx=164,pady=30,command=btn_clear)

btn1.grid(row=4,column=0)
btn2.grid(row=4,column=1)
btn3.grid(row=4,column=2)

btn4.grid(row=3,column=0)
btn5.grid(row=3,column=1)
btn6.grid(row=3,column=2)

btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)

btn0.grid(row=5,column=0)
btn_add.grid(row=6,column=0)
btn_mult.grid(row=6,column=1)
btn_div.grid(row=6,column=2)
btn_sub.grid(row=7,column=0)
btn_equal.grid(row=7,column=1,columnspan=2)
btn_clear.grid(row=5,column=1,columnspan=2)
root.mainloop()