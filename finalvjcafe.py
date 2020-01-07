from tkinter import *
from tkinter import messagebox as ms
from tkinter import ttk
from PIL import Image, ImageTk
import random
import time
import datetime
import sqlite3
from email.message import EmailMessage
import smtplib

with sqlite3.connect('database.db') as db:
    c = db.cursor()
try:
    c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEX  NOT NULL,email TEX NOT NULL);')
except:
    pass
db.commit()
db.close()


class main:
    def __init__(self, master):

        self.master = master

        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        # self.n_reg=StringVar()
        self.n_email = StringVar()
        self.n_email = StringVar()
        # ======All images===========

        self.bg_icon = Image.open("image2.png")
        self.bg_icon = self.bg_icon.resize((2000, 1000))
        self.bg_icon = ImageTk.PhotoImage(self.bg_icon)

        self.logo_icon = Image.open("user.png")
        self.logo_icon = self.logo_icon.resize((450, 250))
        self.logo_icon = ImageTk.PhotoImage(self.logo_icon)
        self.user_icon = Image.open("username.jpg")
        self.user_icon = self.user_icon.resize((100, 50))
        self.user_icon = ImageTk.PhotoImage(self.user_icon)
        self.pass_icon = Image.open("passicon.png")
        self.pass_icon = self.pass_icon.resize((100, 50))
        self.pass_icon = ImageTk.PhotoImage(self.pass_icon)
        self.widgets()

    def login(self):

        with sqlite3.connect('database.db') as db:
            c = db.cursor()

        # Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()

        if result:
            global username1, password1
            username1 = self.username.get()
            password1 = self.password.get()
            # print(str(username1), str(password1) )
            self.SaleWindow = Toplevel(self.master)
            self.app = Billing(self.SaleWindow)
        else:
            ms.showerror('Oops!', 'Username Not Found.')

    def cr(self):
        self.Create = Toplevel(self.master)
        self.app = Createuser(self.Create)


    def widgets(self):
        bg_lbl = Label(self.master,image=self.bg_icon).pack()
        self.head=Label(self.master, text="WELCOME TO VJ CAFE", font=("times new roman", 40, "bold"), fg="red", bd=10,
                          relief=FLAT)
        self.head.place(x=0, y=0, relwidth=1)

        self.logf = Frame(self.master, bg="white")
        self.logf.place(x=500, y=200)

        # PhotoImage(self.logf,file = 'lpu_logo.png')

        logolbl = Label(self.logf, image=self.logo_icon, bd=0).grid(row=0, columnspan=2, pady=20)

        lbluser = Label(self.logf, text="Username", image=self.user_icon, compound=LEFT,
                        font=("times new roman", 20, "bold"), bg="white").grid(row=1, column=0, padx=20, pady=10)
        txtuser = Entry(self.logf, bd="5", textvariable=self.username, relief=GROOVE, font=(" ", 15))
        txtuser.grid(row=1, column=1, padx=20)

        lblpass = Label(self.logf, text="Password", image=self.pass_icon, compound=LEFT,
                        font=("times new roman", 20, "bold"), bg="white").grid(row=2, column=0, padx=20, pady=10)
        txtpass = Entry(self.logf, bd="5",show="*", textvariable=self.password, relief=GROOVE, font=(" ", 15)).grid(row=2,
                                                                                                           column=1,
                                                                                                           padx=20)
        btn_log = Button(self.logf, text="LOGIN", width=15, font=("times new roman", 14, "bold"), bg="blue",
                         fg="white", activebackground="red", command=self.login).grid(row=3, column=0)
        btn_create = Button(self.logf, text="NEW USER", width=15, font=("times new roman", 14, "bold"), bg="blue",
                            fg="white", activebackground="red", command=self.cr).grid(row=3, column=1)




