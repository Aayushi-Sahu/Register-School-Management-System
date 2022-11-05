from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from typing import TextIO
import mysql.connector



class Student:
    def __init__(self,root):
       self.root=root
       self.root.title("School Management System")
       self.root.geometry("1350x700+0+0")
       
       title=Label(self.root,text="School Management System",bd=10,font=("times new roman",45,"bold"),bg="#08A3D2",fg="#031F3C").place(x=0,y=0,relwidth=1,height=80)
       
       
      
       
       #===============menusFr ame==================
       Manage_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
       Manage_Frame.place(x=60,y=100,width=1800,height=110)
       
       class_btn=Button(Manage_Frame,text="Class",command=self.classs_window,font=("times new roman",15,"bold"),bg="#031F3C",fg="#08A3D2",bd=0,cursor="hand2").place(x=20,y=15,width=180,height=40)
      
       student_btn=Button(Manage_Frame,text="Student",command=self.Student_detail_window,font=("times new roman",15,"bold"),bg="#031F3C",fg="#08A3D2",bd=0,cursor="hand2").place(x=240,y=15,width=180,height=40)
       
       teacher_btn=Button(Manage_Frame,text="Teacher",command=self.Teacher_detail_window,font=("times new roman",15,"bold"),bg="#031F3C",fg="#08A3D2",bd=0,cursor="hand2").place(x=460,y=15,width=180,height=40)
       
       staff_btn=Button(Manage_Frame,text="Worker",command=self.Worker_detail_window,font=("times new roman",15,"bold"),bg="#031F3C",fg="#08A3D2",bd=0,cursor="hand2").place(x=680,y=15,width=180,height=40)
       
       timetable_btn=Button(Manage_Frame,text="Time Table",command=self.tt_detail_window,font=("times new roman",15,"bold"),bg="#031F3C",fg="#08A3D2",bd=0,cursor="hand2").place(x=900,y=15,width=180,height=40)
       
       result_btn=Button(Manage_Frame,text="Result",command=self.result,font=("times new roman",15,"bold"),bg="#031F3C",fg="#08A3D2",bd=0,cursor="hand2").place(x=1120,y=15,width=180,height=40)
       
       viewresult_btn=Button(Manage_Frame,text="View Student Result",command=self.report_window,font=("times new roman",15,"bold"),bg="#031F3C",fg="#08A3D2",bd=0,cursor="hand2").place(x=1340,y=15,width=180,height=40)
       
       logout_btn=Button(Manage_Frame,text="Log out",command=self.logout,font=("times new roman",15,"bold"),bg="#031F3C",fg="#08A3D2",bd=0,cursor="hand2").place(x=1560,y=15,width=180,height=40)
       
       
       
      
       #==============Footer==================
       footer=Label(self.root,text="School Management System\nContact us for any Technical Issues: 9782541222",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
       
       self.lbl_student=Label(self.root,text="Total Students\n[ 0 ]",bd=10,font=("times new roman",30,"bold"),bg="#e43b06",fg="#031F3C")
       self.lbl_student.place(x=400,y=800,width=300,height=100)
       
       self.lbl_teacher=Label(self.root,text="Total Teachers\n[ 0 ]",bd=10,font=("times new roman",30,"bold"),bg="#08A3D2",fg="#031F3C")
       self.lbl_teacher.place(x=800,y=800,width=300,height=100)
       
       self.lbl_worker=Label(self.root,text="Total Workers\n[ 0 ]",bd=10,font=("times new roman",30,"bold"),bg="#038074",fg="#031F3C")
       self.lbl_worker.place(x=1200,y=800,width=300,height=100)
       
       
       #==========================function===========
       self.update_details()
       
       
       

          
     #==================================================================================================================
     #============================================================================================
     #=======================================================================
     #===================================================
     #=====================================Student Window+====================================================
     #===================================================
     #===================================================================  
     
      
    def Student_detail_window(self):
                 
                  self.root.destroy()
                                  
                  import student
                    
                   
    def Teacher_detail_window(self):
           self.root.destroy()
           import teacher
    def Worker_detail_window(self):
           self.root.destroy()
           import worker
    def tt_detail_window(self):
           self.root.destroy()
           import timetable 
    def result(self):     
           self.root.destroy()
           import result
    def classs_window(self):
           self.root.destroy()
           import classes
    def report_window(self):     
           self.root.destroy()
           import report
          
           
           
    def logout(self):
          op=messagebox.askyesno("confirm","Do you really want to logout?")  
          if op==True:
                 self.root.destroy()
                 import login
     #==================================================================================================================
     #============================================================================================
     #=======================================================================
     #===================================================
     #=====================================Teacher Window+====================================================
     #===================================================
     #==================================================================
     # 
     # 
    def update_details(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
        my_cursur=conn.cursor()
        
        my_cursur.execute("select * from Student_pro")
        cr=my_cursur.fetchall()
        self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")
        
        my_cursur.execute("select * from teachers_pro")
        cr=my_cursur.fetchall()
        self.lbl_teacher.config(text=f"Total Teachers\n[{str(len(cr))}]")
        
        my_cursur.execute("select * from worker")
        cr=my_cursur.fetchall()
        self.lbl_worker.config(text=f"Total Workers\n[{str(len(cr))}]")
        
        
        self.lbl_student.after(200,self.update_details)
        conn.commit()
        conn.close()   
    #==================================================================================================================
     #============================================================================================
     #=======================================================================
     #===================================================
     #=====================================Staff Window+====================================================
     #===================================================
     #===================================================================            
                
    
    
    #==================================================================================================================
     #============================================================================================
     #=======================================================================
     #===================================================
     #=====================================Staff Window+====================================================
     #===================================================
     #===================================================================  
        
   
    
         
root=Tk()
ob=Student(root)
root.mainloop()