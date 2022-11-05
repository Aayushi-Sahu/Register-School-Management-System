from logging import exception
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from typing import TextIO
import mysql.connector

class Report:
    def __init__(self,root):
       self.root=root
       self.root.title("Student Result Management System")
       self.root.geometry("1352x700+0+0")
       
       title=Label(self.root,text="View Student Result",font=("times new roman",45,"bold"),bg="#08A3D2",fg="#031F3C")
       title.pack(side=TOP,fill=X)
       
        #===============================
       self.var_search=StringVar()
       self.var_id=""
       #==============================
       lbl_search=Label(self.root,text="Search By Roll No.",font=("times new roman",20,"bold"),bg="white").place(x=280,y=150) 
       txt_search=Entry(self.root,textvariable=self.var_search,font=("times new roman",20,"bold"),bg="white").place(x=580,y=150,width=150) 
       
       Searchbtn=Button(self.root,text="Search",font=("times new roman",20,"bold"),fg="white",bg="#08A3D2",cursor="hand2",command=self.search_data).place(x=750,y=150,width=105,height=30) 
       clearhbtn=Button(self.root,text="Clear",font=("times new roman",20,"bold"),fg="white",bg="gray",cursor="hand2",command=self.clear).place(x=880,y=150,width=105,height=30)
       
       
       
       
       
       lbl_roll=Label(self.root,text="Roll No.",font=("times new roman",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=200,y=230,width=200,height=50) 
       lbl_name=Label(self.root,text="Name",font=("times new roman",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=400,y=230,width=200,height=50)
       lbl_classs=Label(self.root,text="Class",font=("times new roman",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=600,y=230,width=200,height=50)
       lbl_marks_ob=Label(self.root,text="Marks Obtained",font=("times new roman",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=800,y=230,width=200,height=50)
       lbl_full_marks=Label(self.root,text="Total Marks",font=("times new roman",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=1000,y=230,width=200,height=50)
        
        
       self.roll=Label(self.root,font=("times new roman",15,"bold"),bg="white",bd=2,relief=GROOVE)
       self.roll.place(x=200,y=280,width=200,height=50) 
       self.name=Label(self.root,font=("times new roman",15,"bold"),bg="white",bd=2,relief=GROOVE)
       self.name.place(x=400,y=280,width=200,height=50)
       self.classs=Label(self.root,font=("times new roman",15,"bold"),bg="white",bd=2,relief=GROOVE)
       self.classs.place(x=600,y=280,width=200,height=50)
       self.marks_ob=Label(self.root,font=("times new roman",15,"bold"),bg="white",bd=2,relief=GROOVE)
       self.marks_ob.place(x=800,y=280,width=200,height=50)
       self.full_marks=Label(self.root,font=("times new roman",15,"bold"),bg="white",bd=2,relief=GROOVE)
       self.full_marks.place(x=1000,y=280,width=200,height=50)
       
       deletebtn=Button(self.root,text="Delete",font=("times new roman",20,"bold"),fg="white",bg="red",cursor="hand2",command=self.delete_data).place(x=630,y=350,width=150,height=30)
       backbtn=Button(self.root,text="Back",font=("times new roman",20,"bold"),command=self.back_window,fg="#031F3C",bg="white",cursor="hand2").place(x=630,y=450,width=150,height=30)
     #==============================
     #=======================
     #======================
     #======================================
     
     
     
     
    def back_window(self):     
           self.root.destroy()
           import dashboard 
     #[======================]  
    def search_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
        my_cursur=conn.cursor()
        try:
           if self.var_search.get()=="":
                messagebox.showerror("Error","Roll No. should be required")
           else:     
                my_cursur.execute("select * from result where Roll=%s",(self.var_search.get(),))
                row=my_cursur.fetchone()
                if row!=None:
                     self.var_id=row[0]
                     self.roll.config(text=row[1])
                     self.name.config(text=row[2])
                     self.classs.config(text=row[3])
                     self.marks_ob.config(text=row[4])
                     self.full_marks.config(text=row[5])
                else:
                     messagebox.showerror("Error","No record found")
                     self.clear()
        except exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    def clear(self):
                     self.var_id=""
                     self.roll.config(text="")
                     self.name.config(text="")
                     self.classs.config(text="")
                     self.marks_ob.config(text="")
                     self.full_marks.config(text="")   
                     self.var_search.set("")
                     
    def delete_data(self):
        try:
                if self.var_id=="":
                     messagebox.showerror("Error","Search student result first")
                else:     
                    conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
                    my_cursur=conn.cursor()
                    sql="select * from result where rid=%s"                  #==========when email & pass invalid=============
                    value=(self.var_id,)
                    my_cursur.execute(sql,value)
                    row=my_cursur.fetchone()
                    #print(row)
                    if row==None:
                         messagebox.showerror("Error","Invalid student result")
                    else:
                        conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
                        my_cursur=conn.cursor()
                        sql="delete from result where rid=%s"                  #==========when email & pass invalid=============
                        value=(self.var_id,)
                        my_cursur.execute(sql,value)
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Delete","Record Has Been Deleted")
                       
                        self.clear()                  
        except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)}")                  
root=Tk()
ob=Report(root)
root.mainloop()