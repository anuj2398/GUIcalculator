from tkinter import *
root=Tk()
root.geometry("355x470")
root.resizable(width=False,height=False)
root.title("CALCULA_THOR")
label=Label(root,text="CALCULATOR")
label=Label(root,text="CALCULATOR",bg="black",fg="white",font=("Ariel",15,"bold"))
label.pack(side=TOP)
root.config(background="black")
textIn=StringVar()
string=''
def allBtn(a):
    global string
    string=string+str(a)
    textIn.set(string)
def clrbut():
    global string
    string=''
    textIn.set('')
def eqlBtn():
    global string
    string=str(eval(string))
    textIn.set(string)
def delbtn():
    global string
    string=string[:-1]
    textIn.set(string)
def percn():
    global string
    string=str(int(string)/100)
    textIn.set(string)
textBox=Entry(root,font=("stencil",15,"bold"),textvar=textIn,width=25,bd=6,bg='powder blue')
textBox.pack()
#buttons
btnpercnt=Button(root,padx=20,pady=8,bg="white",text="%",font=("Arielss",10,"bold"),command=lambda:percn())
btnpercnt.place(x=10,y=110)
btnclear=Button(root,padx=77,pady=8,bg="orange",text="CLR",font=("Arielss",10,"bold"),command=lambda:clrbut())
btnclear.place(x=80,y=110)
btndel=Button(root,padx=15,pady=8,bg="red",text="DEL",font=("Arielss",10,"bold"),command=lambda:delbtn())
btndel.place(x=280,y=110)
btn7=Button(root,padx=20,pady=8,bg="white",text="7",font=("Arielss",10,"bold"),command=lambda:allBtn('7'))
btn7.place(x=10,y=170)
btn8=Button(root,padx=20,pady=8,bg="white",text="8",font=("Arielss",10,"bold"),command=lambda:allBtn('8'))
btn8.place(x=90,y=170)
btn9=Button(root,padx=20,pady=8,bg="white",text="9",font=("Arielss",10,"bold"),command=lambda:allBtn('9'))
btn9.place(x=170,y=170)
btn4=Button(root,padx=20,pady=8,bg="white",text="4",font=("Arielss",10,"bold"),command=lambda:allBtn('4'))
btn4.place(x=10,y=230)
btn5=Button(root,padx=20,pady=8,bg="white",text="5",font=("Arielss",10,"bold"),command=lambda:allBtn('5'))
btn5.place(x=90,y=230)
btn6=Button(root,padx=20,pady=8,bg="white",text="6",font=("Arielss",10,"bold"),command=lambda:allBtn('6'))
btn6.place(x=170,y=230)
btn1=Button(root,padx=20,pady=8,bg="white",text="1",font=("Arielss",10,"bold"),command=lambda:allBtn('1'))
btn1.place(x=10,y=290)
btn2=Button(root,padx=20,pady=8,bg="white",text="2",font=("Arielss",10,"bold"),command=lambda:allBtn('2'))
btn2.place(x=90,y=290)
btn3=Button(root,padx=20,pady=8,bg="white",text="3",font=("Arielss",10,"bold"),command=lambda:allBtn('3'))
btn3.place(x=170,y=290)
btnadd=Button(root,padx=40,pady=8,bg="white",text="+",font=("Arielss",10,"bold"),command=lambda:allBtn('+'))
btnadd.place(x=250,y=170)
btnsub=Button(root,padx=40,pady=8,bg="white",text="-",font=("Arielss",10,"bold"),command=lambda:allBtn('-'))
btnsub.place(x=253,y=230)
btnmul=Button(root,padx=40,pady=8,bg="white",text="x",font=("Arielss",10,"bold"),command=lambda:allBtn('*'))
btnmul.place(x=250,y=290)
btndot=Button(root,padx=20,pady=8,bg="white",text=".",font=("Arielss",10,"bold"),command=lambda:allBtn('.'))
btndot.place(x=10,y=350)
btn0=Button(root,padx=20,pady=8,bg="white",text="0",font=("Arielss",10,"bold"),command=lambda:allBtn('0'))
btn0.place(x=90,y=350)
btndiv=Button(root,padx=20,pady=8,bg="white",text="/",font=("Arielss",10,"bold"),command=lambda:allBtn('/'))
btndiv.place(x=170,y=350)
btnequal=Button(root,padx=40,pady=8,bg="green",text="=",font=("Arielss",10,"bold"),command=lambda:eqlBtn())
btnequal.place(x=250,y=350)
labelButtom=Label(root,text="Design And Developed By:Levi_Ackerman",bg="grey",fg="white",font=("Arial",8,"bold"),padx=80)
labelButtom.pack(side=BOTTOM)

root.mainloop()
