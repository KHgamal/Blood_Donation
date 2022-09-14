import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from PIL import ImageTk, Image  
from tkcalendar import Calendar, DateEntry 
import sqlite3
 
#_____________________________________submitRequest_page_______________________
 #database
def cont_req(d,ph,nm,mc,bu,rea):    

        db.execute("CREATE TABLE IF NOT EXISTS patient(name CHAR(30) NOT NULL,medicalcen CHAR(30) PRIMARY KEY NOT NULL,requestdate timestamp NOT NULL, phone CHAR(15) NOT NULL,bloodtype CHAR(15) NOT NULL,reasons CHAR(30) NOT NULL)")
        db.execute("INSERT INTO patient(name, medicalcen, requestdate,phone,bloodtype,reasons) VALUES(?, ?, ?,?,?,?)", 
                       [ nm.get(), mc.get(), d.get_date(),ph.get(),bu.get(),rea.get()])
        db.commit()
        nm.delete(0,"end")
        mc.delete(0,"end")
        d.delete(0,"end")
        ph.delete(0,"end")
        bu.set("choose Blood Type")
        rea.delete(0,"end")
 #UI     
def submit_request():
    global request
    request=tk.Tk()
    request.geometry("300x600")
    request.resizable(False, False)
    request.config(bg="white")
    
    header=tk.LabelFrame()
    topFrame=tk.Frame(request, bg="red3")
    topFrame.pack(side="top",fill=tk.X)
    homelabel=tk.Label(topFrame,text="Submit Request",font="Bahnschrift 15",bg="red3" ,fg="white",height=1,padx=20)
    homelabel.pack(side="bottom")

#name
    tk.Label(request,text="Patient Name", font=("Comic Sans",14),
             bg="white").place(x=15, y=70)

    name=tk.Entry(request,width=40,bg="#f5f5f5",bd=1)
    name.place(x=15,y=100)

    name.bind("<Return>",lambda temp1:phone.focus())
    
#phone
    tk.Label(request,text="Contact Number", font=("Comic Sans",14),
             bg="white").place(x=15, y=130)
    phone=tk.Entry(request,width=40,bg="#f5f5f5",bd=1)
    phone.place(x=15,y=160)
    phone.bind("<Return>",lambda temp2:optionmenu_widget.focus())
    
#Blood_unit
    tk.Label(request,text="Blood Type :",font=("Comic Sans",14),
                  bg="white").place(x=15, y=190)
    control_variable = tk.StringVar(request)
    control_variable.set("Blood Type")
    OPTION_TUPLE = ("AB+", "AB-", "O+","O-","A+","A-","B+","B-") 
    optionmenu_widget = tk.OptionMenu(request,control_variable, *OPTION_TUPLE)
    optionmenu_widget.place(x=170,y=195)
    optionmenu_widget.bind("<Return>",lambda temp3:medicalcen.focus())
    
#Medical_Center
    tk.Label(request,text="Medical Center", font=("Comic Sans",14),
             bg="white").place(x=15, y=230)
    medicalcen=tk.Entry(request,width=40,bg="#f5f5f5",bd=1)
    medicalcen.place(x=15,y=260)
    medicalcen.bind("<Return>",lambda temp4:requestd.focus())

#Requested_Date
    tk.Label(request,text="Request Date", font=("Comic Sans",14)
             ,bg="white").place(x=10, y=280)
    
    requestd=DateEntry(request, width=16, background="red3",foreground="white",bd=2)
    #requestd=tk.Entry(request,width=40,bg="#f5f5f5",bd=1)
    requestd.place(x=15,y=310)
    requestd.bind("<Return>",lambda temp5:reasons.focus())

