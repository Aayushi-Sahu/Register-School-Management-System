from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from typing import TextIO
import mysql.connector

class Student:
    def __init__(self,root):
       self.root=root
       self.root.title("Student Management System")
       self.root.geometry("1352x700+0+0")
       
       title=Label(self.root,text="Student Management System",bd=10,font=("times new roman",45,"bold"),bg="#08A3D2",fg="#031F3C")
       title.pack(side=TOP,fill=X)
       
       #=============all variable==========
        #=============all variable==========
       self.Roll_No_var=StringVar()
       self.name_var=StringVar()
       self.email_var=StringVar()
       self.gender_var=StringVar()
       self.contact_var=StringVar()
       self.subject_var=StringVar()
       self.dob_var=StringVar()
       self.teacher_id_var=StringVar()
       self.work_var=StringVar()
       self.worker_id_var=StringVar()
       self.search_by=StringVar()
       self.search_txt=StringVar()
       self.salary_var=StringVar()
       self.day_var=StringVar()
       self.time_var=StringVar()
       self.time1_var=StringVar()
       self.time2_var=StringVar()
       self.time4_var=StringVar()      
       self.time5_var=StringVar()
       self.time6_var=StringVar()
       self.time7_var=StringVar()
       
       #===============Manage Frame==================
       #Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#08A3D2"
       #Manage_Frame.place(x=20,y=100,width=750,height=900)
      
       student_btn=Button(self.root,text="Student",width=14,height=3,command=self.Student_detail_window,font=("times new roman",30,"bold"),bg="#031F3C",fg="#08A3D2",bd=0,cursor="hand2").place(x=300,y=150)
       
       teacher_btn=Button(self.root,text="Teacher",width=14,height=3,command=self.Teacher_detail_window,font=("times new roman",30,"bold"),bg="#031F3C",fg="#08A3D2",bd=0,cursor="hand2").place(x=1300,y=150)
       
       staff_btn=Button(self.root,text="Worker",width=14,height=3,command=self.Worker_detail_window,font=("times new roman",30,"bold"),bg="#031F3C",fg="#08A3D2",bd=0,cursor="hand2").place(x=300,y=600)
       
       timetable_btn=Button(self.root,text="Time Table",width=14,height=3,command=self.Time_Table_window,font=("times new roman",30,"bold"),bg="#031F3C",fg="#08A3D2",bd=0,cursor="hand2").place(x=1300,y=600)
       
       #student_fees_btn=Button(self.root,text="Fees",width=14,height=3,font=("times new roman",30,"bold"),bg="#031F3C",fg="#08A3D2",bd=0,cursor="hand2").place(x=800,y=750)
       
     #==================================================================================================================
     #============================================================================================
     #=======================================================================
     #===================================================
     #=====================================Teacher Window+====================================================
     #===================================================
     #===================================================================  
       
    def Student_detail_window(self):
       self.root1=Toplevel()
       self.root1.title("Student Details")
       self.root1.geometry("1000x800+495+150")
       
       self.root1.config(bg="white")
       self.root1.focus_force()
       self.root1.grab_set()
       
       title=Label(self.root1,text="Student Detail",bd=10,font=("times new roman",45,"bold"),bg="white",fg="#031F3C")
        
       
       Manage_Frame=Frame(self.root1,bd=4,relief=RIDGE,bg="#08A3D2")
       Manage_Frame.place(x=10,y=20,width=750,height=900)
       
       m_title=Label(Manage_Frame,text="Manage Students",bg="#08A3D2",fg="white",width=20,font=("times new roman",40,"bold"))
       m_title.grid(row=0,columnspan=10,pady=20,padx=40)
       
       
       lbl_roll=Label(Manage_Frame,text="Roll No.",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_roll.grid(row=1,column=0,pady=20,padx=40,sticky="w")
       
       txt_roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",20,"bold"))
       txt_roll.grid(row=1,column=1,pady=20,padx=40,sticky="w")
       
       lbl_name=Label(Manage_Frame,text="Name",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_name.grid(row=2,column=0,pady=20,padx=40,sticky="w")
       
       txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",20,"bold"))
       txt_name.grid(row=2,column=1,pady=20,padx=40,sticky="w")
       
       lbl_email=Label(Manage_Frame,text="Email",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_email.grid(row=3,column=0,pady=20,padx=40,sticky="w")
       
       txt_email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",20,"bold"))
       txt_email.grid(row=3,column=1,pady=20,padx=40,sticky="w")
       
       lbl_gender=Label(Manage_Frame,text="Gender",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_gender.grid(row=4,column=0,pady=20,padx=40,sticky="w")
       
       combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",19,"bold"),state="readonly")
       combo_gender["values"]=["Male","Female","Other"]
       combo_gender.grid(row=4,column=1,pady=20,padx=40,sticky="w")
       
       lbl_contact=Label(Manage_Frame,text="Contact",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_contact.grid(row=5,column=0,pady=20,padx=40,sticky="w")
       
       txt_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",20,"bold"))
       txt_contact.grid(row=5,column=1,pady=20,padx=40,sticky="w")
       
       lbl_dob=Label(Manage_Frame,text="DOB",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_dob.grid(row=6,column=0,pady=20,padx=40,sticky="w")
       
       txt_dob=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",20,"bold"))
       txt_dob.grid(row=6,column=1,pady=20,padx=40,sticky="w")
   
       lbl_address=Label(Manage_Frame,text="Address",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_address.grid(row=7,column=0,pady=20,padx=40,sticky="w")
       
       self.txt_address=Text(Manage_Frame,width=35,height=4)
       self.txt_address.grid(row=7,column=1,pady=20,padx=40,sticky="w")
       
       
       
       #===================button frame===============
       btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="#08A3D2")
       btn_Frame.place(x=40,y=770,width=550)
       
       Addbtn=Button(btn_Frame,text="Add",width=15,command=self.add_student).grid(row=0,column=0,padx=10,pady=10)
       Updatebtn=Button(btn_Frame,text="Update",width=15,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
       Deletebtn=Button(btn_Frame,text="Delete",width=15,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
       Clearbtn=Button(btn_Frame,text="Clear",width=15,command=self.clear).grid(row=0,column=3,padx=10,pady=10)
       
       
        #=====Datail Frame==================
       detail_Frame=Frame(self.root1,bd=4,relief=RIDGE,bg="#08A3D2")
       detail_Frame.place(x=800,y=20,width=1100,height=900)
       
       lbl_search=Label(detail_Frame,text="Search By",bg="#08A3D2",fg="white",font=("times new roman",20,"bold"))
       lbl_search.grid(row=0,column=0,pady=50,padx=40,sticky="w")
       
       combo_search=ttk.Combobox(detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",20,"bold"),state="readonly")
       combo_search["values"]=["Roll","Name","contact"]
       combo_search.grid(row=0,column=1,pady=20,padx=30,sticky="w")
       
       txt_search=Entry(detail_Frame,textvariable=self.search_txt,width=18,font=("times new roman",20,"bold"))
       txt_search.grid(row=0,column=2,pady=20,padx=40,sticky="w")
       
       Searchbtn=Button(detail_Frame,text="Search",width=15,pady=5,command=self.search_data).grid(row=0,column=3,padx=20,pady=20)
       Showallbtn=Button(detail_Frame,text="Show All",width=15,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=20,pady=20)
       
        #===============================table frame====================
       
       Table_Frame=Frame(detail_Frame,bd=4,relief=RIDGE,bg="#08A3D2")
       Table_Frame.place(x=70,y=110,width=960,height=750)
       
       
       scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
       
       scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
       
       self.Student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       
       scroll_x.pack(side=BOTTOM,fill=X)
       scroll_y.pack(side=RIGHT,fill=Y)
       scroll_x.config(command= self.Student_table.xview)
       scroll_y.config(command= self.Student_table.yview)
       
       self.Student_table.heading("roll",text="Roll no.")
       self.Student_table.heading("name",text="Name")
       self.Student_table.heading("email",text="Email")
       self.Student_table.heading("gender",text="Gender")
       self.Student_table.heading("contact",text="Contact")
       self.Student_table.heading("dob",text="D.O.B")
       self.Student_table.heading("address",text="Address")
       
       
       self.Student_table["show"]="headings"
       
       
       self.Student_table.column("roll",width=130)
       self.Student_table.column("name",width=130)
       self.Student_table.column("email",width=130)
       self.Student_table.column("gender",width=130)
       self.Student_table.column("contact",width=130)
       self.Student_table.column("dob",width=130)
       self. Student_table.column("address",width=130)
       self.Student_table.pack(fill=BOTH,expand=1) 
       
       self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
       self.fetch_data()
       
    def add_student(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="Select" or self.contact_var.get()=="" or self.dob_var.get()=="":
                messagebox.showerror("Error","All Fields are required!!!")
        else:    
                conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
                my_cursur=conn.cursor()
                my_cursur.execute("insert into student_pro (Roll,Name,email,gender,contact,dob,address) values(%s,%s,%s,%s,%s,%s,%s)",
                                                                                                                               (self.Roll_No_var.get(),
                                                                                                                                self.name_var.get(),
                                                                                                                                self.email_var.get(),
                                                                                                                                self.gender_var.get(),
                                                                                                                                self.contact_var.get(),
                                                                                                                                self.dob_var.get(),
                                                                                                                                self.txt_address.get("1.0",END)
                                                                                                                               ))
                conn.commit()
                self.fetch_data()
                self.clear()
                conn.close()
                messagebox.showinfo("Success","Record Has Been Inserted")
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
        my_cursur=conn.cursor()
        my_cursur.execute("select * from student_pro")
        rows=my_cursur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            conn.commit()
        conn.close()    
        
    def clear(self): 
        self.Roll_No_var.set(""),
        self.name_var.set(""),
        self.email_var.set(""),
        self.gender_var.set(""),
        self.contact_var.set(""),
        self.dob_var.set(""),
        self.txt_address.delete("1.0",END)  
        
    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        content=self.Student_table.item(cursor_row)
        row=content['values']
        
        self.Roll_No_var.set(row[0]),
        self.name_var.set(row[1]),
        self.email_var.set(row[2]),
        self.gender_var.set(row[3]),
        self.contact_var.set(row[4]),
        self.dob_var.set(row[5]),
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])
        
    def update_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
        my_cursur=conn.cursor()
        my_cursur.execute("update student_pro set Name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where Roll=%s",
                                                                                    (self.name_var.get(),
                                                                                     self.email_var.get(),
                                                                                     self.gender_var.get(),
                                                                                     self.contact_var.get(),
                                                                                     self.dob_var.get(),
                                                                                     self.txt_address.get("1.0",END),
                                                                                     self.Roll_No_var.get()
                                                                                   ))
        conn.commit()
        self.fetch_data()
        self.clear()
        conn.close()   
        
    def delete_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
        my_cursur=conn.cursor()
        sql="delete from student_pro where Roll=%s"                  #==========when email & pass invalid=============
        value=(self.Roll_No_var.get(),)
        my_cursur.execute(sql,value)
        conn.commit()
        conn.close()
        self.fetch_data()
        self.clear()
        
    def search_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
        my_cursur=conn.cursor()
        my_cursur.execute("select * from student_pro where " +str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=my_cursur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            conn.commit()
        conn.close()   
           
     #==================================================================================================================
     #============================================================================================
     #=======================================================================
     #===================================================
     #=====================================Teacher Window+====================================================
     #===================================================
     #===================================================================
    def Teacher_detail_window(self):
       self.root2=Toplevel()
       self.root2.title("Teacher Details")
       self.root2.geometry("1000x800+495+150")
       
       self.root2.config(bg="white")
       self.root2.focus_force()
       self.root2.grab_set()
       
       title=Label(self.root2,text="Teacher Detail",bd=10,font=("times new roman",45,"bold"),bg="white",fg="#031F3C")
       
        
       Manage_Frame=Frame(self.root2,bd=4,relief=RIDGE,bg="#08A3D2")
       Manage_Frame.place(x=10,y=20,width=750,height=900)
      
       m_title=Label(Manage_Frame,text="Manage Teacher",bg="#08A3D2",fg="white",width=20,font=("times new roman",40,"bold"))
       m_title.grid(row=0,columnspan=10,pady=20,padx=40)
       
       lbl_teacher_id=Label(Manage_Frame,text="Teacher_id",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_teacher_id.grid(row=1,column=0,pady=20,padx=40,sticky="w")
       
       txt_teacher_id=Entry(Manage_Frame,textvariable=self.teacher_id_var,font=("times new roman",20,"bold"))
       txt_teacher_id.grid(row=1,column=1,pady=20,padx=40,sticky="w")
       
       
       
       lbl_name=Label(Manage_Frame,text="Name",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_name.grid(row=2,column=0,pady=20,padx=40,sticky="w")
       
       txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",20,"bold"))
       txt_name.grid(row=2,column=1,pady=20,padx=40,sticky="w")
       
       lbl_email=Label(Manage_Frame,text="Email",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_email.grid(row=3,column=0,pady=20,padx=40,sticky="w")
       
       txt_email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",20,"bold"))
       txt_email.grid(row=3,column=1,pady=20,padx=40,sticky="w")
       
       lbl_gender=Label(Manage_Frame,text="Gender",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_gender.grid(row=4,column=0,pady=20,padx=40,sticky="w")
       
       combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",19,"bold"),state="readonly")
       combo_gender["values"]=["Male","Female","Other"]
       combo_gender.grid(row=4,column=1,pady=20,padx=40,sticky="w")
       
       lbl_contact=Label(Manage_Frame,text="Contact",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_contact.grid(row=5,column=0,pady=20,padx=40,sticky="w")
       
       txt_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",20,"bold"))
       txt_contact.grid(row=5,column=1,pady=20,padx=40,sticky="w")
       
       lbl_subject=Label(Manage_Frame,text="Subject",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_subject.grid(row=6,column=0,pady=20,padx=40,sticky="w")
       
       txt_subject=Entry(Manage_Frame,textvariable=self.subject_var,font=("times new roman",20,"bold"))
       txt_subject.grid(row=6,column=1,pady=20,padx=40,sticky="w")
       
      
       
       lbl_dob=Label(Manage_Frame,text="DOB",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_dob.grid(row=7,column=0,pady=20,padx=40,sticky="w")
       
       txt_dob=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",20,"bold"))
       txt_dob.grid(row=7,column=1,pady=20,padx=40,sticky="w")
   
       lbl_address=Label(Manage_Frame,text="Address",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_address.grid(row=8,column=0,pady=20,padx=40,sticky="w")
       
       self.txt_address=Text(Manage_Frame,width=35,height=4)
       self.txt_address.grid(row=8,column=1,pady=20,padx=40,sticky="w")
       
        #===================button frame===============
       btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="#08A3D2")
       btn_Frame.place(x=40,y=770,width=550)
       
       Addbtn=Button(btn_Frame,text="Add",width=15,command=self.add_Teacher).grid(row=0,column=0,padx=10,pady=10)
       Updatebtn=Button(btn_Frame,text="Update",width=15,command=self.teacher_update_data).grid(row=0,column=1,padx=10,pady=10)
       Deletebtn=Button(btn_Frame,text="Delete",width=15,command=self.teacher_delete_data).grid(row=0,column=2,padx=10,pady=10)
       Clearbtn=Button(btn_Frame,text="Clear",width=15,command=self.teacherclear).grid(row=0,column=3,padx=10,pady=10)
       
       
         #=====Datail Frame==================
       detail_Frame=Frame(self.root2,bd=4,relief=RIDGE,bg="#08A3D2")
       detail_Frame.place(x=800,y=20,width=1100,height=900)
       
       lbl_search=Label(detail_Frame,text="Search By",bg="#08A3D2",fg="white",font=("times new roman",20,"bold"))
       lbl_search.grid(row=0,column=0,pady=50,padx=40,sticky="w")
       
       combo_search=ttk.Combobox(detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",20,"bold"),state="readonly")
       combo_search["values"]=["teacher_id","Name","contact"]
       combo_search.grid(row=0,column=1,pady=20,padx=30,sticky="w")
       
       txt_search=Entry(detail_Frame,textvariable=self.search_txt,width=18,font=("times new roman",20,"bold"))
       txt_search.grid(row=0,column=2,pady=20,padx=40,sticky="w")
       
       Searchbtn=Button(detail_Frame,text="Search",width=15,pady=5,command=self.teacher_search_data).grid(row=0,column=3,padx=20,pady=20)
       Showallbtn=Button(detail_Frame,text="Show All",width=15,pady=5,command=self. fetchteacher_data).grid(row=0,column=4,padx=20,pady=20)
       
        #===============================table frame====================
       
       Table_Frame=Frame(detail_Frame,bd=4,relief=RIDGE,bg="#08A3D2")
       Table_Frame.place(x=70,y=110,width=960,height=750)
       
       
       scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
       
       scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
       
       self.Teacher_table=ttk.Treeview(Table_Frame,columns=("teacher_id","name","email","gender","contact","subject","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       
       scroll_x.pack(side=BOTTOM,fill=X)
       scroll_y.pack(side=RIGHT,fill=Y)
       scroll_x.config(command= self.Teacher_table.xview)
       scroll_y.config(command= self.Teacher_table.yview)
       
       self.Teacher_table.heading("teacher_id",text="Teacher_id")
       self.Teacher_table.heading("name",text="Name")
       self.Teacher_table.heading("email",text="Email")
       self.Teacher_table.heading("gender",text="Gender")
       self.Teacher_table.heading("contact",text="Contact")
       self.Teacher_table.heading("subject",text="Subject")
       self.Teacher_table.heading("dob",text="D.O.B")
       self.Teacher_table.heading("address",text="Address")
       
       
       self.Teacher_table["show"]="headings"
       
       
       self.Teacher_table.column("teacher_id",width=130)
       self.Teacher_table.column("name",width=130)
       self.Teacher_table.column("email",width=130)
       self.Teacher_table.column("gender",width=130)
       self.Teacher_table.column("contact",width=130)
       self.Teacher_table.column("subject",width=130)
       self.Teacher_table.column("dob",width=130)
       self.Teacher_table.column("address",width=130)
       self.Teacher_table.pack(fill=BOTH,expand=1) 
       
       self.Teacher_table.bind("<ButtonRelease-1>",self.teacherget_cursor)
       self.fetchteacher_data()
       
    def add_Teacher(self):
        if self.teacher_id_var.get()=="" or  self.name_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="Select" or self.contact_var.get()=="" or self.dob_var.get()=="":
                messagebox.showerror("Error","All Fields are required!!!")
        else:    
                conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
                my_cursur=conn.cursor()
                my_cursur.execute("insert into teachers_pro (teacher_id,Name,email,gender,contact,subject,dob,address) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                                                                                                                               (self.teacher_id_var.get(),
                                                                                                                                self.name_var.get(),
                                                                                                                                self.email_var.get(),
                                                                                                                                self.gender_var.get(),
                                                                                                                                self.contact_var.get(),
                                                                                                                                self.subject_var.get(),
                                                                                                                                self.dob_var.get(),
                                                                                                                                self.txt_address.get("1.0",END)
                                                                                                                               ))
                conn.commit()
                self.fetchteacher_data()
                self.teacherclear()
                conn.close()
                messagebox.showinfo("Success","Record Has Been Inserted")
                
                
    def fetchteacher_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
        my_cursur=conn.cursor()
        my_cursur.execute("select * from teachers_pro")
        rows=my_cursur.fetchall()
        if len(rows)!=0:
            self.Teacher_table.delete(*self.Teacher_table.get_children())
            for row in rows:
                self.Teacher_table.insert('',END,values=row)
            conn.commit()
        conn.close()    
        
    def teacherclear(self): 
        self.teacher_id_var.set(""),
        self.name_var.set(""),
        self.email_var.set(""),
        self.gender_var.set(""),
        self.contact_var.set(""),
        self.subject_var.set(""),
        self.dob_var.set(""),
        self.txt_address.delete("1.0",END)  
        
    def teacherget_cursor(self,ev):
        cursor_row=self.Teacher_table.focus()
        content=self.Teacher_table.item(cursor_row)
        row=content['values']
        
        self.teacher_id_var.set(row[0]),
        self.name_var.set(row[1]),
        self.email_var.set(row[2]),
        self.gender_var.set(row[3]),
        self.contact_var.set(row[4]),
        self.subject_var.set(row[5]),
        self.dob_var.set(row[6]),
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[7])
        
    def teacher_update_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
        my_cursur=conn.cursor()
        my_cursur.execute("update teachers_pro set Name=%s,email=%s,gender=%s,contact=%s,subject=%s,dob=%s,address=%s where teacher_id=%s",
                                                                                    (self.name_var.get(),
                                                                                     self.email_var.get(),
                                                                                     self.gender_var.get(),
                                                                                     self.contact_var.get(),
                                                                                     self.subject_var.get(),
                                                                                     self.dob_var.get(),
                                                                                     self.txt_address.get("1.0",END),
                                                                                     self.teacher_id_var.get()
                                                                                   ))
        conn.commit()
        self.fetchteacher_data()
        self.teacherclear()
        conn.close()   
        
    def teacher_delete_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
        my_cursur=conn.cursor()
        sql="delete from teachers_pro where teacher_id=%s"                  #==========when email & pass invalid=============
        value=(self.teacher_id_var.get(),)
        my_cursur.execute(sql,value)
        conn.commit()
        conn.close()
        self.fetchteacher_data()
        self.teacherclear()
        
    def teacher_search_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
        my_cursur=conn.cursor()
        my_cursur.execute("select * from teachers_pro where " +str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=my_cursur.fetchall()
        if len(rows)!=0:
            self.Teacher_table.delete(*self.Teacher_table.get_children())
            for row in rows:
                self.Teacher_table.insert('',END,values=row)
            conn.commit()
        conn.close()             
                
    #==================================================================================================================
     #============================================================================================
     #=======================================================================
     #===================================================
     #=====================================Staff Window+====================================================
     #===================================================
     #===================================================================            
                
    def Worker_detail_window(self):
       self.root3=Toplevel()
       self.root3.title("Workers Details")
       self.root3.geometry("1000x800+495+150")
       
       self.root3.config(bg="white")
       self.root3.focus_force()
       self.root3.grab_set()
       
       title=Label(self.root3,text="Workers Detail",bd=10,font=("times new roman",45,"bold"),bg="white",fg="#031F3C")
       
        
       Manage_Frame=Frame(self.root3,bd=4,relief=RIDGE,bg="#08A3D2")
       Manage_Frame.place(x=10,y=20,width=750,height=900)
      
       m_title=Label(Manage_Frame,text="Manage Worker",bg="#08A3D2",fg="white",width=20,font=("times new roman",40,"bold"))
       m_title.grid(row=0,columnspan=10,pady=20,padx=40)
       
       lbl_worker_id=Label(Manage_Frame,text="Worker_id",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_worker_id.grid(row=1,column=0,pady=20,padx=40,sticky="w")
       
       txt_worker_id=Entry(Manage_Frame,textvariable=self.worker_id_var,font=("times new roman",20,"bold"))
       txt_worker_id.grid(row=1,column=1,pady=20,padx=40,sticky="w")
       
       lbl_name=Label(Manage_Frame,text="Name",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_name.grid(row=2,column=0,pady=20,padx=40,sticky="w")
       
       txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",20,"bold"))
       txt_name.grid(row=2,column=1,pady=20,padx=40,sticky="w")
       
      
       lbl_gender=Label(Manage_Frame,text="Gender",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_gender.grid(row=3,column=0,pady=20,padx=40,sticky="w")
       
       combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",19,"bold"),state="readonly")
       combo_gender["values"]=["Male","Female","Other"]
       combo_gender.grid(row=3,column=1,pady=20,padx=40,sticky="w")
       
       lbl_contact=Label(Manage_Frame,text="Contact",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_contact.grid(row=4,column=0,pady=20,padx=40,sticky="w")
       
       txt_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",20,"bold"))
       txt_contact.grid(row=4,column=1,pady=20,padx=40,sticky="w")
       
       lbl_work=Label(Manage_Frame,text="Work",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_work.grid(row=5,column=0,pady=20,padx=40,sticky="w")
        
       combo_work=ttk.Combobox(Manage_Frame,textvariable=self.work_var,font=("times new roman",19,"bold"),state="readonly")
       combo_work["values"]=["Peon","Bus Driver","sweeper","other"]
       combo_work.grid(row=5,column=1,pady=20,padx=40,sticky="w")
       
      
       
       lbl_dob=Label(Manage_Frame,text="DOB",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_dob.grid(row=6,column=0,pady=20,padx=40,sticky="w")
       
       txt_dob=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",20,"bold"))
       txt_dob.grid(row=6,column=1,pady=20,padx=40,sticky="w")
    
       lbl_address=Label(Manage_Frame,text="Address",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_address.grid(row=7,column=0,pady=20,padx=40,sticky="w")
       
       self.txt_address=Text(Manage_Frame,width=35,height=4)
       self.txt_address.grid(row=7,column=1,pady=20,padx=40,sticky="w")  
       
       lbl_salary=Label(Manage_Frame,text="Salary",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_salary.grid(row=8,column=0,pady=20,padx=40,sticky="w")
       
       txt_salary=Entry(Manage_Frame,textvariable=self.salary_var,font=("times new roman",20,"bold"))
       txt_salary.grid(row=8,column=1,pady=20,padx=40,sticky="w")      
       
        
        #===================button frame===============
       btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="#08A3D2")
       btn_Frame.place(x=40,y=770,width=550)
       
       Addbtn=Button(btn_Frame,text="Add",width=15,command=self.add_Worker).grid(row=0,column=0,padx=10,pady=10)
       Updatebtn=Button(btn_Frame,text="Update",width=15,command=self.worker_update_data).grid(row=0,column=1,padx=10,pady=10)
       Deletebtn=Button(btn_Frame,text="Delete",width=15,command=self.worker_delete_data).grid(row=0,column=2,padx=10,pady=10)
       Clearbtn=Button(btn_Frame,text="Clear",width=15,command=self.workerclear).grid(row=0,column=3,padx=10,pady=10)
       
       
         #=====Datail Frame==================
       detail_Frame=Frame(self.root3,bd=4,relief=RIDGE,bg="#08A3D2")
       detail_Frame.place(x=800,y=20,width=1100,height=900)
       
       lbl_search=Label(detail_Frame,text="Search By",bg="#08A3D2",fg="white",font=("times new roman",20,"bold"))
       lbl_search.grid(row=0,column=0,pady=50,padx=40,sticky="w")
       
       combo_search=ttk.Combobox(detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",20,"bold"),state="readonly")
       combo_search["values"]=["worker_id","Name","contact"]
       combo_search.grid(row=0,column=1,pady=20,padx=30,sticky="w")
       
       txt_search=Entry(detail_Frame,textvariable=self.search_txt,width=18,font=("times new roman",20,"bold"))
       txt_search.grid(row=0,column=2,pady=20,padx=40,sticky="w")
       
       Searchbtn=Button(detail_Frame,text="Search",width=15,pady=5,command=self.worker_search_data).grid(row=0,column=3,padx=20,pady=20)
       Showallbtn=Button(detail_Frame,text="Show All",width=15,pady=5,command=self.fetchworker_data).grid(row=0,column=4,padx=20,pady=20)
           
                   
        #===============================table frame====================
       
       Table_Frame=Frame(detail_Frame,bd=4,relief=RIDGE,bg="#08A3D2")
       Table_Frame.place(x=70,y=110,width=960,height=750)
       
       
       scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
       
       scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
       
       self.Worker_table=ttk.Treeview(Table_Frame,columns=("worker_id","name","gender","contact","work","dob","address","salary"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       
       scroll_x.pack(side=BOTTOM,fill=X)
       scroll_y.pack(side=RIGHT,fill=Y)
       scroll_x.config(command= self.Worker_table.xview)
       scroll_y.config(command= self.Worker_table.yview)
       
       self.Worker_table.heading("worker_id",text="Worker_id")
       self.Worker_table.heading("name",text="Name")
       self.Worker_table.heading("gender",text="Gender")
       self.Worker_table.heading("contact",text="Contact")
       self.Worker_table.heading("work",text="Work")
       self.Worker_table.heading("dob",text="D.O.B")
       self.Worker_table.heading("address",text="Address")
       self.Worker_table.heading("salary",text="Salary")
       
       
       self.Worker_table["show"]="headings"
       
       
       self.Worker_table.column("worker_id",width=130)
       self.Worker_table.column("name",width=130)
       self.Worker_table.column("gender",width=130)
       self.Worker_table.column("contact",width=130)
       self.Worker_table.column("work",width=130)
       self.Worker_table.column("dob",width=130)
       self.Worker_table.column("address",width=130)
       self.Worker_table.column("salary",width=130)
       self.Worker_table.pack(fill=BOTH,expand=1) 
       
       self.Worker_table.bind("<ButtonRelease-1>",self.workerget_cursor)
       self.fetchworker_data()
       
    def add_Worker(self):
        if self.worker_id_var.get()=="" or  self.name_var.get()==""  or self.contact_var.get()=="" or self.work_var.get()=="" or self.dob_var.get()=="" or self.salary_var.get()== "":
                messagebox.showerror("Error","All Fields are required!!!")
        else:    
                conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
                my_cursur=conn.cursor()
                my_cursur.execute("insert into worker (worker_id,Name,gender,contact,work,dob,address,salary) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                                                                                                                               (self.worker_id_var.get(),
                                                                                                                                self.name_var.get(),
                                                                                                                                self.gender_var.get(),
                                                                                                                                self.contact_var.get(),
                                                                                                                                self.work_var.get(),
                                                                                                                                self.dob_var.get(),
                                                                                                                                self.txt_address.get("1.0",END),
                                                                                                                                self.salary_var.get()
                                                                                                                               ))
                conn.commit()
                self.fetchworker_data()
                self.workerclear()
                conn.close()
                messagebox.showinfo("Success","Record Has Been Inserted")
                  
       
    def fetchworker_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
        my_cursur=conn.cursor()
        my_cursur.execute("select * from worker")
        rows=my_cursur.fetchall()
        if len(rows)!=0:
            self.Worker_table.delete(*self.Worker_table.get_children())
            for row in rows:
                self.Worker_table.insert('',END,values=row)
            conn.commit()
        conn.close()    
        
    def workerclear(self): 
        self.worker_id_var.set(""),
        self.name_var.set(""),
        self.gender_var.set(""),
        self.contact_var.set(""),
        self.work_var.set(""),
        self.dob_var.set(""),
        self.txt_address.delete("1.0",END)  
        self.salary_var.set(""),
        
        
    def workerget_cursor(self,ev):
        cursor_row=self.Worker_table.focus()
        content=self.Worker_table.item(cursor_row)
        row=content['values']
        
        self.worker_id_var.set(row[0]),
        self.name_var.set(row[1]),
        self.gender_var.set(row[2]),
        self.contact_var.set(row[3]),
        self.work_var.set(row[4]),
        self.dob_var.set(row[5]),
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])
        self.salary_var.set(row[7]),
        
      
    def worker_update_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
        my_cursur=conn.cursor()
        my_cursur.execute("update worker set Name=%s,gender=%s,contact=%s,work=%s,dob=%s,address=%s,salary=%s where worker_id=%s",
                                                                                    (self.name_var.get(),
                                                                                     self.gender_var.get(),
                                                                                     self.contact_var.get(),
                                                                                     self.work_var.get(),
                                                                                     self.dob_var.get(),
                                                                                     self.txt_address.get("1.0",END),
                                                                                     self.salary_var.get(),
                                                                                     self.worker_id_var.get()
                                                                                    ))
        conn.commit()
        self.fetchworker_data()
        self.workerclear()
        conn.close()   
        
    def worker_delete_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
        my_cursur=conn.cursor()
        sql="delete from worker where worker_id=%s"                  #==========when email & pass invalid=============
        value=(self.worker_id_var.get(),)
        my_cursur.execute(sql,value)
        conn.commit()
        conn.close()
        self.fetchworker_data()
        self.workerclear()
        
    def worker_search_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
        my_cursur=conn.cursor()
        my_cursur.execute("select * from worker where " +str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=my_cursur.fetchall()
        if len(rows)!=0:
            self.Worker_table.delete(*self.Worker_table.get_children())
            for row in rows:
                self.Worker_table.insert('',END,values=row)
            conn.commit()
        conn.close()     
    
       
    
    #==================================================================================================================
     #============================================================================================
     #=======================================================================
     #===================================================
     #=====================================Staff Window+====================================================
     #===================================================
     #===================================================================  
        
    def Time_Table_window(self):
       self.root4=Toplevel()
       self.root4.title("Time Table")
       self.root4.geometry("800x800+495+150")
       
       self.root4.config(bg="white")
       self.root4.focus_force()
       self.root4.grab_set()
       
       title=Label(self.root4,text="Time Table",bd=10,font=("times new roman",45,"bold"),bg="white",fg="#031F3C")   
       
       
       Manage_Frame=Frame(self.root4,bd=4,relief=RIDGE,bg="#08A3D2")
       Manage_Frame.place(x=10,y=20,width=750,height=900)
      
       m_title=Label(Manage_Frame,text="Student Time Table",bg="#08A3D2",fg="white",width=20,font=("times new roman",40,"bold"))
       m_title.grid(row=0,columnspan=10,pady=20,padx=20)
       
       
      
       lbl_day=Label(Manage_Frame,text="Day",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_day.grid(row=1,column=0,pady=20,padx=40,sticky="w")
       
       combo_day=ttk.Combobox(Manage_Frame,textvariable=self.day_var,font=("times new roman",19,"bold"),state="readonly")
       combo_day["values"]=["Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday","Sunday"]
       combo_day.grid(row=1,column=1,pady=20,padx=40,sticky="w")
       
       lbl_time=Label(Manage_Frame,text="8:30-9:15",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_time.grid(row=2,column=0,pady=20,padx=40,sticky="w")
        
       combo_time=ttk.Combobox(Manage_Frame,textvariable=self.time_var,font=("times new roman",19,"bold"),state="readonly")
       combo_time["values"]=["Science","English","Maths","Computer","Hindi","Social Science"]
       combo_time.grid(row=2,column=1,pady=20,padx=40,sticky="w")
       
       lbl_time1=Label(Manage_Frame,text="9:15-9:45",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_time1.grid(row=3,column=0,pady=20,padx=40,sticky="w")
        
       combo_time1=ttk.Combobox(Manage_Frame,textvariable=self.time1_var,font=("times new roman",19,"bold"),state="readonly")
       combo_time1["values"]=["Science","English","Maths","Computer","Hindi","Social Science","other"]
       combo_time1.grid(row=3,column=1,pady=20,padx=40,sticky="w")
       
       lbl_time2=Label(Manage_Frame,text="9:45-10:30",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_time2.grid(row=4,column=0,pady=20,padx=40,sticky="w")
        
       combo_time2=ttk.Combobox(Manage_Frame,textvariable=self.time2_var,font=("times new roman",19,"bold"),state="readonly")
       combo_time2["values"]=["Science","English","Maths","Computer","Hindi","Social Science","other"]
       combo_time2.grid(row=4,column=1,pady=20,padx=40,sticky="w")
       
       lbl_time4=Label(Manage_Frame,text="11:30-12:15",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_time4.grid(row=5,column=0,pady=20,padx=40,sticky="w")
        
       combo_time4=ttk.Combobox(Manage_Frame,textvariable=self.time4_var,font=("times new roman",19,"bold"),state="readonly")
       combo_time4["values"]=["Science","English","Maths","Computer","Hindi","Social Science","other"]
       combo_time4.grid(row=5,column=1,pady=20,padx=40,sticky="w")
       
       
       lbl_time5=Label(Manage_Frame,text="12:15-1:00",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_time5.grid(row=6,column=0,pady=20,padx=40,sticky="w")
        
       combo_time5=ttk.Combobox(Manage_Frame,textvariable=self.time5_var,font=("times new roman",19,"bold"),state="readonly")
       combo_time5["values"]=["Science","English","Maths","Computer","Hindi","Social Science","other"]
       combo_time5.grid(row=6,column=1,pady=20,padx=40,sticky="w")
       
       lbl_time6=Label(Manage_Frame,text="1:00-1:45",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_time6.grid(row=7,column=0,pady=20,padx=40,sticky="w")
        
       combo_time6=ttk.Combobox(Manage_Frame,textvariable=self.time6_var,font=("times new roman",19,"bold"),state="readonly")
       combo_time6["values"]=["Science","English","Maths","Computer","Hindi","Social Science","other"]
       combo_time6.grid(row=7,column=1,pady=20,padx=40,sticky="w")
       
       lbl_time7=Label(Manage_Frame,text="1:45-2:30",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_time7.grid(row=8,column=0,pady=20,padx=40,sticky="w")
        
       combo_time7=ttk.Combobox(Manage_Frame,textvariable=self.time7_var,font=("times new roman",19,"bold"),state="readonly")
       combo_time7["values"]=["Science","English","Maths","Computer","Hindi","Social Science","other"]
       combo_time7.grid(row=8,column=1,pady=20,padx=40,sticky="w")
       
         #===================button frame===============
       btn_Frame=Frame(Manage_Frame,relief=RIDGE,bg="#08A3D2")
       btn_Frame.place(x=40,y=820,width=550,height=50)
       
       Addbtn=Button(btn_Frame,text="Add",width=15,command=self.add_Timetable).grid(row=0,column=0,padx=10,pady=10)
       Updatebtn=Button(btn_Frame,text="Update",width=15,command=self.timetable_update_data).grid(row=0,column=1,padx=10,pady=10)
       Deletebtn=Button(btn_Frame,text="Delete",width=15,command=self.timetable_delete_data).grid(row=0,column=2,padx=10,pady=10)
       Clearbtn=Button(btn_Frame,text="Clear",width=15,command=self.timetableclear).grid(row=0,column=3,padx=10,pady=10)
       
       
         #=====Datail Frame==================
       detail_Frame=Frame(self.root4,bd=4,relief=RIDGE,bg="#08A3D2")
       detail_Frame.place(x=800,y=20,width=1100,height=900)
       
      #===================table frame================
       
       Table_Frame=Frame(detail_Frame,bd=4,relief=RIDGE,bg="#08A3D2")
       Table_Frame.place(x=00,y=0,width=1090,height=890)
       
       
       scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
       
       scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
       
       self.Timetable_table=ttk.Treeview(Table_Frame,columns=("day","time","time1","time2","time4","time5","time6","time7"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       
       scroll_x.pack(side=BOTTOM,fill=X)
       scroll_y.pack(side=RIGHT,fill=Y)
       scroll_x.config(command= self.Timetable_table.xview)
       scroll_y.config(command= self.Timetable_table.yview)
       
       self.Timetable_table.heading("day",text="Day")
       self.Timetable_table.heading("time",text="8:30-9:15")
       self.Timetable_table.heading("time1",text="9:15-9:45")
       self.Timetable_table.heading("time2",text="9:45-10:30")
       self.Timetable_table.heading("time4",text="11:30-12:15")
       self.Timetable_table.heading("time5",text="12:15-01:00")
       self.Timetable_table.heading("time6",text="01:00-01:45")
       self.Timetable_table.heading("time7",text="01:45-2:30")
       
       
       self.Timetable_table["show"]="headings"
       
       
       self.Timetable_table.column("day",width=130)
       self.Timetable_table.column("time",width=130)
       self.Timetable_table.column("time1",width=130)
       self.Timetable_table.column("time2",width=130)
       self.Timetable_table.column("time4",width=130)
       self.Timetable_table.column("time5",width=130)
       self.Timetable_table.column("time6",width=130)
       self.Timetable_table.column("time7",width=130)
       self.Timetable_table.pack(fill=BOTH,expand=1) 
       
       self.Timetable_table.bind("<ButtonRelease-1>",self.timetableget_cursor)
       self.fetchtimetable_data()
       
       
       
    def add_Timetable(self):
        if self.day_var.get()=="" or  self.time_var.get()==""  or self.time1_var.get()=="" or self.time2_var.get()=="" or self.time5_var.get()=="" or self.time4_var.get()== "":
                messagebox.showerror("Error","All Fields are required!!!",parent=self.roo4)
        else:    
                conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
                my_cursur=conn.cursor()
                my_cursur.execute("insert into TT (day,time,time1,time2,time4,time5,time6,time7) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                                                                                                                               (self.day_var.get(),
                                                                                                                                self.time_var.get(),
                                                                                                                                self.time1_var.get(),
                                                                                                                                self.time2_var.get(),
                                                                                                                                self.time4_var.get(),
                                                                                                                                self.time5_var.get(),
                                                                                                                                self.time6_var.get(),
                                                                                                                                self.time7_var.get()
                                                                                                                               ))
                conn.commit()
                self.fetchtimetable_data()
                self.timetableclear()
                conn.close()
                messagebox.showinfo("Success","Record Has Been Inserted")   
       
       
            
    def fetchtimetable_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
        my_cursur=conn.cursor()
        my_cursur.execute("select * from TT")
        rows=my_cursur.fetchall()
        if len(rows)!=0:
            self.Timetable_table.delete(*self.Timetable_table.get_children())
            for row in rows:
                self.Timetable_table.insert('',END,values=row)
            conn.commit()
        conn.close()    
         
    def timetableclear(self): 
        self.day_var.set(""),
        self.time_var.set(""),
        self.time1_var.set(""),
        self.time2_var.set(""),
        self.time4_var.set(""),
        self.time5_var.set(""),
        self.time6_var.set(""),
        self.time7_var.set(""),
        
    def timetableget_cursor(self,ev):
        cursor_row=self.Timetable_table.focus()
        content=self.Timetable_table.item(cursor_row)
        row=content['values']
        
        self.day_var.set(row[0]),
        self.time_var.set(row[1]),
        self.time1_var.set(row[2]),
        self.time2_var.set(row[3]),
        self.time4_var.set(row[4]),
        self.time5_var.set(row[5]),
        self.time6_var.set(row[6]),
        self.time7_var.set(row[7]),
        
    def timetable_update_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
        my_cursur=conn.cursor()
        my_cursur.execute("update TT set ,time=%s,time1=%s,time2=%s,time4=%s,time5=%s,time6=%s,time where day=%s",
                                                                                    (self.time_var.get(),
                                                                                     self.time1_var.get(),
                                                                                     self.time2_var.get(),
                                                                                     self.time4_var.get(),
                                                                                     self.time5_var.get(),
                                                                                     self.time6_var.get(),
                                                                                     self.time7_var.get(),
                                                                                     self.day_var.get()
                                                                                    ))
        conn.commit()
        self.fetchtimetable_data()
        self.timetableclear()
        conn.close()   
        
    def timetable_delete_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
        my_cursur=conn.cursor()
        sql="delete from TT where day=%s"                  #==========when email & pass invalid=============
        value=(self.day_var.get(),)
        my_cursur.execute(sql,value)
        conn.commit()
        conn.close()
        self.fetchtimetable_data()
        self.timetableclear()
        
    
         
root=Tk()
ob=Student(root)
root.mainloop()