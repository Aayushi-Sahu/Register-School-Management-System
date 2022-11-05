from tkinter import*
from tkinter import ttk,messagebox
import mysql.connector    #=========database connectivity mysql==============


#============define a class============
class Register:             
    def __init__(self,root):            #=========constructor==========root is a variable
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        
        #=====================background colour daek blue & blue===================
        left_lbl=Label(self.root,bg="#08A3D2").place(x=0,y=0,relheight=1,width=900)
        
        right_lbl=Label(self.root,bg="#031F3C").place(x=900,y=0,relwidth=1,relheight=1)
       
        # =====Registration Frame============
        frame1=Frame(self.root,bg="white")
        frame1.place(x=500,y=150,width=900,height=550)    #========define frame lenght============
        
        
        #========give the title text designn place==================
        title=Label(frame1,text="REGISTER HERE",font=("times new roman",25,"bold"),bg="white",fg="green").place(x=50,y=30)
        
        
        #==========ROW1 (first name & last name )=========
        f_name=Label(frame1,text="FIRST NAME",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",18),bg="lightgrey")
        self.txt_fname.place(x=50,y=130,width=250)
        
        l_name=Label(frame1,text="LAST NAME",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",18),bg="lightgrey")
        self.txt_lname.place(x=370,y=130,width=250)
        
        
        #==========ROW2 (contact & email)==========
        contact=Label(frame1,text="CONTACT NO.",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",18),bg="lightgrey")
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame1,text="EMAIL",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",18),bg="lightgrey")
        self.txt_email.place(x=370,y=200,width=250)
        
        
        #==========ROW3 (question & answer)==========
        question=Label(frame1,text="SECURITY QUESTION",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=240)
        
                 
        self.cmb_question=ttk.Combobox(frame1,font=("times new roman",15),state='readonly',justify=CENTER)      #============use combobox==========
        self.cmb_question['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_question.place(x=50,y=270,width=250)
        self.cmb_question.current(0)
        
        
        
        answer=Label(frame1,text="ANSWER",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",18),bg="lightgrey")
        self.txt_answer.place(x=370,y=270,width=250)
        
        #==========ROW4 (gender & address)==========
        gender=Label(frame1,text="GENDER",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=310)
        
        
        self.cmb_gen=ttk.Combobox(frame1,font=("times new roman",15),state='readonly',justify=CENTER)      #============use combobox==========
        self.cmb_gen['values']=("Select","Male","Female","Other")
        self.cmb_gen.place(x=50,y=340,width=250)
        self.cmb_gen.current(0)
        
        
        
        address=Label(frame1,text="ADDRESS",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=310)
        self.txt_address=Entry(frame1,font=("times new roman",18),bg="lightgrey")
        self.txt_address.place(x=370,y=340,width=250)
        
        
         #==========ROW 5 (password & confirm password)==========
        password=Label(frame1,text="PASSWORD",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=380)
        self.txt_password=Entry(frame1,font=("times new roman",18),bg="lightgrey")
        self.txt_password.place(x=50,y=410,width=250)
    
        
        cpassword=Label(frame1,text="CONFIRM PASSWORD",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=380)
        self.txt_cpassword=Entry(frame1,font=("times new roman",18),bg="lightgrey")
        self.txt_cpassword.place(x=370,y=410,width=250)
        
        
        #=====button (Terms)===================
        self.var_chk=IntVar()     #=========a vaiable for checkbutton
        chk=Checkbutton(frame1,text="I Agree Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=440)
        
        #=======register button===========
        btn_register=Button(frame1,text="REGISTER NOW",bg="green",fg="white",cursor="hand2",font=("times new roman",15,"bold"),command=self.register_data).place(x=50,y=480)
        
        #===========login button===========
        btn_login=Button(frame1,text="SIGN IN",command=self.login_window,fg="white",bg="#B00857",cursor="hand2",font=("times new roman",14)).place(x=600,y=30)
    
    
    
    
    #=======define a function when we click login button go to login page=========  
    #==========this function called on login button=========================== 
    def login_window(self):  
        self.root.destroy()             #this for import the python file
        import login                    #use python file anme not class
    
    
        
     #============define a function when we fill the all entry in the register form then it will clear===========       
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_address.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.cmb_question.current(0)
        self.cmb_gen.current(0)
       
            
    #===============define a function to get the detail use database & validation============= 
    #==============this function called on regiter button=================================   
    def register_data(self):   
        if self.txt_fname.get()==""or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_question.get()=="Select" or self.txt_answer.get()=="" or self.cmb_gen.get()=="Select" or self.txt_address.get()=="" or self.txt_password.get()==" " or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)  
        elif   self.txt_password.get()!= self.txt_cpassword.get():
            messagebox.showerror("Error","Password & Confirm Password Should Be Same",parent=self.root)  
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree Our Terms & Conditions",parent=self.root)     
        else:
            try:                        # database connectivity=======================
                conn=mysql.connector.connect(host="localhost",user="root",password="aayushi@1234",database="adb") 
                my_cursur=conn.cursor()
                
                sql="select * from student where email=%s"       #======= when email is alredy existd=================
                value=(self.txt_email.get(),)
                my_cursur.execute(sql,value)
                row=my_cursur.fetchone()
                #print(row)
                if row!=None:
                     messagebox.showerror("Error","User Already Exits,Please try with another email",parent=self.root) 
                else:   
                    my_cursur.execute("insert into student (f_name,l_name,contact,email,question,answer,gender,address,password) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (self.txt_fname.get(),
                                   self.txt_lname.get(),
                                   self.txt_contact.get(),
                                   self.txt_email.get(),
                                   self.cmb_question.get(),
                                   self.txt_answer.get(),
                                   self.cmb_gen.get(),
                                   self.txt_address.get(),
                                   self.txt_password.get()
                                ))            #=======user entry=========
                    conn.commit()
                    conn.close()              #close the database
                    messagebox.showinfo("Success","Register Successfull",parent=self.root) 
                    self.clear() 
                    self.login_window()    # call the function (clear the entry)====================
                
                
            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)      #============it will show error =============
             
root=Tk()
obj=Register(root)   # =========creating a object================
root.mainloop()    