#Reasons
    tk.Label(request,text="reasons",font=("Comic Sans",14),
             bg="white").place(x=10, y=330)
    reasons=tk.Entry(request,width=32,bg="#f5f5f5",bd=1)
    reasons.place(x=15,y=360,height=50)
    
    
    reasons.bind("<Return>",lambda temp6:reasons.cont_req
     (d=requestd,ph=phone,nm=name,mc=medicalcen,rea=reasons,bu=control_variable))


    req_cont=tk.Button(request,text="Submit",padx=8, pady=4, bd=8,fg="white", bg="red3",width=5,
                        height=1,font=("Comic Sans",10,"bold"),command=lambda :cont_req
                        (d=requestd,ph=phone,nm=name,mc=medicalcen,rea=reasons,bu=control_variable))
    req_cont.place(x=200, y=450)
    
    Button(text="Back",padx=8, pady=4, bd=8,font=("Arial",10,"bold"),bg="red3",fg="white",height=1,
           width=5,command=lambda:next_back(request, Receiver)).place(x=200, y=505)
    
#______________________________________donorList_page__________________________
def dList():
   global donor 
   global SEARCH
   global tree
   donor=tk.Tk()
   donor.geometry("300x500")
   donor.config(bg="white")
   donor.resizable(False,False) 
   
   #header=tk.LabelFrame()
   topFrame2=tk.Frame(donor, bg="red3")
   topFrame2.pack(side="top",fill=tk.X)
   homelabel2=tk.Label(topFrame2,text="Donors list",font="Bahnschrift 15" ,bg="red3",
                      fg="white",height=2,padx=20)
   homelabel2.pack(side="bottom")
   
   # search
   LeftViewForm = Frame(donor,bg="white")
   LeftViewForm.pack(side=TOP, fill=X)
   
   # blood unit
   SEARCH = StringVar()   
   SEARCH.set("Blood unit")
   OPTION_TUPLE1 = ("AB+", "AB-", "O+","O-","A+","A-","B+","B-") 
   # ديه اللى هيتعمل ليها get فى دالة ال search   
   optionmenu_widget1= tk.OptionMenu(LeftViewForm,SEARCH,*OPTION_TUPLE1,command=SearchRecord) 
   optionmenu_widget1.pack(side=RIGHT, padx=20,pady=10)
   #optionmenu_widget1.place(x=5,y=65,width=200,height=35)
   
   # view all button
   btn_search = Button(LeftViewForm, text="View All", command=DisplayData)
   btn_search.pack(side=RIGHT, padx=10, pady=10)
   
   Button(text="Back",padx=8, pady=4, bd=8,font=("Arial",10,"bold"),bg="red3",fg="white",height=1,
             width=4,command=lambda:next_back(donor,Receiver)).place(x=5,y=57)
# table  
   MidViewForm = Frame(donor, width=300)
   MidViewForm.pack(side=BOTTOM)
   
   # 1 setting scrollbar
   scrollbarx = Scrollbar(donor, orient=HORIZONTAL)
   scrollbary = Scrollbar(donor, orient=VERTICAL)

   # 3 tree
   tree = ttk.Treeview(donor,columns=("Name", "phone", "Blood Unit","address"),selectmode="extended", 
            yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set,height=100,)
   
   # 4 style of tree
   s = ttk.Style()
   s.theme_use('clam')
   # Configure the style of Heading in Treeview widget
   s.configure('Treeview.Heading', foreground="white",background="red3")
   
   # scroll bar
   scrollbary.config(command=tree.yview)
   scrollbary.pack(side=RIGHT, fill=Y)
   scrollbarx.config(command=tree.xview)
   scrollbarx.pack(side=BOTTOM, fill=X)
   
   # 2 setting headings for the columns
   tree.heading('Name', text="Name", anchor=W)
   tree.heading('phone', text="phone", anchor=W)
   # tree.heading('Contact', text="Contact", anchor=W)
   tree.heading('Blood Unit', text="Blood Unit", anchor=W)
   tree.heading('address', text="address", anchor=W)
   
   # 5 setting width of the columns
   tree.column('#0', stretch=NO, minwidth=0, width=0)
   tree.column('#1', stretch=NO, minwidth=0, width=70)
   tree.column('#2', stretch=NO, minwidth=0, width=70)
   tree.column('#3', stretch=NO, minwidth=0, width=70)
   
   tree.pack()
   DisplayData()

