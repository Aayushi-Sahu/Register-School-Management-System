from tkinter import*
from tkinter import ttk,messagebox
import os
import mysql.connector                #================databse connectivity mysql============


#============define a clas==================
class Login_Window:
    def __init__(self,root):                   #======constructor=
        self.root=root
        self.root.title("LOGIN")
        self.root.geometry("1350x700+0+0")
        
        #=======Background color=========
        left_lbl=Label(self.root,bg="#08A3D2").place(x=0,y=0,relheight=1,width=900)
        
        right_lbl=Label(self.root,bg="#031F3C").place(x=900,y=0,relwidth=1,relheight=1)
        
       
        
        #========login frame=======
        login_frame1=Frame(self.root,bg="white")
        login_frame1.place(x=500,y=150,width=900,height=500)
        
        title=Label(login_frame1,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)
        
        
        #=======entry======
        email=Label(login_frame1,text="EMAIL ADDRESS",font=("times new roman",18,"bold"),bg="white",fg="grey").place(x=250,y=150)
        self.txt_email=Entry(login_frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_email.place(x=250,y=180,width=350,height=35)
        
        
        password=Label(login_frame1,text="PASSWORD",font=("times new roman",18,"bold"),bg="white",fg="grey").place(x=250,y=250)
        self.txt_password=Entry(login_frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_password.place(x=250,y=280,width=350,height=35)
        
        
        
        #======= resitration Button==========
        btn_reg=Button(login_frame1,text="Register New Account?",command=self.register_window,font=("times new roman",14),bg="white",fg="#B00857",bd=0,cursor="hand2").place(x=250,y=330)
        
        #======= forget Button==========
        btn_forget=Button(login_frame1,text="Forget Password",command=self.forget_password_window,font=("times new roman",14),bg="white",fg="Red",bd=0,cursor="hand2").place(x=450,y=330)
        
        #=======login Button==========
        btn_login=Button(login_frame1,text="Login",command=self.login,font=("times new roman",20,"bold"),fg="white",bg="#B00857",cursor="hand2").place(x=250,y=390,width=180,height=40) 
        
        
    def reset(self):
        self.cmb_question.current(0)
        self.txt_new_password.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)
        
    def forget_paas(self):
        if self.cmb_question.get()=="" or self.txt_answer.get()=="" or self.txt_new_password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
                my_cursur=conn.cursor()
                sql="select * from student where email=%s and question=%s and answer=%s"                  #==========when email & pass invalid=============
                value=(self.txt_email.get(),self.cmb_question.get(),self.txt_answer.get(),)
                my_cursur.execute(sql,value)
                row=my_cursur.fetchone()
                #print(row)
                if row==None:
                    messagebox.showerror("Error","Please Select Correct Security question/ Enter Answer password",parent=self.root2)
                else:
                    sql="update student set password=%s where email=%s"                  #==========when email & pass invalid=============
                    value=(self.txt_new_password.get(),self.txt_email.get(),)
                    my_cursur.execute(sql,value)
                    row2=my_cursur.fetchone()
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Your password has been reset,Please login with new password",parent=self.root2)
                    
                    self.reset()
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)}",parent=self.root)       
                
              
    #==========forget password function===============  
    #=======called the funtion on forget button========  
    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset your password",parent=self.root)
        else: 
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
                my_cursur=conn.cursor()
                sql="select * from student where email=%s"                  #==========when email & pass invalid=============
                value=(self.txt_email.get(),)
                my_cursur.execute(sql,value)
                row=my_cursur.fetchone()
                #print(row)
                if row==None:
                    messagebox.showerror("Error","Please enter the valid email address to reset your password",parent=self.root)
                else:
                    conn.close() 
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+495+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()
        
        
                    #=========give the title, designn, twext, place=======================
                    t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)
        
                    #======forget password entry field================
                    question=Label(self.root2,text="SECURITY QUESTION",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=100)
        
        
                    self.cmb_question=ttk.Combobox(self.root2,font=("times new roman",15),state='readonly',justify=CENTER)
                    self.cmb_question['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
                    self.cmb_question.place(x=50,y=130,width=250)
                    self.cmb_question.current(0)
        
        
        
                    answer=Label(self.root2,text="ANSWER",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=180)
                    self.txt_answer=Entry(self.root2,font=("times new roman",18),bg="lightgrey")
                    self.txt_answer.place(x=50,y=210,width=250)
        
        
                    new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=260)
                    self.txt_new_password=Entry(self.root2,font=("times new roman",18),bg="lightgrey")
                    self.txt_new_password.place(x=50,y=290,width=250)
        
                    #=============reset button===================
                    btn_change_password=Button(self.root2,text="Reset Password",font=("times new roman",15,"bold"),command=self.forget_paas,fg="white",bg="green",cursor="hand2").place(x=90,y=340)
    
                     
                     
                    
            except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)}",parent=self.root)     
           
    
           
        
            
        
        
           
    
    
        
    #============function for click to button then go to register page==   
    #============the function called on register button==================
    def register_window(self):  
        self.root.destroy()
        import register             # use python file name not class name
                      
    #================define a function to get the detail use database & validation============= 
    #==============this function called on login button================================= 
    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","All Field are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") #============database =========
                my_cursur=conn.cursor()
                sql="select * from student where email=%s and password=%s"                  #==========when email & pass invalid=============
                value=(self.txt_email.get(),self.txt_password.get(),)
                my_cursur.execute(sql,value)
                row=my_cursur.fetchone()
                
                if row==None:
                    messagebox.showerror("Error","Invalid Username & Password",parent=self.root) 
                    
                else:
                     
                    messagebox.showinfo("Success",f"Welcome : {self.txt_email.get()}",parent=self.root) 
                    self.root.destroy()
                    import dashboard
                       
                       
        
                    
                    #=============close the database
                    conn.close()
        
                    
       
       
        
        
                    #=========give the title, designn, twext, place=======================
            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)   
   
    
        
root=Tk()
obj=Login_Window(root)
root.mainloop()            