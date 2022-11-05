from logging import exception
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from typing import TextIO
import mysql.connector

class result:
    def __init__(self,root):
       self.root=root
       self.root.title("Student Result Management System")
       self.root.geometry("1352x700+0+0")
       
       title=Label(self.root,text="Add Student Result",font=("times new roman",45,"bold"),bg="#08A3D2",fg="#031F3C")
       title.pack(side=TOP,fill=X)
       #====================variables========
       self.var_id=StringVar()
       self.var_roll=StringVar()
       self.var_name=StringVar()
       self.var_class=StringVar()
       self.var_marks=StringVar()
       self.var_full_marks=StringVar()
       self.roll_list=[]
       self.fetch_roll()
       
       
       
      
       #===============================
       #==============================
       lbl_select=Label(self.root,text="Select Student",font=("times new roman",20,"bold"),bg="white").place(x=250,y=150) 
       lbl_name=Label(self.root,text="Name",font=("times new roman",20,"bold"),bg="white").place(x=250,y=230)
       lbl_class=Label(self.root,text="Class",font=("times new roman",20,"bold"),bg="white").place(x=250,y=310)
       lbl_marks_ob=Label(self.root,text="Marks Obtained",font=("times new roman",20,"bold"),bg="white").place(x=250,y=390)
       lbl_full_marks=Label(self.root,text="Full Marks",font=("times new roman",20,"bold"),bg="white").place(x=250,y=470)
       
       #===================
       self.txt_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,font=("times new roman",20,"bold"),state='readonly',justify=CENTER)      #============use combobox==========
       
       self.txt_student.place(x=650,y=150,width=200)
       self.txt_student.set("Select")
       
       Searchbtn=Button(self.root,text="Search",font=("times new roman",20,"bold"),fg="white",bg="#08A3D2",cursor="hand2",command=self.search_data).place(x=880,y=150,width=105,height=30) 

       
       txt_name=Entry(self.root,textvariable=self.var_name,font=("times new roman",18),bg="white",state='readonly').place(x=650,y=230,width=330)
       txt_class=Entry(self.root,textvariable=self.var_class,font=("times new roman",18),bg="white",state='readonly').place(x=650,y=310,width=330)
       txt_marks=Entry(self.root,textvariable=self.var_marks,font=("times new roman",18),bg="white").place(x=650,y=390,width=330)
       txt_full_marks=Entry(self.root,textvariable=self.var_full_marks,font=("times new roman",18),bg="white").place(x=650,y=470,width=330)
       
       
       btn_add=Button(self.root,text="Submit",fg="white",bg="green",cursor="hand2",command=self.add_result,font=("times new roman",18)).place(x=650,y=550,width=130)
       btn_clear=Button(self.root,text="Clear",fg="white",bg="#B00857",cursor="hand2",command=self.clear,font=("times new roman",18)).place(x=850,y=550,width=130)
    
       btn_back=Button(self.root,text="Back",fg="#031F3C",bg="white",cursor="hand2",command=self.back_window,font=("times new roman",18)).place(x=750,y=700,width=100)
    
    def back_window(self):     
           self.root.destroy()
           import dashboard 
           
           
           
    def fetch_roll(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
        my_cursur=conn.cursor()
        try:
           my_cursur.execute("select Roll from student_pro")
           rows=my_cursur.fetchall()
           if len(rows)>0:
               for row in rows:
                   self.roll_list.append(row[0])
        except exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
    def search_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
        my_cursur=conn.cursor()
        try:
           sql="select Name,class from student_pro where Roll=%s"
           value=(self.var_roll.get(),)
           my_cursur.execute(sql,value)
           row=my_cursur.fetchone()
           if row!=None:
              self.var_name.set(row[0])
              self.var_class.set(row[1])
           else:
              messagebox.showerror("Error","No record found")
              
        except exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
    def add_result(self):
        if  self.var_name.get()=="" :
                messagebox.showerror("Error","Please first search student record")
        else: 
            try:  
                conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
                my_cursur=conn.cursor()
                sql="select * from result where Roll=%s and class=%s"                  #==========when email & pass invalid=============
                value=(self.var_roll.get(),self.var_class.get(),)
                my_cursur.execute(sql,value)
                row=my_cursur.fetchone()
                #print(row)
                if row!=None:
                    messagebox.showerror("Error","Result already exists")
                else:
                    my_cursur.execute("insert into result(Roll,Name,class,marks_ob,full_marks) values(%s,%s,%s,%s,%s)",
                                                                                                                    (self.var_roll.get(),
                                                                                                                    self.var_name.get(),
                                                                                                                    self.var_class.get(),
                                                                                                                    self.var_marks.get(),
                                                                                                                    self.var_full_marks.get()
                                                                                                                               ))
                    conn.commit()
                    self.clear()
                    conn.close()
                    messagebox.showinfo("Success","Record Has Been Inserted")
            except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)}")        
                
    def clear(self):
           self.var_roll.set("Select"),
           self.var_name.set(""),
           self.var_class.set(""),
           self.var_marks.set(""),
           self.var_full_marks.set("")
                                                                                                                                        
                
                
                
                
root=Tk()
ob=result(root)
root.mainloop()