#function to search data
def SearchRecord():
        #clearing current display data
        tree.delete(*tree.get_children())
        #select query with where clause
        cursor=db.execute("SELECT name, phone, bloodtype, address FROM donor WHERE name LIKE ?",
                          ('%' + str(optionmenu_widget1.get()) + '%',))
        #fetch all matching records
        fetch = cursor.fetchall()
        #loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
       # conn.close()
       
#defining function to access data from SQLite database
def DisplayData():
    #clear current data
    tree.delete(*tree.get_children())
    #select query
    cursor=db.execute("SELECT name, phone, bloodtype, address FROM donor")
    #fetch all data from database
    fetch = cursor.fetchall()
    #loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
   # conn.close()   
   
#______________________________________Requests_page___________________________
def Requests():
   global req_uest 
   req_uest=tk.Tk()
   req_uest.geometry("300x500")
   req_uest.config(bg="white")
   req_uest.resizable(False,False) 

   #header=tk.LabelFrame()
   topFrame3=tk.Frame(req_uest, bg="white")
   topFrame3.pack(side="top",fill=tk.X)
   homelabel3=tk.Label(topFrame3,text="Requests",font=("Bahnschrift 15",15,"bold") ,bg="white",
                      fg="red3",height=1,padx=20,pady=20)
   homelabel3.pack(side="left")
   Button(text="Back",padx=8, pady=4, bd=8,font=("Arial",10,"bold"),bg="red3",fg="white",height=1,
             width=5,command=lambda:next_back(req_uest,Second)).place(x=180,y=10)
   
# table  
   MidViewForm = Frame(req_uest, width=300)
   MidViewForm.pack(side=BOTTOM)
   
   # 1 setting scrollbar
   scrollbarx = Scrollbar(req_uest, orient=HORIZONTAL)
   scrollbary = Scrollbar(req_uest, orient=VERTICAL)

   # 3 tree
   tree = ttk.Treeview(req_uest,columns=("Name", "phone", "Blood Unit","request Date","reason"),selectmode="extended", 
            yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set,height=100,)
   
   # 4 style of tree
   s = ttk.Style()
   s.theme_use('clam')
   # Configure the style of Heading in Treeview widget
   s.configure('Treeview.Heading', foreground="white",background="red3")
   
   # scroll bar
   scrollbary.config(command=tree.yview)
   scrollbary.pack(side=RIGHT, fill=Y)
   scrollbarx.config(command=tree.xview)
   scrollbarx.pack(side=BOTTOM, fill=X)
   
   # 2 setting headings for the columns
   tree.heading('Name', text="Name", anchor=W)
   tree.heading('phone', text="phone", anchor=W)
   tree.heading('Blood Unit', text="Blood Unit", anchor=W)
   tree.heading('request Date', text="request Date", anchor=W)
   tree.heading('reason', text="reason", anchor=W)
   
   # 5 setting width of the columns
   tree.column('#0', stretch=NO, minwidth=0, width=0)
   tree.column('#1', stretch=NO, minwidth=0, width=70)
   tree.column('#2', stretch=NO, minwidth=0, width=70)
   tree.column('#3', stretch=NO, minwidth=0, width=70)
   tree.column('#4', stretch=NO, minwidth=0, width=80)
   
   tree.pack()
   cursor=db.execute("SELECT name,phone,bloodtype,requestdate,reasons  FROM patient")
   #fetch all data from database
   fetch = cursor.fetchall()
   #loop for displaying all data in GUI
   for data in fetch:
       tree.insert('', 'end', values=(data))
   cursor.close()
   