class Createuser:
    def __init__(self,master):
        self.master = master
        self.master.title("LOGIN SCREEN")
        self.master.geometry("1600x800+0+0")
        self.n_username = StringVar()
        self.n_password = StringVar()
        # self.n_reg=StringVar()
        self.n_email = StringVar()
        self.n_email = StringVar()
        self.n_otp=StringVar()
        self.otp1=StringVar()
        self.bg1_icon = Image.open("blue.png")
        self.bg1_icon = self.bg1_icon.resize((2000, 1000))
        self.bg1_icon = ImageTk.PhotoImage(self.bg1_icon)
        self.widgets()
    def otp(self):

        self.otp1=random.randint(10000,20000)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Next, log in to the server
        server.login("dishacheck123@gmail.com", "2rasika4")

        msg = EmailMessage()
        msg['from'] = 'VJCAFE'
        msg['subject'] = "HERE'S YOUR OTP"

        #msg.set_content(otp)
        server.sendmail("dishacheck123@gmail.com", self.n_email.get(), msg.as_string()+str(self.otp1))


    def widgets(self):
        #self.crf = Frame(self.master, padx=10, pady=10)
        #self.crf.place(x=500, y=200)
        bg_lbl = Label(self.master, image=self.bg1_icon).pack()
        self.head = Label(self.master, text="CREATE YOUR ACCOUNT", font=("times new roman", 40, "bold"), fg="red", bd=10,
                          relief=FLAT)
        self.head.place(x=0, y=0, relwidth=1)

        self.crff= Frame(self.master, bg="alice blue")
        self.crff.configure(width=800,height=10000)
        self.crff.place(x=500, y=200)


       # lblinfo = Label(self.crf, font=('ariel', 20, 'bold',), text=localtime, fg="Purple", bd=10, anchor='w')
        #lblinfo.grid(row=1, column=0)
        #self.crff = Frame(self.master, width=800,height=700, bg="pink", relief=SUNKEN)
        #self.crff.pack(side=TOP)
        Label(self.crff, text='Username ', font=('times new roman', 20,"bold"),bg="white").grid( row=1,column=0,pady=20, padx=10)
        Entry(self.crff,bd="5" ,textvariable=self.n_username,relief=GROOVE, font=('times new roman', 20, "bold")).grid(row=1, column=1,padx=20)
        Label(self.crff, text='Password ', font=('times new roman', 20, "bold"), bg="white").grid(row=2, column=0,
                                                                                                   pady=20, padx=10)
        Entry(self.crff, bd="5",textvariable = self.n_password,show='*',relief = GROOVE, font=('times new roman', 20, "bold")).grid(row=2, column=1, padx=20)
        Label(self.crff, text='Email Id', font=('times new roman', 20, "bold"), bg="white").grid(row=3, column=0,pady=20, padx=10)
        Entry(self.crff, bd="5",textvariable = self.n_email, relief = GROOVE , font=('times new roman', 20, "bold")).grid(row=3, column=1, padx=20)
        Button(self.crff, text='Send OTP',width=15, background='white', font=('times new roman', 14, "bold"),
               command=self.otp).grid(row=5, column=0)
        Entry(self.crff, textvariable=self.n_otp, bd=3, font=('times new roman', 20, "bold")).grid(row=5, column=1)
        Button(self.crff, text='Create Account', background='white',width=15, font=('times new roman', 14, "bold"),
               command=self.new_user).grid(row=9, column=0)
        Button(self.crff, text='Go to Login', background='white',width=15, font=('times new roman', 14, "bold"),
               command=self.log).grid(row=9, column=1)

    def new_user(self):
        
        with sqlite3.connect('database.db') as db:
            c = db.cursor()

        if self.n_username.get() != ' ' and self.n_password.get() != ' ' and self.n_email.get() != ' ':
            find_user = ('SELECT * FROM user WHERE username = ?')
            c.execute(find_user, [(self.n_username.get())])

            if str(self.n_otp.get())!=str(self.otp1):
                ms.showerror('Error!', 'Enter correct otp or email address')
            elif c.fetchall():
                ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
            else:
                insert = 'INSERT INTO user(username,password,email) VALUES(?,?,?)'
                c.execute(insert, [(self.n_username.get()), (self.n_password.get()), (self.n_email.get())])
                db.commit()

                ms.showinfo('Success!', 'Account Created!')
                self.log()
        else:
            ms.showerror('Error!', 'Please Enter the details.')

    def log(self):
        self.master.destroy()




#================================================Price=================================================================

