from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from typing import TextIO
import mysql.connector


class Timetable:
    def __init__(self,root):
       self.root4=root
       self.root4.title("Timetable")
       self.root4.geometry("1352x700+0+0")
       
       title=Label(self.root4,text="Timetable",bd=10,font=("times new roman",45,"bold"),bg="#08A3D2",fg="#031F3C")
       title.pack(side=TOP,fill=X)
         #=============================================
         #============all Variable==========#========
         #================
       self.day_var=StringVar()
       self.time_var=StringVar()
       self.time1_var=StringVar()
       self.time2_var=StringVar()
       self.time4_var=StringVar()      
       self.time5_var=StringVar()
       self.time6_var=StringVar()
       self.time7_var=StringVar()
       
       
       
       backgout_btn=Button(self.root4,text="Back",font=("times new roman",15,"bold"),command=self.back_window,bg="white",fg="#031F3C",bd=0,cursor="hand2").place(x=1780,y=18,width=100,height=40)   
       Manage_Frame=Frame(self.root4,bd=4,relief=RIDGE,bg="#08A3D2")
       Manage_Frame.place(x=20,y=100,width=750,height=900)
      
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
       detail_Frame.place(x=800,y=100,width=1100,height=900)
       
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
       
    def back_window(self):     
           self.root4.destroy()
           import dashboard 
           
             
       
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
        my_cursur.execute("update TT set time=%s,time1=%s,time2=%s,time4=%s,time5=%s,time6=%s,time7=%s where day=%s",
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
ob=Timetable(root)
root.mainloop()     