#______________________________________Receive_page____________________________
def Receiver():
   global receiver 
   receiver=tk.Tk()
   receiver.geometry("300x500")
   receiver.config(bg="white")
   receiver.resizable(False,False)
   tk.Label(receiver,text="Here is a list of donors :", font=("Comic Sans",15),
            bg="white").place(x=5, y=30) 
   Button(text="Donors list",padx=8, pady=4, bd=8,font=("Arial",10,"bold"),bg="red3",fg="white",height=1,width=7,
          command=lambda:next_back(receiver, dList)).place(x=140,y=80)
   tk.Label(receiver,text="Can't find what you are looking for ?", font=("Comic Sans",12),
           fg="red3", bg="white").place(x=40, y=145) 
   tk.Label(receiver,text="Submit a blood request : ", font=("Comic Sans",15),
            bg="white").place(x=5, y=190) 
 
   Button(text="Request",padx=8, pady=4, bd=8,font=("Arial",10,"bold"),bg="red3",fg="white",height=1,width=7,
          command=lambda:next_back(receiver, submit_request)).place(x=140,y=240)

#signUp Database
def cont_sign(a,b,nm,em,bu,ad):    

        db.execute("CREATE TABLE IF NOT EXISTS donor(name CHAR(30) NOT NULL,email CHAR(30) PRIMARY KEY NOT NULL,password CHAR(15) NOT NULL, phone CHAR(15) NOT NULL,bloodtype CHAR(15) NOT NULL,address CHAR(30) NOT NULL)")
        data = db.execute("SELECT email FROM donor").fetchall()
    
        result = [] 
  
        for t in data: 
            result.append(t[0])
        temp_var=em.get()
    
        fal=None
#email already exists
        if temp_var in result:  
            fal=tk.Label(text="The email id matches previous records",fg="red3", 
                         font=("Comic Sans",12),bg="white")
            #allow another sign up
            em.delete(0,"end")
            a.delete(0,"end")
            b.delete(0,"end")
            bu.set("choose Blood unit")
            ad.delete(0,"end")
            fal.place(x=10, y=430)
        else:
            db.execute("INSERT INTO donor(name, email, password,phone,bloodtype,address) VALUES(?, ?, ?,?,?,?)", 
                       [ nm.get(), em.get(), a.get(),b.get(),bu.get(),ad.get()])
            db.commit()
            nm.delete(0,"end")
            em.delete(0,"end")
            a.delete(0,"end")
            b.delete(0,"end")
            bu.set("choose Blood unit")
            ad.delete(0,"end")
            if fal:
                fal.destroy()
            tk.Label(text="Sign Up Successful", font=("Comic Sans",12),fg="red3",
                     bg="white").place(x=15, y=430)

#______________________________________SignUp_page_____________________________
def sign_up():
    global sign
    sign=tk.Tk()
    sign.geometry("300x600")
    sign.resizable(False, False)
    sign.config(bg="white")

    tk.Label(sign,text="Register",fg="red3", font=("Comic Sans",15,
             "bold"),bg="white").place(x=100, y=20)
#name
    tk.Label(sign,text="Name", font=("Comic Sans",14),
             bg="white").place(x=15, y=70)

    name=tk.Entry(sign,width=40,bg="#f5f5f5",bd=1)
    name.place(x=15,y=100)

    name.bind("<Return>",lambda temp1:email.focus())
    
#email
    tk.Label(sign,text="Email", font=("Comic Sans",14),
             bg="white").place(x=15, y=130)
    email=tk.Entry(sign,width=40,bg="#f5f5f5",bd=1)
    email.place(x=15,y=160)
    email.bind("<Return>",lambda temp2:password.focus())
    
#password
    tk.Label(sign,text="Password", font=("Comic Sans",14),
             bg="white").place(x=15, y=190)
    password=tk.Entry(sign,show="*",width=40,bg="#f5f5f5",bd=1)
    password.place(x=15,y=220)
    password.bind("<Return>",lambda temp3:phone.focus())

