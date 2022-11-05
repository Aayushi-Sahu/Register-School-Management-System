from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from typing import TextIO
import mysql.connector

class Worker:
    def __init__(self,root):
       self.root3=root
       self.root3.title("Worker Detail")
       self.root3.geometry("1352x700+0+0")
       
       title=Label(self.root3,text="Worker Detail",bd=10,font=("times new roman",45,"bold"),bg="#08A3D2",fg="#031F3C")
       title.pack(side=TOP,fill=X)
       
       #=============all variable==========
       self.work_var=StringVar()
       self.worker_id_var=StringVar()
       self.name_var=StringVar()
       self.email_var=StringVar()
       self.gender_var=StringVar()
       self.contact_var=StringVar()
       self.dob_var=StringVar()
       self.salary_var=StringVar()
       self.search_by=StringVar()
       self.search_txt=StringVar()
       
       
       
       backgout_btn=Button(self.root3,text="Back",font=("times new roman",15,"bold"),bg="white",fg="#031F3C",bd=0,cursor="hand2").place(x=1780,y=18,width=100,height=40)
       Manage_Frame=Frame(self.root3,bd=4,relief=RIDGE,bg="#08A3D2")
       Manage_Frame.place(x=20,y=100,width=750,height=900)
      
       m_title=Label(Manage_Frame,text="Manage Worker",bg="#08A3D2",fg="white",width=20,font=("times new roman",40,"bold"))
       m_title.grid(row=0,columnspan=10,pady=20,padx=40)
       
       lbl_worker_id=Label(Manage_Frame,text="Worker_id",bg="#08A3D2",fg="white",width=10,font=("times new roman",20,"bold"))
       lbl_worker_id.grid(row=1,column=0,pady=20,padx=40,sticky="w")
       
       self.txt_worker_id=Entry(Manage_Frame,textvariable=self.worker_id_var,font=("times new roman",20,"bold"))
       self.txt_worker_id.grid(row=1,column=1,pady=20,padx=40,sticky="w")
       
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
       detail_Frame.place(x=800,y=100,width=1100,height=900)
       
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
            try:   
                conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
                my_cursur=conn.cursor()
                sql="select * from worker where worker_id=%s"                  #==========when email & pass invalid=============
                value=(self.worker_id_var.get(),)
                my_cursur.execute(sql,value)
                row=my_cursur.fetchone()
                #print(row)
                if row!=None:
                    messagebox.showerror("Error","worker id already exists")
                else:
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
            except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)}")       
       
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
        self.txt_worker_id.config(state=NORMAL)
        
    def workerget_cursor(self,ev):
        self.txt_worker_id.config(state='readonly')
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
        messagebox.showinfo("Success","Record Update Successfully")
    def worker_delete_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
        my_cursur=conn.cursor()
        sql="delete from worker where worker_id=%s"                  #==========when email & pass invalid=============
        value=(self.worker_id_var.get(),)
        my_cursur.execute(sql,value)
        conn.commit()
        conn.close()
        messagebox.showinfo("Delete","Record Has Been Deleted")
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
        
           
root=Tk()
ob=Worker(root)
root.mainloop()     