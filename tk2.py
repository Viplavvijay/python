from tkinter import *
root=Tk()
root.title("Calculator")
root.geometry("400x300+10+10")
root.config(bg="powderblue")

class Mywindow:
    def gui(self,master):

        #for label
        self.ibl1=Label(master, text="first number",font=("arial",15,"bold"),bg="powderblue")
        self.ibl1.place(x=10,y=50)

        self.ibl2=Label(master,text="second number",font=("arial",15,"bold"),bg="powderblue")
        self.ibl2.place(x=10,y=100)

        self.ibl3=Label(master,text="Result",font=("arial",15,"bold"),bg="powderblue")
        self.ibl3.place(x=10,y=200)

        #for entry box
        self.t1=Entry(bd=3,font=("arial",12,"bold"))
        self.t1.place(x=200,y=50)

        self.t2=Entry(bd=3,font=("arial",12,"bold"))
        self.t2.place(x=200,y=100)

        self.t3=Entry(bd=3,font=("arial",12,"bold"))
        self.t3.place(x=200,y=200)

        #for button for add and sub
        self.b1=Button(master,width=10,text="Add",command=self.add,font=("arial",10,"bold"),bg="powderblue")
        self.b1.place(x=200,y=150)

        self.b2=Button(master,width=10,text="Subtract",command=self.sub,font=("arial",10,"bold"),bg="powderblue")
        self.b2.place(x=300,y=150)


    def add(self):
        self.t3.delete(0,"end")
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END,int(result))

    def sub(self):
        self.t3.delete(0,"end")
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END,int(result))

mywin=Mywindow()
mywin.gui(root)

root.mainloop()