#Phone
    tk.Label(sign,text="Phone", font=("Comic Sans",14)
             ,bg="white").place(x=15, y=250)

    phone=tk.Entry(sign,width=40,bg="#f5f5f5",bd=1)
    phone.place(x=15,y=280)
    phone.bind("<Return>",lambda temp4:optionmenu_widget.focus())

#Blood_unit
    tk.Label(sign,text="Blood Type :",font=("Comic Sans",14),
              bg="white").place(x=10, y=300)
    control_variable = tk.StringVar(sign)
    control_variable.set("Blood unit")
    OPTION_TUPLE = ("AB+", "AB-", "O+","O-","A+","A-","B+","B-") 
    optionmenu_widget = tk.OptionMenu(sign,control_variable, *OPTION_TUPLE)
    optionmenu_widget.place(x=170,y=305)
    optionmenu_widget.bind("<Return>",lambda temp5:address.focus())

#Address
    tk.Label(sign,text="Address",font=("Comic Sans",14),
             bg="white").place(x=10, y=330)
    address=tk.Entry(sign,width=32,bg="#f5f5f5",bd=1)
    address.place(x=15,y=360,height=50) 
    address.bind("<Return>",lambda temp6:address.cont_sign
     (a=password,b=phone,nm=name,em=email,ad=address,bu=control_variable))


    sign_cont=tk.Button(sign,text="Sign Up",padx=8, pady=4, bd=8,fg="white", bg="red3",width=5,
                        height=1,font=("Comic Sans",10,"bold"),command=lambda :cont_sign
                        (a=password,b=phone,nm=name,em=email,ad=address,bu=control_variable))
    sign_cont.place(x=200, y=460)
    
    Button(text="Back",padx=8, pady=4, bd=8,font=("Arial",10,"bold"),bg="red3",fg="white",height=1,
           width=5,command=lambda:next_back(sign, log_in)).place(x=200, y=515)
    tk.mainloop()

#log in Database
def func(var1,var2):
    data = db.execute("SELECT email FROM donor").fetchall()
        
    res=[]

    for t in data: 
        res.append(t[0])
    temp_var1=var1.get()
    
    
#if email is correct
    if temp_var1 in res:
        #inval1.delete(0,"end")
        info = db.execute(f"SELECT password FROM donor WHERE email='{temp_var1}'").fetchall()
 #if pass is correct
        if var2.get()==info[0][0]:
            val=tk.Label(text="You have been successfully logged in", font=("Arial", 12), bg="white",
                         fg="red3").place(x=0,y=235)
         
            tk.mainloop()
 #if pass is not correct
        else:
            inval=tk.Label(text="Plase enter valid password", bg="white", fg="red3").place(x=110,y=160)
          
#if email is  not correct
    else:
        inval1=tk.Label(text="Plase enter valid email", bg="white", fg="red3").place(x=80,y=80)
    
#______________________________________login_page______________________________
def log_in():
    global anyo
    anyo=tk.Tk()
    anyo.geometry("300x500")
    anyo.resizable(False,False)
    anyo.title("Login Page")
    anyo.config(bg="white")
    #tk.Label(bg="old lace").pack()
    login=tk.Label(anyo, text="Login Page", font=("Comic Sans",24,"bold"), bg="white"
                   ,fg="red3")
    login.place(x=60,y=20)

#user name 
    uname=tk.Label(anyo, text="Email", font=("Comic Sans",16), bg="white").place(x=0,y=80)
    utxt=tk.Entry(bg='gray95',width=45)
    utxt.place(x=10,y=120,height=30)
    utxt.bind("<Return>",lambda temp5:passw.focus())

