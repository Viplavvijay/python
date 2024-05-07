from tkinter import *
root=Tk()
root.title("Calculator")
root.geometry("400x300+10+10")
root.config(bg="powderblue")

class mywindow:
    def gui(self,master):

        #label
        self.lbl1=Label(master,font=("arial",15,"italic"),bg="powderblue",text="eNO1")
        self.lbl1.place(x=10,y=50)
        self.lbl2=Label(master,font=("arial",15,"italic"),bg="powderblue",text="eNO2")
        self.lbl2.place(x=10,y=100)
        self.lbl3=Label(master,font=("arial",15,"italic"),bg="powderblue",text="RESULT")
        self.lbl3.place(x=10,y=300)

        #entrybox
        self.t1=Entry(font=("arial",15,"italic"),bd=2)
        self.t1.place(x=200,y=50)
        self.t2=Entry(font=("arial",15,"italic"),bd=2)
        self.t2.place(x=200,y=100)
        self.t3=Entry(font=("arial",15,"italic"),bd=2)
        self.t3.place(x=200,y=200)
                      
        #button
        self.b1=Button(master,text="add",command=self.add(),font=("arial",10,"italic"),width=12)
        self.b1.place(x=200,y=150)
        self.b2=Button(master,text="sub",command=self.sub(),font=("arial",10,"italic"),width=12)
        self.b2.place(x=300,y=150)

    def add(self):
        self.t3.delete(0,"end")
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END,int(result))

abc=mywindow()
abc.gui(root)

root.mainloop()  
        
        