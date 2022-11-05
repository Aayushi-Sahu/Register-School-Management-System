from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from typing import TextIO
import mysql.connector

class cc:
    def __init__(self,root):
       self.root=root
       self.root.title("Classes")
       self.root.geometry("1200x480+80+170")
       
       title=Label(self.root,text="Classes Detail",bd=10,font=("times new roman",30,"bold"),bg="#08A3D2",fg="#031F3C")
       title.pack(side=TOP,fill=X)  
       
       
       #==================================
       #===================================
       #============Variable=============
       #-============
       self.var_class=StringVar()
       self.var_fees=StringVar()  
       
       backgout_btn=Button(self.root,text="Back",font=("times new roman",15,"bold"),command=self.back_window,bg="white",fg="#031F3C",bd=0,cursor="hand2").place(x=1780,y=18,width=100,height=40)
        #==================================
        #===========================
        #===========================label==========
       lbl_class=Label(self.root,text="Classes",font=("times new roman",20,"bold"),bg="white").place(x=25,y=150) 
       lbl_fees=Label(self.root,text="Fees",font=("times new roman",20,"bold"),bg="white").place(x=25,y=230)
       lbl_description=Label(self.root,text="Description",font=("times new roman",20,"bold"),bg="white").place(x=25,y=310) 
       
       #==================================
        #===========================
        #===========================entry==========
       self.txt_class=Entry(self.root,textvariable=self.var_class,font=("times new roman",18),bg="lightyellow")
       self.txt_class.place(x=300,y=150,width=330)
       
       txt_fees=Entry(self.root,textvariable=self.var_fees,font=("times new roman",18),bg="lightyellow").place(x=300,y=230,width=330)
       
       self.txt_description=Text(self.root,font=("times new roman",18),bg="lightyellow")
       self.txt_description.place(x=300,y=310,width=500,height=100)
       
       #==================================
        #===========================
        #==========================button==========
       self.btn_add=Button(self.root,text="Save",font=("timesself.newself.roman",15,"bold"),fg="white",bg="#2196f3",cursor="hand2",command=self.add)
       self.btn_add.place(x=300,y=500,width=110,height=40)
       self.btn_update=Button(self.root,text="Update",font=("times new roman",15,"bold"),fg="white",bg="#4caf50",cursor="hand2",command=self.update_data)
       self.btn_update.place(x=420,y=500,width=110,height=40)
       self.btn_delete=Button(self.root,text="Delete",font=("times new roman",15,"bold"),fg="white",bg="#f44336",cursor="hand2",command=self.delete_data)
       self.btn_delete.place(x=540,y=500,width=110,height=40)
       self.btn_clear=Button(self.root,text="Clear",font=("times new roman",15,"bold"),fg="white",bg="#B00857",cursor="hand2",command=self. clear)
       self.btn_clear.place(x=660,y=500,width=110,height=40)  
       
       
       #==================================
        #===========================
        #==========================Seacch paneln========== 
       self.var_search=StringVar() 
       lbl_search_class=Label(self.root,text="Classes",font=("times new roman",20,"bold"),bg="white").place(x=970,y=150)  
       txt_search_class=Entry(self.root,textvariable=self.var_search,font=("times new roman",18),bg="lightyellow").place(x=1200,y=150,width=180) 
       btn_search=Button(self.root,text="Search",font=("timesself.newself.roman",15,"bold"),fg="white",bg="#2196f3",cursor="hand2",command=self.search_data).place(x=1400,y=150,width=110,height=28)
       
       
        #==================================
        #===========================
        #=========================content========= 
        
       self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
       self.C_Frame.place(x=970,y=250,width=550,height=340)
       
       
       scroll_x=Scrollbar(self.C_Frame,orient=HORIZONTAL)
       
       scroll_y=Scrollbar(self.C_Frame,orient=VERTICAL)
       
       self.ClassTable=ttk.Treeview(self.C_Frame,columns=("no.","class","fees","description"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       
       scroll_x.pack(side=BOTTOM,fill=X)
       scroll_y.pack(side=RIGHT,fill=Y)
       scroll_x.config(command= self.ClassTable.xview)
       scroll_y.config(command= self.ClassTable.yview)
       
       self.ClassTable.heading("no.",text="No.")
       self.ClassTable.heading("class",text="Class")
       self.ClassTable.heading("fees",text="Fees")
       self.ClassTable.heading("description",text="Description")
       
       
       self.ClassTable["show"]="headings"
       
       
       self.ClassTable.column("no.",width=130)
       self.ClassTable.column("class",width=130)
       self.ClassTable.column("fees",width=130)
       self.ClassTable.column("description",width=130)
       
       self.ClassTable.pack(fill=BOTH,expand=1)
       self.ClassTable.bind("<ButtonRelease-1>",self.get_cursor)
       self.fetch_data()
#===
# =======================================================================================
#=============================================   

    def back_window(self):     
           self.root.destroy()
           import dashboard 

    def add(self):
        if self.var_class.get()=="":
                messagebox.showerror("Error","class name should be required")
        else: 
            try:  
                conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
                my_cursur=conn.cursor()
                sql="select * from class_pro where class=%s"                  #==========when email & pass invalid=============
                value=(self.var_class.get(),)
                my_cursur.execute(sql,value)
                row=my_cursur.fetchone()
                #print(row)
                if row!=None:
                    messagebox.showerror("Error","Class already exists")
                else:
                    my_cursur.execute("insert into class_pro (class,fees,description) values(%s,%s,%s)",
                                                                                           (self.var_class.get(),
                                                                                            self.var_fees.get(),
                                                                                            self.txt_description.get("1.0",END)
                                                                                                                               ))
                    conn.commit()
                    self.fetch_data()
                    self.clear()
                    conn.close()
                    messagebox.showinfo("Success","Record Has Been Inserted")
            except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)}") 
                
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
        my_cursur=conn.cursor()
        my_cursur.execute("select * from class_pro")
        rows=my_cursur.fetchall()
        if len(rows)!=0:
            self.ClassTable.delete(*self.ClassTable.get_children())
            for row in rows:
                self.ClassTable.insert('',END,values=row)
            conn.commit()
        conn.close()   
        
        
    def get_cursor(self,ev):
        self.txt_class.config(state='readonly')
        cursor_row=self.ClassTable.focus()
        content=self.ClassTable.item(cursor_row)
        row=content['values']
        
        self.var_class.set(row[1]),
        self.var_fees.set(row[2]),
        
        self.txt_description.delete("1.0",END)
        self.txt_description.insert(END,row[3])    
        
        
    def update_data(self):
            try:
                if self.var_class.get()=="":
                     messagebox.showerror("Error","Class name should be required")
                else:     
                    conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
                    my_cursur=conn.cursor()
                    sql="select * from class_pro where class=%s"                  #==========when email & pass invalid=============
                    value=(self.var_class.get(),)
                    my_cursur.execute(sql,value)
                    row=my_cursur.fetchone()
                    #print(row)
                    if row==None:
                         messagebox.showerror("Error","Select Class from list")
                    else:
                        my_cursur.execute("update class_pro set fees=%s,description=%s where class=%s",
                                                                                    (self.var_fees.get(),
                                                                                     self.txt_description.get("1.0",END),
                                                                                     self.var_class.get(),
                                                                                     ))
                        conn.commit()
                        self.fetch_data()
                        self.clear()
                        conn.close()   
                        messagebox.showinfo("Success","Record Update Successfully")    
            except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)}")   
                
                
    def clear(self): 
        self.var_class.set(""),
        self.var_fees.set(""),
        self.var_search.set(""),
        self.txt_description.delete("1.0",END)  
        self.txt_class.config(state=NORMAL)    
        
        
    def delete_data(self):
        try:
                if self.var_class.get()=="":
                     messagebox.showerror("Error","Class name should be required")
                else:     
                    conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
                    my_cursur=conn.cursor()
                    sql="select * from class_pro where class=%s"                  #==========when email & pass invalid=============
                    value=(self.var_class.get(),)
                    my_cursur.execute(sql,value)
                    row=my_cursur.fetchone()
                    #print(row)
                    if row==None:
                         messagebox.showerror("Error","Select Class from list")
                    else:
                        conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
                        my_cursur=conn.cursor()
                        sql="delete from class_pro where class=%s"                  #==========when email & pass invalid=============
                        value=(self.var_class.get(),)
                        my_cursur.execute(sql,value)
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Delete","Record Has Been Deleted")
                        self.fetch_data()
                        self.clear()                  
        except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)}") 
                
                
    def search_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
        my_cursur=conn.cursor()
        my_cursur.execute("select * from class_pro where class "+" LIKE '%"+str(self.var_search.get())+"%'")
        rows=my_cursur.fetchall()
        if len(rows)!=0:
           self.ClassTable.delete(*self.ClassTable.get_children())
           for row in rows:
                self.ClassTable.insert('',END,values=row)
                conn.commit()
                conn.close()               
root=Tk()
ob=cc(root)
root.mainloop()