#password
    passw=tk.Label(anyo, text="Password", font=("Comic Sans",16), bg="white"
                   ).place(x=0,y=160)
  
    ptxt=tk.Entry(bg='gray95',show="*")
    ptxt.place(x=10,y=200,width=275,height=30)
    ptxt.bind("<Return>",lambda temp6:func(utxt,ptxt))

    logbut=tk.Button(anyo, text="Login", font=("Comic Sans",10,"bold"), bg="red3", fg="white",padx=8,
                     pady=4, bd=8, height=1,width=5,command=lambda:func(var1=utxt,var2=ptxt))
    logbut.place(x=10,y=255)
    Label(text="Don't have an account ? ",font=("Comic Sans",12,"bold"), bg="white").place(x=0,y=330)
    Button(anyo, text="Sign up", font=("Comic Sans",10,"bold"), bg="red3", fg="white",padx=8, pady=4,
           bd=8, height=1,width=5,command=lambda:next_back(anyo,sign_up)).place(x=200,y=320)
    
    tk.Label(anyo,text="Go back to Previous page :", font=("Comic Sans",11,"bold"), fg="black",
              bg="white").place(x=0, y=390)
    Button(text="Back",padx=8, pady=4, bd=8,font=("Arial",10,"bold"),bg="red3",fg="white",height=1,
           width=5,command=lambda:next_back(anyo,Second)).place(x=200,y=380)

#______________________________________Donor_page______________________________
def Second():  
  global second
  second=tk.Tk()
  second.geometry("300x500")

  second.resizable(False, False)
  second.title("Donor Page")
  second.config(bg="white")
  
  tk.Label(second,text="Blood is life-giving", font=("Comic Sans",20,"bold"), fg="red3",
           bg="white").place(x=0, y=20) 
  tk.Label(second,text=" Our thanks go out to you for making ", font=("Comic Sans",12,"bold"), fg="black",
           bg="white").place(x=0, y=70)
  tk.Label(second,text=" this choice and for taking the time to", font=("Comic Sans",12,"bold"), fg="black",
           bg="white").place(x=0, y=100)
  tk.Label(second,text=" make a blood donation.", font=("Comic Sans",12,"bold"), fg="black",
           bg="white").place(x=0, y=130)
  tk.Label(second,text=" We deeply thank you.", font=("Comic Sans",15,"bold"), fg="black",
           bg="white").place(x=0, y=160)
  
  tk.Label(second,text="keep in touch with us :", font=("Comic Sans",11,"bold"), fg="black",
           bg="white").place(x=70, y=220)
  Button(text="Register",padx=8, pady=4, bd=8,font=("Arial",10,"bold"),bg="red3",fg="white",height=1,width=10,
         command=lambda:next_back(second, log_in)).place(x=95,y=250) 
  
  tk.Label(second,text="Take a look at requests :", font=("Comic Sans",11,"bold"), fg="black",
           bg="white").place(x=60, y=310)
  Button(text="Requests",padx=8, pady=4, bd=8,font=("Arial",10,"bold"),bg="red3",fg="white",height=1,width=10,
         command=lambda:next_back(second, Requests)).place(x=95,y=340) 
  
#_________________next/back_____________
def next_back(recent,fun):
    recent.destroy()
    fun()

#______________________________________first_page______________________________
win=Tk()
db=sqlite3.connect("data.db")

#windows propreties
win.title("Blood donation")
win.config(bg="white")
win.geometry("300x500")
win.resizable(False,False)

#image 
img= (Image.open("D:/8.blood app/python/images/blood.jpg"))
resized_image= img.resize((300,250), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
label=Label(image=new_image)
label.pack()

#Donor_button
mg= (Image.open("D:/8.blood app/python/buttons/Button_7.jpg"))
rmg= mg.resize((150,70))
Donorimage = ImageTk.PhotoImage(rmg)
roundedbutton = Button(image=Donorimage,border=0,command=lambda:next_back(win, Second)) 
roundedbutton.place(relx=0.25,rely=0.6)

#Receiver_button
mg2= (Image.open("D:/8.blood app/python/buttons/Button_6.jpg"))
rmg2= mg2.resize((150,70))
Receiverimage = ImageTk.PhotoImage(rmg2)
roundedbutton2 = Button(image=Receiverimage,border=0,command=lambda:next_back(win,Receiver)) 
roundedbutton2.place(relx=0.25,rely=0.75)
                
tk.mainloop()