class Price:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x400+0+0")
        self.master.title("Price List")
        self.frame = Frame(self.master, bg="pink")
        self.frame.pack()
        tops = Frame(self.master, width=1600, height=50, bg="pink", relief=SUNKEN)
        tops.pack(side=TOP)

        roo = Frame(self.master, width=800, height=700, relief=SUNKEN)
        roo.pack(side=LEFT)

        rf = Frame(self.master, width=300, height=700, relief=SUNKEN)
        rf.pack(side=RIGHT)

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
        lblinfo.grid(row=0, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="_____________", fg="white", anchor=W)
        lblinfo.grid(row=0, column=2)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
        lblinfo.grid(row=0, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fries ", fg="steel blue", anchor=W)
        lblinfo.grid(row=1, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="100", fg="steel blue", anchor=W)
        lblinfo.grid(row=1, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pasta", fg="steel blue", anchor=W)
        lblinfo.grid(row=2, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="180", fg="steel blue", anchor=W)
        lblinfo.grid(row=2, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
        lblinfo.grid(row=3, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
        lblinfo.grid(row=3, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Sizzlers", fg="steel blue", anchor=W)
        lblinfo.grid(row=4, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="300", fg="steel blue", anchor=W)
        lblinfo.grid(row=4, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cookies", fg="steel blue", anchor=W)
        lblinfo.grid(row=5, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="120", fg="steel blue", anchor=W)
        lblinfo.grid(row=5, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheesecake", fg="steel blue", anchor=W)
        lblinfo.grid(row=6, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="200", fg="steel blue", anchor=W)
        lblinfo.grid(row=6, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza", fg="steel blue", anchor=W)
        lblinfo.grid(row=7, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="250", fg="steel blue", anchor=W)
        lblinfo.grid(row=7, column=3)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger", fg="steel blue", anchor=W)
        lblinfo.grid(row=8, column=0)
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="150", fg="steel blue", anchor=W)
        lblinfo.grid(row=8, column=3)

 # ============================BILLING CLASS=================================================================================================

class Billing:
    def __init__(self, master):
        self.master = master
        self.master.title("RESTAURANT BILLING SYSTEM")
        self.master.geometry("1600x800+0+0")
        #self.bg = Image.open("cafe.png")
        #self.bg = self.bg.resize((2000, 1000))
        #self.bg = ImageTk.PhotoImage(self.bg)

        self.master.config( bg="alice blue")
        self.frame = Frame(self.master,bg="alice blue",bd=10)

        self.frame.pack()

        # -------------------------------------------------------------------------------------------------------------------------------------------------------------------
        tops = Frame(self.master, width=1600, height=50, bg="pink", relief=SUNKEN)
        tops.pack(side=TOP)

        lf = Frame(self.master, width=800,bd=10 ,height=700, bg="alice blue",relief=SUNKEN)
        lf.pack(side=LEFT)

        rf = Frame(self.master, width=300, height=700, bg="alice blue",relief=SUNKEN,bd=10)
        rf.pack(side=RIGHT)
        #bg1_lbl = Label(self.master, image=self.bg).pack()
        heading = Label(tops, font=('Ink Free', 100, 'bold'), text="VJ  Cafe", fg="Purple", bg="alice blue",bd=10, anchor='w')
        heading.grid(row=0, column=0)

        # -----time----
        localtime = time.asctime(time.localtime(time.time()))

        # ----labelinfo----
        lblinfo = Label(tops, font=('Ink Free', 100, 'bold',), text="VJ Cafe",fg="Purple",bg="alice blue",bd=10, anchor='w')
        lblinfo.grid(row=0, column=0)
        lblinfo = Label(tops, font=('ariel', 20, 'bold',), text=localtime, fg="Purple", bd=10, anchor='w')
        lblinfo.grid(row=1, column=0)
        lblinfo = Label(tops, font=('Ink Free', 20, 'bold',), text="VJ Cafe,H R Mahajani Rd,Matunga,Mumbai,Maharastra 400019", fg="Purple", bd=10, anchor='w')
        lblinfo.grid(row=2, column=0)
       # lblinfo = Label(tops, font=('Ink Free', 40, 'bold',),text="BRING A LAPTOP, A FRIEND OR A BOOK", bd=10, anchor='w')
        #lblinfo.grid(row=3, column=0)



        # ................buttons.................
        def Receipt():
            COF = float(Fries.get())
            COP = float(Pasta.get())
            COD = float(Drinks.get())
            COS = float(Sizzlers.get())
            CO = float(Cookies.get())
            CC = float(Cheesecake.get())
            COPP = float(Pizza.get())
            COB = float(Burger.get())

            CostOfFries = COF * 100
            CostOfDrinks = COD * 50
            CostOfPasta = COP * 180
            CostOfSizzlers = COS * 300
            CostOfCookies = CO * 120
            CostOfCheesecake = CC * 200
            CostOfPizza = COPP * 250
            CostOfBurger = COB * 150

            CostOfMeal = "Rs", str(
                '%.2f' % (
                        CostOfFries + CostOfDrinks + CostOfPasta + CostOfSizzlers + CostOfCheesecake + CostOfCookies + CostOfPizza + CostOfBurger))
            PayTax = ((
                              CostOfFries + CostOfDrinks + CostOfPasta + CostOfSizzlers + CostOfCheesecake + CostOfCookies + CostOfPizza + CostOfBurger) * 0.02)
            Total = (
                    CostOfFries + CostOfDrinks + CostOfPasta + CostOfSizzlers + CostOfCheesecake + CostOfCookies + CostOfPizza + CostOfBurger)

            OverallCost = "Rs", str('%.2f' % (Total + PayTax))

            TaxPaid = "Rs", str('%.2f' % (PayTax))

            Tax.set(TaxPaid)
            TotalCost.set(OverallCost)

            txtReceipt.delete("1.0", END)
            x = random.randint(10903, 609235)
            # randomRef = str(x)
            y = "BILL"
            ref = y + str(x)
            # rf.set("BILL"+randomRef)
            txtReceipt.insert(END, 'Receipt Ref:\t\t\t' + ref + '\n' + localtime + "\n")
            txtReceipt.insert(END, 'ITEM:\t\t\t' + "Cost of Items\n")
            txtReceipt.insert(END, 'Fries:\t\t\t' + str(CostOfFries) + "\n")
            txtReceipt.insert(END, 'Cheesecake:\t\t\t' + str(CostOfCheesecake) + "\n")
            txtReceipt.insert(END, 'Pizza:\t\t\t' + str(CostOfPizza) + "\n")
            txtReceipt.insert(END, 'Burger:\t\t\t' + str(CostOfBurger) + "\n")
            txtReceipt.insert(END, 'Drinks:\t\t\t' + str(CostOfDrinks) + "\n")
            txtReceipt.insert(END, 'Pasta:\t\t\t' + str(CostOfPasta) + "\n")
            txtReceipt.insert(END, 'Sizzlers:\t\t\t' + str(CostOfSizzlers) + "\n")
            txtReceipt.insert(END, 'Cookies:\t\t\t' + str(CostOfCookies) + "\n")
            txtReceipt.insert(END, 'Tax:\t\t\t' + Tax.get() + "\n")
            txtReceipt.insert(END, 'Total Cost:\t\t\t' + TotalCost.get() + "\n")
            with sqlite3.connect('database.db') as db:
                c = db.cursor()

            # Find user If there is any take proper action
            find_user = ('SELECT * FROM user WHERE username = ? and password = ?')

            c.execute(find_user, [str(username1), str(password1)])
            result1 = c.fetchall()
            email1(result1[0][2])
        def Ref():
            x = random.randint(200000, 700000)
            randomRef = str(x)
            rand.set(randomRef)

            COF = float(Fries.get())
            COP = float(Pasta.get())
            COD = float(Drinks.get())
            COS = float(Sizzlers.get())
            CO = float(Cookies.get())
            CC = float(Cheesecake.get())
            COPP = float(Pizza.get())
            COB = float(Burger.get())

            CostOfFries = COF * 100
            CostOfDrinks = COD * 50
            CostOfPasta = COP * 180
            CostOfSizzlers = COS * 300
            CostOfCookies = CO * 120
            CostOfCheesecake = CC * 200
            CostOfPizza = COPP * 250
            CostOfBurger = COB * 150

            CostOfMeal = "Rs", str(
                '%.2f' % (
                            CostOfFries + CostOfDrinks + CostOfPasta + CostOfSizzlers + CostOfCheesecake + CostOfCookies + CostOfPizza + CostOfBurger))
            PayTax = ((
                                  CostOfFries + CostOfDrinks + CostOfPasta + CostOfSizzlers + CostOfCheesecake + CostOfCookies + CostOfPizza + CostOfBurger) * 0.02)
            Total = (
                        CostOfFries + CostOfDrinks + CostOfPasta + CostOfSizzlers + CostOfCheesecake + CostOfCookies + CostOfPizza + CostOfBurger)

            OverallCost = "Rs", str('%.2f' % (Total + PayTax))

            TaxPaid = "Rs", str('%.2f' % (PayTax))

            Tax.set(TaxPaid)
            TotalCost.set(OverallCost)
            txtReceipt.delete("1.0", END)
            x = random.randint(10903, 609235)
            # randomRef = str(x)
            y = "BILL"
            ref = y + str(x)
            # rf.set("BILL"+randomRef)
            txtReceipt.insert(END, 'Receipt Ref:\t\t\t' + ref + '\n' + localtime + "\n")
            txtReceipt.insert(END, 'ITEM:\t\t\t' + "Cost of Items\n")
            txtReceipt.insert(END, 'Fries:\t\t\t' + str(CostOfFries) + "\n")
            txtReceipt.insert(END, 'Cheesecake:\t\t\t' + str(CostOfCheesecake) + "\n")
            txtReceipt.insert(END, 'Pizza:\t\t\t' + str( CostOfPizza) + "\n")
            txtReceipt.insert(END, 'Burger:\t\t\t' + str(CostOfBurger) + "\n")
            txtReceipt.insert(END, 'Drinks:\t\t\t' + str(CostOfDrinks) + "\n")
            txtReceipt.insert(END, 'Pasta:\t\t\t' + str(CostOfPasta) + "\n")
            txtReceipt.insert(END, 'Sizzlers:\t\t\t' + str(CostOfSizzlers) + "\n")
            txtReceipt.insert(END, 'Cookies:\t\t\t' + str(CostOfCookies) + "\n")
            txtReceipt.insert(END, 'Tax:\t\t\t' + Tax.get() + "\n")
            txtReceipt.insert(END, 'Total Cost:\t\t\t' + TotalCost.get() + "\n")

        def qExit():
            self.master.destroy()

        def Reset():
            rand.set("")
            Fries.set("0")
            Pasta.set("0")
            Drinks.set("0")
            Sizzlers.set("0")
            Cookies.set("0")
            Cheesecake.set("0")
            Pizza.set("0")
            Burger.set("0")
            Tax.set("")
            TotalCost.set("")

        def email1(emailid):
            server = smtplib.SMTP('smtp.gmail.com', 587)

            server.starttls()
            # Next, log in to the server
            server.login("dishacheck123@gmail.com", "2rasika4")
            msg=EmailMessage()
            msg['from']='VJCAFE'
            msg['subject']='ORDER PLACED'
            #msg.set_content("Thank you for ordering from VJ CAFE! Your order will be at your door soon!HAPPY EATING!!!")
            msg.add_alternative('''
            <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>

<head>
    <meta charset="UTF-8">
    <meta content="width=device-width, initial-scale=1" name="viewport">
    <meta name="x-apple-disable-message-reformatting">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta content="telephone=no" name="format-detection">
    <title></title>
    <!--[if (mso 16)]>
    <style type="text/css">
    a {text-decoration: none;}
    </style>
    <![endif]-->
    <!--[if gte mso 9]><style>sup { font-size: 100% !important; }</style><![endif]-->
</head>

<body>
    <div class="es-wrapper-color">
        <!--[if gte mso 9]>
<v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
<v:fill type="tile" color="#e5cea7"></v:fill>
</v:background>
<![endif]-->
        <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0">
            <tbody>
                <tr>
                    <td class="esd-email-paddings" valign="top">
                        <table class="es-header esd-header-popover" cellspacing="0" cellpadding="0" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" esd-custom-block-id="2105" align="center">
                                        <table class="es-header-body" width="600" cellspacing="0" cellpadding="0" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p10" esd-general-paddings-checked="false" align="left">
                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="580" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-image" align="center" style="position: relative;"><a target="_blank" href="https://viewstripo.email/"><img src="https://fhgoha.stripocdn.email/content/guids/957f7204-fb70-4d1b-99fb-4837014f8c14/images/4801574174060223.jpg" alt="Shop Tea logo" title="Shop Tea logo" width="251" style="display: block; width: 251px; height: 68.9688px;"></a></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table class="es-content" cellspacing="0" cellpadding="0" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center">
                                        <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure" align="left">
                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="600" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-banner" style="position: relative;" align="center" esdev-config="h2"><a target="_blank"><img class="adapt-img esdev-stretch-width esdev-banner-rendered" src="https://fhgoha.stripocdn.email/content/guids/bannerImgGuid/images/67751574176023573.png" alt title width="600" style="display: block;"></a></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table class="es-content" cellspacing="0" cellpadding="0" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" esd-custom-block-id="3389" align="center">
                                        <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffdba7" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure" align="left">
                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="600" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody></tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p20t es-p10b es-p20r es-p20l" esd-general-paddings-checked="false" align="left">
                                                        <!--[if mso]><table width="560" cellpadding="0" cellspacing="0"><tr><td width="194"><![endif]-->
                                                        <table class="es-left" cellspacing="0" cellpadding="0" align="left">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="es-m-p0r es-m-p20b esd-container-frame" width="174" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-spacer es-p15t es-p15b" align="center">
                                                                                        <table width="100%" height="100%" cellspacing="0" cellpadding="0" border="0">
                                                                                            <tbody>
                                                                                                <tr>
                                                                                                    <td style="border-bottom: 1px solid rgb(170, 99, 23); background: rgba(0, 0, 0, 0) none repeat scroll 0% 0%; height: 1px; width: 100%; margin: 0px;"></td>
                                                                                                </tr>
                                                                                            </tbody>
                                                                                        </table>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                    <td class="es-hidden" width="20"></td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td width="173"><![endif]-->
                                                        <table class="es-left" cellspacing="0" cellpadding="0" align="left">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="es-m-p20b esd-container-frame" width="173" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-text es-p5b" align="center">
                                                                                        <h2 style="color: rgb(51, 51, 51);">Contact us</h2>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td width="20"></td><td width="173"><![endif]-->
                                                        <table class="es-right" cellspacing="0" cellpadding="0" align="right">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="173" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-spacer es-p15t es-p15b" align="center">
                                                                                        <table width="100%" height="100%" cellspacing="0" cellpadding="0" border="0">
                                                                                            <tbody>
                                                                                                <tr>
                                                                                                    <td style="border-bottom: 1px solid rgb(170, 99, 23); background: rgba(0, 0, 0, 0) none repeat scroll 0% 0%; height: 1px; width: 100%; margin: 0px;"></td>
                                                                                                </tr>
                                                                                            </tbody>
                                                                                        </table>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p10t es-p20b es-p20r es-p20l" esd-general-paddings-checked="false" esd-custom-block-id="2119" align="left">
                                                        <!--[if mso]><table width="560" cellpadding="0" cellspacing="0"><tr><td width="178" valign="top"><![endif]-->
                                                        <table class="es-left" cellspacing="0" cellpadding="0" align="left">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="es-m-p0r es-m-p20b esd-container-frame" width="178" valign="top" align="center">
                                                                        <table style="background-color: rgb(255, 235, 204);" width="100%" cellspacing="0" cellpadding="0" bgcolor="#ffebcc">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-image es-p10t es-p10b" align="center"><a target="_blank"><img class="adapt-img" src="https://fhgoha.stripocdn.email/content/guids/CABINET_9eace4b41023d36a1181d08854bdcb5f/images/21181509377817646.png" alt="Contact us icon" title="Contact us icon" width="178"></a></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td width="20"></td><td width="362" valign="top"><![endif]-->
                                                        <table cellspacing="0" cellpadding="0" align="right">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="362" align="left">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="es-m-txt-с esd-block-text" esdev-links-color="#aa6317" align="left">
                                                                                        <p style="color: #333333; line-height: 200%;"><span style="line-height: 200%;"><strong><span style="font-size: 16px;">Address: </span></strong><strong><span style="font-size: 16px;">H R Mahajani Rd, Matunga, Mumbai, Maharashtra 400019</span></strong></span></p>
                                                                                        <p style="color: #333333; line-height: 200%;"><span style="font-size: 16px; line-height: 200%;"><strong>Phone: 022 2419 8101</strong></span></p>
                                                                                        <p style="color: #333333; line-height: 200%;"><br></p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table class="es-content" cellspacing="0" cellpadding="0" align="center">
                            <tbody>
                                <tr></tr>
                                <tr>
                                    <td class="esd-stripe" esd-custom-block-id="2120" align="center">
                                        <table class="es-footer-body" style="background-color: rgb(153, 195, 85);" width="600" cellspacing="0" cellpadding="0" bgcolor="#99c355" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p15t es-p20b es-p10r es-p10l" esd-general-paddings-checked="false" align="left">
                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="580" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-image es-p5b" align="center"><a target="_blank"><img class="adapt-img" src="https://fhgoha.stripocdn.email/content/guids/957f7204-fb70-4d1b-99fb-4837014f8c14/images/58341574177004879.png" alt="Tea Shop logo" title="Tea Shop logo" width="190" style="display: block;"></a></td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td class="esd-block-text" align="center">
                                                                                        <p style="color: #333333;">Tea shop © 2019&nbsp;All rights reserved</p>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td class="esd-block-text" esdev-links-color="#333333" align="center">
                                                                                        <p style="color: #333333;">You are receiving this email because you have visited our site</p>
                                                                                        <p style="color: #333333;">or asked us about regular newsletter.</p>
                                                                                        <p style="color: #333333;">Vector graphics designed by <a target="_blank" style="color: #333333;" href="http://www.freepik.com/">Freepik</a></p>
                                                                                        <p style="line-height: 150%; color: #333333; font-size: 13px;"><a target="_blank" style="font-size: 13px; color: #333333;" href>Unsubscribe</a>&nbsp; | <a target="_blank" style="font-size: 13px; color: #333333;" href>Update Preferences</a> | <a target="_blank" style="line-height: 150%; font-size: 13px; color: #333333;">Customer Support</a></p>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td class="esd-block-social es-p20t" align="center">
                                                                                        <table class="es-table-not-adapt es-social" cellspacing="0" cellpadding="0">
                                                                                            <tbody>
                                                                                                <tr>
                                                                                                    <td class="es-p10r" valign="top" align="center"><a href><img title="Twitter" src="https://stripo.email/cabinet/assets/editor/assets/img/social-icons/circle-black/twitter-circle-black.png" alt="Tw" width="32"></a></td>
                                                                                                    <td class="es-p10r" valign="top" align="center"><a href><img title="Facebook" src="https://stripo.email/cabinet/assets/editor/assets/img/social-icons/circle-black/facebook-circle-black.png" alt="Fb" width="32"></a></td>
                                                                                                    <td class="es-p10r" valign="top" align="center"><a href><img title="Youtube" src="https://stripo.email/cabinet/assets/editor/assets/img/social-icons/circle-black/youtube-circle-black.png" alt="Yt" width="32"></a></td>
                                                                                                    <td valign="top" align="center"><a href><img title="Vkontakte" src="https://stripo.email/cabinet/assets/editor/assets/img/social-icons/circle-black/vk-circle-black.png" alt="Vk" width="32"></a></td>
                                                                                                </tr>
                                                                                            </tbody>
                                                                                        </table>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table class="esd-footer-popover es-content" cellspacing="0" cellpadding="0" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center">
                                        <table class="es-content-body" style="background-color: transparent;" width="600" cellspacing="0" cellpadding="0" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p30t es-p30b es-p20r es-p20l" align="left">
                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="560" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-image es-infoblock" align="center"><a target="_blank" href="http://viewstripo.email/?utm_source=templates&utm_medium=email&utm_campaign=beverage_coffee&utm_content=shopping_festival"><img src="https://fhgoha.stripocdn.email/content/guids/CABINET_9df86e5b6c53dd0319931e2447ed854b/images/64951510234941531.png" alt width="125"></a></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</body>

</html>     ''',subtype="html")
            server.sendmail("dishacheck123@gmail.com", emailid, msg.as_string())

       # def email1(emailid):
            '''server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            # Next, log in to the server
            server.login("dishacheck123@gmail.com", "2rasika4")

            # Send the mail
            msg = 
        # The /n separates the message from the headers
            server.sendmail("dishacheck123@gmail.com", emailid, msg)'''

        def price():
            # Price=
            app = Price(Toplevel())

        # ..............................................................................

        # --------------------------------------Resturant Information  1------------------------------------------------------------

        rand = StringVar()
        """lblReference = Label(lf,font = ('arial','16','bold'),text="Reference",bd = 16, anchor = 'w')
        lblReference.grid(row=0,column=0)
        txtReference = Entry(lf,font = ('arial','16','bold'),textvariable = rand,bd =10,insertwidth=4,bg ='pink',justify='right')
        txtReference.grid(row=0,column=1)"""

        Fries = StringVar()
        Fries.set("0")
        lblFries = Label(lf, font=('Ink Free', '16', 'bold'), text="Large Fries", bd=16, anchor='w', bg="alice blue")
        lblFries.grid(row=1, column=0)
        txtFries = Spinbox(lf, from_=0, textvariable=Fries,bg='pink', font=('arial', '16', 'bold'), justify='right',
                           to=1000, relief=GROOVE)
        txtFries.grid(row=1, column=1)

        Pasta = StringVar()
        Pasta.set("0")
        lblVeg = Label(lf, bg="alice blue", font=('Ink Free', '16', 'bold'), text="Pasta", bd=16, anchor='w')
        lblVeg.grid(row=2, column=0)
        txtVeg = Spinbox(lf, from_=0, textvariable=Pasta, font=('arial', '16', 'bold'), bg='pink', justify='right',
                         to=1000)
        txtVeg.grid(row=2, column=1)
        """font = ('arial','16','bold'),insertwidth=4,,"""

        Sizzlers = StringVar()
        Sizzlers.set("0")
        lblChicken = Label(lf, font=('Ink Free', '16', 'bold'), bg="alice blue", text="Sizzlers", bd=16, anchor='w')
        lblChicken.grid(row=3, column=0)
        txtChicken = Spinbox(lf, from_=0, textvariable=Sizzlers, font=('arial', '16', 'bold'), bg='pink',
                             justify='right',
                             to=1000)
        txtChicken.grid(row=3, column=1)

        Drinks = StringVar()
        Drinks.set("0")
        lblDrinks = Label(lf, font=('Ink Free', '16', 'bold'), text="Drinks", bd=16, anchor='w', bg="alice blue")
        lblDrinks.grid(row=3, column=2)
        txtDrinks = Spinbox(lf, from_=0, textvariable=Drinks, font=('arial', '16', 'bold'), bg='pink', justify='right',
                            to=1000)
        txtDrinks.grid(row=3, column=3)

        Pizza = StringVar()
        Pizza.set("0")
        lblDrinks = Label(lf, font=('Ink Free', '16', 'bold'), text="Pizza", bd=16, anchor='w', bg="alice blue")
        lblDrinks.grid(row=4, column=2)
        txtDrinks = Spinbox(lf, font=('arial', '16', 'bold'), textvariable=Pizza,  insertwidth=4, bg='pink',
                            justify='right', to=1000)
        txtDrinks.grid(row=4, column=3)

        Burger = StringVar()
        Burger.set("0")
        lblBurger = Label(lf, font=('Ink Free', '16', 'bold'), text="Burger", bd=16, anchor='w', bg="alice blue")
        lblBurger.grid(row=4, column=0)
        txtBurger = Spinbox(lf, font=('arial', '16', 'bold'), textvariable=Burger, insertwidth=4, bg='pink',
                            justify='right', to=1000)
        txtBurger.grid(row=4, column=1)

        Cookies = StringVar()
        Cookies.set("0")
        lblservice = Label(lf, font=('Ink Free', '16', 'bold'), text="Cookies ", bd=16, anchor='w', bg="alice blue")
        lblservice.grid(row=1, column=2)
        txtservice = Spinbox(lf, from_=0, textvariable=Cookies, font=('arial', '16', 'bold'), bg='pink',
                             justify='right',
                             to=1000)
        txtservice.grid(row=1, column=3)

        Tax = StringVar()
        lblTax = Label(lf, font=('Ink Free', '16', 'bold'), text="Tax", bd=16, anchor='w', bg="alice blue")
        lblTax.grid(row=5, column=0)
        txtTax = Label(lf, font=('arial', '16', 'bold'), textvariable=Tax, bd=10, bg="alice blue")
        txtTax.grid(row=5, column=1)

        Cheesecake = StringVar()
        Cheesecake.set("0")
        lblservice = Label(lf, font=('Ink Free', '16', 'bold'), text="Cheesecake ", bd=16, anchor='w', bg="alice blue")
        lblservice.grid(row=2, column=2)
        txtservice = Spinbox(lf, from_=0, textvariable=Cheesecake, font=('arial', '16', 'bold'), bg='pink',
                             justify='right',
                             to=1000)
        txtservice.grid(row=2, column=3)

        TotalCost = StringVar()
        lblTotalCost = Label(lf, font=('Ink Free', '16', 'bold'), text="Total", bd=16, anchor='w', bg="alice blue")
        lblTotalCost.grid(row=5, column=2)
        txtTotalCost = Label(lf, font=('arial', '16', 'bold'), textvariable=TotalCost, bd=10, bg="alice blue")
        txtTotalCost.grid(row=5, column=3)
        # -----------------------------------------------Receipt--------------------------------------------------------------------------------------

        txtReceipt = Text(rf, width=57, height=19, bg="white", bd=10, font=('arial', 12, 'bold'))
        txtReceipt.grid(row=0, column=0)
        # --------------------------Buttons-----------------------------------------------------
        btnprice = Button(lf, padx=16, pady=8, bd=10, fg="black", font=('Ink Free', 16, 'bold'), width=10, text="Price",
                          bg="pink", command=price)
        btnprice.grid(row=8, column=0)
        btnTotal = Button(lf, padx=16, pady=8, bd=10, fg='Black', font=('Ink Free', '16', 'bold'), width=10, text="Total",
                          bg='pink', command=Ref).grid(row=8, column=1)
        btnReset = Button(lf, padx=16, pady=8, bd=10, fg='Black', font=('Ink Free', '16', 'bold'), width=10, text="Reset",
                          bg='pink', command=Reset).grid(row=8, column=2)
        btnExit = Button(lf, padx=16, pady=8, bd=10, fg='Black', font=('Ink Free', '16', 'bold'), width=10, text="Logout",
                         bg='pink', command=qExit).grid(row=8, column=4)

        btnReceipt = Button(lf, padx=16, pady=8, bd=10, fg='Black', font=('Ink Free', '16', 'bold'), width=10,
                            text="Place Order", bg='pink', command=Receipt).grid(row=8, column=3)


if __name__ == '__main__':
    root = Tk()
    root.title('Login')
    root.geometry('800x750+300+300')
    main(root)
    root.mainloop()

