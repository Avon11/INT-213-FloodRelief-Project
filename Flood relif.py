from tkinter import *
from PIL import ImageTk, Image
import sqlite3


def front():
    windowf = Tk()
    windowf.title("Flood Relief ")
    windowf.geometry("1500x800")
    windowf.configure(bg="MistyRose2")
    canvasfg = Canvas(windowf)
    imagelogo = ImageTk.PhotoImage(Image.open("logo.png"))
    canvasfg.create_image(175, 100, image=imagelogo)
    canvasfg.configure(bg="MistyRose2")
    canvasfg.pack()
    frame1 = Frame(windowf)
    frame1.pack()
    imgdisaster = ImageTk.PhotoImage(Image.open("Button1.jpeg"))
    disasterinfo = Button(frame1, image=imgdisaster, width=400, height=300, bg="black",command=deathinformation)

    imgcamp = ImageTk.PhotoImage(Image.open("camp 2.png"))
    campinfo = Button(frame1, image=imgcamp, width=400, height=300, bg="black",command=campinformation)


    imgdonation = ImageTk.PhotoImage(Image.open("donation1.jpg"))
    donationinfo = Button(frame1, image=imgdonation, width=400, height=300, bg="black", command=donation)

    disasterinfo.grid(row=0, column=0, padx=20, pady=20)
    campinfo.grid(row=0, column=2, padx=20, pady=20)
    donationinfo.grid(row=0, column=4, padx=20, pady=20)

    frame2 = Frame(windowf)
    frame2.pack()
    aboutus = Label(frame2, text="About US", font=49, bg="MistyRose2").pack(fill="x", ipadx=2, ipady=2)
    contact = Label(frame2, text="Contact Number:9897367795", bg="MistyRose2").pack(fill="x", ipadx=2, ipady=2)
    email = Label(frame2, text="Email:getHelpinFlood@gmail.com", bg="MistyRose2").pack(fill="x", ipadx=2, ipady=2)

    windowf.mainloop()



def campinformation():
    # connect database
    con = sqlite3.connect('camp_database.db')

    # create cursor
    c = con.cursor()

    # create table
    '''
    c.execute(""" CREATE TABLE camp(
        name text,
        address text,
        caddress text,
        phone1 integer,
        phone2 integer,
        adhar integer,
        dob text,
        blood text,
        birthmark text,
        medical text,
        campinfo text,
        dateofarrival text
        )""")
    '''

    def submit():
        # connect database
        con = sqlite3.connect('camp_database.db')

        # create cursor
        c = con.cursor()

        # Insert into table
        c.execute(
            "INSERT INTO camp VALUES(:name, :address, :caddress, :phone1, :phone2, :adhar, :dob, :blood, :birthmark, :medical, :campinfo, :dateofarrival)",

            {
                'name': input_name.get(),
                'address': input_address.get(),
                'caddress': input_caddress.get(),
                'phone1': input_phone1.get(),
                'phone2': input_phone2.get(),
                'adhar': input_adhar.get(),
                'dob': input_dob.get(),
                'blood': input_blood.get(),
                'birthmark': input_birthmark.get(),
                'medical': input_medical.get(),
                'campinfo': input_camp.get(),
                'dateofarrival': input_dateofarrival.get()

            })

        con.commit()
        con.close()
        # clear the text boxes
        entry_name.delete(0, END)
        entry_address.delete(0, END)
        entry_caddress.delete(0, END)
        entry_phone1.delete(0, END)
        entry_phone2.delete(0, END)
        entry_adhar.delete(0, END)
        entry_dob.delete(0, END)
        entry_blood.delete(0, END)
        entry_birthmark.delete(0, END)
        entry_medical.delete(0, END)
        entry_camp.delete(0, END)
        entry_dateofarrival.delete(0, END)

    # For showing data of camp
    def showdata():
        root2 = Tk()
        root2.geometry("1500x900")
        root2.title("Database for Camp")
        root2.config(bg="bisque2")
        # connect database
        con = sqlite3.connect('camp_database.db')
        # create cursor
        c = con.cursor()
        # to display the database
        c.execute("SELECT * from camp")
        record = c.fetchall()

        # loop through records
        print_data_name = ''
        print_data_address = ''
        print_data_phone1 = ''
        print_data_adhar = ''
        print_data_dob = ''
        print_data_blood = ''
        print_data_birthmark = ''
        print_data_medical = ''
        print_data_camp = ''
        print_data_dateofarrival = ''

        for records in record:
            print_data_name += str(records[0]) + " \n"
            print_data_address += str(records[1]) + "\n"
            print_data_phone1 += str(records[3]) + "\n"
            print_data_adhar += str(records[5]) + "\n"
            print_data_dob += str(records[6]) + "\n"
            print_data_blood += str(records[7]) + "\n"
            print_data_birthmark += str(records[8]) + "\n"
            print_data_medical += str(records[9]) + "\n"
            print_data_camp += str(records[10]) + "\n"
            print_data_dateofarrival += str(records[11]) + "\n"

        displaylabel_name = Label(root2, text=print_data_name, bg="bisque2", fg="black", font=("Helvetica", 10))
        displaylabel_address = Label(root2, text=print_data_address, bg="bisque2", fg="black", font=("Helvetica", 10))
        displaylabel_phone1 = Label(root2, text=print_data_phone1, bg="bisque2", fg="black", font=("Helvetica", 10))
        displaylabel_adhar = Label(root2, text=print_data_adhar, bg="bisque2", fg="black", font=("Helvetica", 10))
        displaylabel_dob = Label(root2, text=print_data_dob, bg="bisque2", fg="black", font=("Helvetica", 10))
        displaylabel_blood = Label(root2, text=print_data_blood, bg="bisque2", fg="black", font=("Helvetica", 10))
        displaylabel_birthmark = Label(root2, text=print_data_birthmark, bg="bisque2", fg="black", font=("Helvetica", 10))
        displaylabel_medical = Label(root2, text=print_data_medical, bg="bisque2", fg="black", font=("Helvetica", 10))
        displaylabel_camp = Label(root2, text=print_data_camp, bg="bisque2", fg="black", font=("Helvetica", 10))
        displaylabel_dateofarrival = Label(root2, text=print_data_dateofarrival, bg="bisque2", fg="black",font=("Helvetica", 10))

        Label(root2, text="Name", bg="bisque2", fg="black", font=("Helvetica", 15)).grid(row=0, column=1, padx=5,
                                                                                         pady=3)
        Label(root2, text="Address", bg="bisque2", fg="black", font=("Helvetica", 15)).grid(row=0, column=2, padx=5,
                                                                                            pady=3)

        Label(root2, text="Phone number 1", bg="bisque2", fg="black", font=("Helvetica", 15)).grid(row=0, column=3,
                                                                                                   padx=5, pady=3)
        Label(root2, text="Adhar Card ", bg="bisque2", fg="black", font=("Helvetica", 15)).grid(row=0, column=4,
                                                                                                padx=5, pady=3)
        Label(root2, text="Date of birth", bg="bisque2", fg="black", font=("Helvetica", 15)).grid(row=0, column=5,
                                                                                                  padx=5, pady=3)
        Label(root2, text="Blood Group", bg="bisque2", fg="black", font=("Helvetica", 15)).grid(row=0, column=6,
                                                                                                padx=5, pady=3)
        Label(root2, text="Birthmark", bg="bisque2", fg="black", font=("Helvetica", 15)).grid(row=0, column=7, padx=5,
                                                                                              pady=3)
        Label(root2, text="Medical", bg="bisque2", fg="black", font=("Helvetica", 15)).grid(row=0, column=8, padx=5,
                                                                                            pady=3)
        Label(root2, text="Camp Info.", bg="bisque2", fg="black", font=("Helvetica", 15)).grid(row=0, column=9,
                                                                                               padx=5, pady=3)
        Label(root2, text="Date of Arrival", bg="bisque2", fg="black", font=("Helvetica", 15)).grid(row=0, column=10,padx=5, pady=3)

        displaylabel_name.grid(row=1, column=1, padx=5, pady=5)
        displaylabel_address.grid(row=1, column=2, padx=5, pady=5)
        displaylabel_phone1.grid(row=1, column=3, padx=5, pady=5)
        displaylabel_adhar.grid(row=1, column=4, padx=5, pady=5)
        displaylabel_dob.grid(row=1, column=5, padx=5, pady=5)
        displaylabel_blood.grid(row=1, column=6, padx=5, pady=5)
        displaylabel_birthmark.grid(row=1, column=7, padx=5, pady=5)
        displaylabel_medical.grid(row=1, column=8, padx=5, pady=5)
        displaylabel_camp.grid(row=1, column=9, padx=5, pady=5)
        displaylabel_dateofarrival.grid(row=1, column=10, padx=5, pady=5)

        root2.mainloop()

        con.commit()
        con.close()

    #######################################################################################################################

    window = Tk()
    window.title("Camp Information")
    window.geometry("1500x900")
    window.config(bg="snow")
    frame1 = Frame(window)
    frame1.pack()
    heading_label = Label(frame1, text="Camp Information Portal", bg="snow", fg="black", font=("Helvetica", 28))
    name_label = Label(frame1, text="NAME", bg="snow", fg="black", font=("Helvetica", 15))
    address_label = Label(frame1, text="ADDRESS", bg="snow", fg="black", font=("Helvetica", 15))
    caddress_label = Label(frame1, text="CORRESPONDING ADDRESS", bg="snow", fg="black", font=("Helvetica", 15))
    phone1_label = Label(frame1, text="PHONE NUMBER", bg="snow", fg="black", font=("Helvetica", 15))
    phone2_label = Label(frame1, text="ADDITIONAL PHONE NUMBER", bg="snow", fg="black", font=("Helvetica", 15))
    blood_label = Label(frame1, text="BLOOD GROUP", bg="snow", fg="black", font=("Helvetica", 15))
    birthmrk_label = Label(frame1, text="BIRTH MARK", bg="snow", fg="black", font=("Helvetica", 15))
    dob_label = Label(frame1, text="DATE OF BIRTH", bg="snow", fg="black", font=("Helvetica", 15))
    adhar_label = Label(frame1, text="ADHAR CARD NUMBER", bg="snow", fg="black", font=("Helvetica", 15))
    medical_label = Label(frame1, text="MEDICAL CONDITION", bg="snow", fg="black", font=("Helvetica", 15))
    camp_label = Label(frame1, text="CAMP NUMBER", bg="snow", fg="black", font=("Helvetica", 15))
    date_label = Label(frame1, text="DATE OF ARRIVAL", bg="snow", fg="black", font=("Helvetica", 15))
    enterbutton = Button(frame1, text="ENTER", bg="azure", fg="black", font=("Helvetica", 15), command=submit)
    showdatabutton = Button(frame1, text="SHOW DATA", bg="azure", fg="black", font=("Helvetica", 15), command=showdata)

    input_name = StringVar()
    entry_name = Entry(frame1, textvariable=input_name)

    input_address = StringVar()
    entry_address = Entry(frame1, textvariable=input_address)

    input_caddress = StringVar()
    entry_caddress = Entry(frame1, textvariable=input_caddress)

    input_phone1 = StringVar()
    entry_phone1 = Entry(frame1, textvariable=input_phone1)

    input_phone2 = StringVar()
    entry_phone2 = Entry(frame1, textvariable=input_phone2)

    input_adhar = StringVar()
    entry_adhar = Entry(frame1, textvariable=input_adhar)

    input_dob = StringVar()
    entry_dob = Entry(frame1, textvariable=input_dob)

    input_blood = StringVar()
    entry_blood = Entry(frame1, textvariable=input_blood)

    input_birthmark = StringVar()
    entry_birthmark = Entry(frame1, textvariable=input_birthmark)

    input_medical = StringVar()
    entry_medical = Entry(frame1, textvariable=input_medical)

    input_camp = StringVar()
    entry_camp = Entry(frame1, textvariable=input_camp)

    input_dateofarrival = StringVar()
    entry_dateofarrival = Entry(frame1, textvariable=input_dateofarrival)

    heading_label.grid(row=0, column=1, padx=5, pady=5, ipadx=5, ipady=5, columnspan=2)
    name_label.grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5)
    entry_name.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5)
    address_label.grid(row=2, column=0, padx=5, pady=5, ipadx=5, ipady=5)
    entry_address.grid(row=2, column=1, padx=5, pady=5, ipadx=5, ipady=5)
    caddress_label.grid(row=2, column=2, padx=5, pady=5, ipadx=5, ipady=5)
    entry_caddress.grid(row=2, column=3, padx=5, pady=5, ipadx=5, ipady=5)
    phone1_label.grid(row=3, column=0, padx=5, pady=5, ipadx=5, ipady=5)
    entry_phone1.grid(row=3, column=1, padx=5, pady=5, ipadx=5, ipady=5)
    phone2_label.grid(row=3, column=2, padx=5, pady=5, ipadx=5, ipady=5)
    entry_phone2.grid(row=3, column=3, padx=5, pady=5, ipadx=5, ipady=5)
    adhar_label.grid(row=4, column=0, padx=5, pady=5, ipadx=5, ipady=5)
    entry_adhar.grid(row=4, column=1, padx=5, pady=5, ipadx=5, ipady=5)
    dob_label.grid(row=5, column=0, padx=5, pady=5, ipadx=5, ipady=5)
    entry_dob.grid(row=5, column=1, padx=5, pady=5, ipadx=5, ipady=5)
    blood_label.grid(row=6, column=0, padx=5, pady=5, ipadx=5, ipady=5)
    entry_blood.grid(row=6, column=1, padx=5, pady=5, ipadx=5, ipady=5)
    birthmrk_label.grid(row=7, column=0, padx=5, pady=5, ipadx=5, ipady=5)
    entry_birthmark.grid(row=7, column=1, padx=5, pady=5, ipadx=5, ipady=5)
    medical_label.grid(row=8, column=0, padx=5, pady=5, ipadx=5, ipady=5)
    entry_medical.grid(row=8, column=1, padx=5, pady=5, ipadx=5, ipady=5)
    camp_label.grid(row=9, column=0, padx=5, pady=5, ipadx=5, ipady=5)
    entry_camp.grid(row=9, column=1, padx=5, pady=5, ipadx=5, ipady=5)
    date_label.grid(row=10, column=0, padx=5, pady=5, ipadx=5, ipady=5)
    entry_dateofarrival.grid(row=10, column=1, padx=5, pady=5, ipadx=5, ipady=5)
    enterbutton.grid(row=11, columnspan=5, column=0, padx=5, pady=5, ipadx=5, ipady=5)
    showdatabutton.grid(row=12, columnspan=5, column=0, padx=5, pady=5, ipadx=5, ipady=5)

    # To save the file automatically
    con.commit()
    con.close()
    window.mainloop()



'''***************************************This is Starting of Payment Module**********************************'''


def donation():
    # create table
    '''
    c.execute(""" CREATE TABLE payment (
        name text,
        address text,
        email text,
        contactno integer,
        amount integer
        )""")
    '''
    # connect database
    con = sqlite3.connect('payment_database.db')

    # create cursor
    c = con.cursor()
    #####################################################################################################################
    window1 = Tk()
    window1.title("DONATION PAGE")
    window1.geometry("1500x800")
    window1.configure(bg="bisque2")
    frame1 = Frame(window1, bg="bisque2")
    frame1.pack()

    l1 = Label(frame1, text="GREAT OPPORTUNITIES TO HELP OTHER, STEP OUT AND DONATE HERE!", bg="bisque2", fg="black",
               font=("Helvetica", 28))
    l2 = Label(frame1, text="Pay Online", bg="bisque2", fg="green", font=("Helvetica", 25))
    l3 = Label(frame1, text="NOTE:WE ONLY ACCEPT ONLINE DONATION", bg="bisque2", fg="red", font=("Helvetica", 15))

    v2 = IntVar()
    radiobutton1 = Radiobutton(frame1, text="Credit Card", fg="black", bg="LightCyan3", variable=v2, value=1, height=2,
                               width=15)
    radiobutton2 = Radiobutton(frame1, text="Debit Card", fg="black", bg="LightCyan3", variable=v2, value=2, height=2,
                               width=15)

    l1.grid(row=1, column=1)
    l2.grid(row=2, column=1)
    l3.grid(row=3, column=1)

    radiobutton1.grid(row=4, column=1, padx=5, pady=5)
    radiobutton2.grid(row=5, column=1, padx=5, pady=5)

    frame2 = Frame(window1, bg="bisque2")
    frame2.pack()
    l4 = Label(frame2, text="CARD NUMBER", bg="bisque2", fg="black", font=("Helvetica", 15))
    numbercard = StringVar()
    cardnumber = Entry(frame2, textvariable=numbercard)

    l5 = Label(frame2, text="Expiry date", bg="bisque2", fg="black", font=("Helvetica", 15))
    expirycard = StringVar()
    expirydate = Entry(frame2, textvariable=expirycard)

    l6 = Label(frame2, text="CVV", bg="bisque2", fg="black", font=("Helvetica", 15))
    cvvcard = StringVar()
    cvvnumber = Entry(frame2, textvariable=cvvcard)

    l4.grid(row=0, column=0)
    cardnumber.grid(row=0, column=1, padx=5, pady=5)
    l5.grid(row=1, column=0)
    expirydate.grid(row=1, column=1, padx=5, pady=5)
    l6.grid(row=2, column=0)
    cvvnumber.grid(row=2, column=1, padx=5, pady=5)

    frame3 = Frame(window1, bg="black")
    frame3.pack()
    canvas = Canvas(frame3, width=1500, height=1, bg="black")
    canvas.pack()
    canvas.create_line(300, 35, 300, 200, dash=(5, 2))

    ###################################################################################################################

    def submit():
        # connect database
        con = sqlite3.connect('payment_database.db')

        # create cursor
        c = con.cursor()

        # Insert into table
        c.execute("INSERT INTO payment VALUES(:name, :address, :contact, :email, :amount)",

                  {
                      'name': name.get(),
                      'address': address.get(),
                      'contact': contact.get(),
                      'email': email.get(),
                      'amount': amount.get()
                  })

        con.commit()
        con.close()
        # clear the text boxes
        name.delete(0, END)
        address.delete(0, END)
        contact.delete(0, END)
        email.delete(0, END)
        amount.delete(0, END)
        cardnumber.delete(0, END)
        cvvnumber.delete(0, END)
        expirydate.delete(0, END)

    # show data function

    def showdata():
        root1 = Tk()
        root1.geometry("1500x900")
        root1.config(bg="bisque2")
        root1.title("Donation Database")
        # connect database
        con = sqlite3.connect('payment_database.db')
        # create cursor
        c = con.cursor()
        # to display the database
        c.execute("SELECT *,oid from payment ORDER BY amount desc")
        record = c.fetchall()

        # loop through records
        print_data_name = ''
        print_data_address = ''
        print_data_contact = ''
        print_data_email = ''
        print_data_amount = ''

        for records in record:
            print_data_name += str(records[0]) + " \n"
            print_data_address += str(records[1]) + "\n"
            print_data_contact += str(records[2]) + "\n"
            print_data_email += str(records[3]) + "\n"
            print_data_amount += str(records[4]) + "\n"

        displaylabel_name = Label(root1, text=print_data_name, bg="bisque2", fg="black", font=("Helvetica", 15))
        displaylabel_address = Label(root1, text=print_data_address, bg="bisque2", fg="black", font=("Helvetica", 15))
        displaylabel_contact = Label(root1, text=print_data_contact, bg="bisque2", fg="black", font=("Helvetica", 15))
        displaylabel_email = Label(root1, text=print_data_email, bg="bisque2", fg="black", font=("Helvetica", 15))
        displaylabel_amount = Label(root1, text=print_data_amount, bg="bisque2", fg="black", font=("Helvetica", 15))

        Label(root1, text="Name", bg="bisque2", fg="black", font=("Helvetica", 20)).grid(row=0, column=1, padx=10,
                                                                                         pady=10)
        Label(root1, text="Address", bg="bisque2", fg="black", font=("Helvetica", 20)).grid(row=0, column=2, padx=10,
                                                                                            pady=10)
        Label(root1, text="Contact Number", bg="bisque2", fg="black", font=("Helvetica", 20)).grid(row=0, column=3,padx=10, pady=10)
        Label(root1, text="Email", bg="bisque2", fg="black", font=("Helvetica", 20)).grid(row=0, column=4, padx=10,pady=10)
        Label(root1, text="Amount(In Rs)", bg="bisque2", fg="black", font=("Helvetica", 20)).grid(row=0, column=5,padx=10, pady=10)

        displaylabel_name.grid(row=1, column=1, padx=10, pady=10)
        displaylabel_address.grid(row=1, column=2, padx=10, pady=10)
        displaylabel_contact.grid(row=1, column=3, padx=10, pady=10)
        displaylabel_email.grid(row=1, column=4, padx=10, pady=10)
        displaylabel_amount.grid(row=1, column=5, padx=10, pady=10)
        root1.mainloop()

        con.commit()
        con.close()

    #######################################################################################################################

    frame4 = Frame(window1, bg="bisque2")
    frame4.pack()

    basiclabel = Label(frame4, text="BASIC INFORMATION", bg="bisque2", fg="black", font=("Helvetica", 25))

    amountlabel = Label(frame4, text="Amount", bg="bisque2", fg="black", font=("Helvetica", 15))
    amounte = StringVar()
    amount = Entry(frame4, textvariable=amounte)

    namelabel = Label(frame4, text="NAME", bg="bisque2", fg="black", font=("Helvetica", 15))
    inputname = StringVar()
    name = Entry(frame4, textvariable=inputname)

    addlabel = Label(frame4, text="ADDRESS", bg="bisque2", fg="black", font=("Helvetica", 15))
    inputadd = StringVar()
    address = Entry(frame4, textvariable=inputadd)

    emaillabel = Label(frame4, text="Email", bg="bisque2", fg="black", font=("Helvetica", 15))
    inputemail = StringVar()
    email = Entry(frame4, textvariable=inputemail)

    contactlabel = Label(frame4, text="Contact No.", bg="bisque2", fg="black", font=("Helvetica", 15))
    inputcontact = StringVar()
    contact = Entry(frame4, textvariable=inputcontact)

    enterbutton = Button(frame4, text=" DONATE ", height=2, width=17, bg="PaleGreen2", fg="black",font=("Helvetica", 10), command=submit)

    basiclabel.grid(row=0, column=1, padx=10, pady=10)
    namelabel.grid(row=1, column=0, padx=5, pady=5)
    name.grid(row=1, column=1, padx=5, pady=5)
    addlabel.grid(row=2, column=0, padx=5, pady=5)
    address.grid(row=2, column=1, padx=5, pady=5)
    emaillabel.grid(row=3, column=0, padx=5, pady=5)
    email.grid(row=3, column=1, padx=5, pady=5)
    contactlabel.grid(row=4, column=0, padx=5, pady=5)
    contact.grid(row=4, column=1, padx=5, pady=5)
    amountlabel.grid(row=5, column=0)
    amount.grid(row=5, column=1, padx=5, pady=5)
    enterbutton.grid(row=6, column=1, ipadx=5, ipady=5, padx=5, pady=5)

    # Display data button
    displaydata = Button(frame4, text="See Data", height=2, width=17, bg="azure2", fg="black", font=("Helvetica", 10),command=showdata)
    displaydata.grid(row=7, column=1, columnspan=2, ipadx=5, ipady=5, padx=5, pady=5)

    # To save the file automatically
    con.commit()
    con.close()

    window1.mainloop()


'''********************************This is end of payment Module*******************************************'''


def deathinformation():
    # connect database
    con = sqlite3.connect('death_database.db')

    # create cursor
    c = con.cursor()

    # create table

    '''c.execute(""" CREATE TABLE death (
        name text,
        address text,
        phone1 integer,
        adhar integer,
        dob text,
        birthmark text,
        deathplace text,
        dateofdeath text
        )""")'''

    def submit():
        # connect database
        con = sqlite3.connect('death_database.db')

        # create cursor
        c = con.cursor()

        # Insert into table
        c.execute("INSERT INTO death VALUES(:name , "
                  ":address ,"
                  ":phone1 , "
                  ":adhar ,"
                  ":dob ,"
                  ":birthmark ,"
                  ":deathplace ,"
                  ":dateofdeath)",

                  {
                      'name': input_name.get(),
                      'address': input_address.get(),
                      'phone1': input_phone1.get(),
                      'adhar': input_adhar.get(),
                      'dob': input_dob.get(),
                      'birthmark': input_birthmark.get(),
                      'deathplace': input_birthmark.get(),
                      'dateofdeath': input_dateofdeath.get()

                  })

        con.commit()
        con.close()
        # clear the text boxes
        entry_name.delete(0, END)
        entry_address.delete(0, END)
        entry_phone1.delete(0, END)
        entry_adhar.delete(0, END)
        entry_dob.delete(0, END)
        entry_birthmark.delete(0, END)
        entry_deathplace.delete(0, END)
        entry_dateofdeath.delete(0, END)

    # For showing data of death
    def showdata():
        root2 = Tk()
        root2.geometry("1500x900")
        root2.config(bg="bisque2")
        # connect database
        con = sqlite3.connect('death_database.db')
        # create cursor
        c = con.cursor()
        # to display the database
        c.execute('SELECT * from death')
        record = c.fetchall()

        # loop through records
        print_data_name = ''
        print_data_address = ''
        print_data_phone1 = ''
        print_data_adhar = ''
        print_data_dob = ''
        print_data_birthmark = ''
        print_data_deathplace = ''
        print_data_dateofdeath = ''

        for records in record:
            print_data_name += str(records[0]) + " \n"
            print_data_address += str(records[1]) + "\n"
            print_data_phone1 += str(records[2]) + "\n"
            print_data_adhar += str(records[3]) + "\n"
            print_data_dob += str(records[4]) + "\n"
            print_data_birthmark += str(records[5]) + "\n"
            print_data_deathplace += str(records[6]) + "\n"
            print_data_dateofdeath += str(records[7]) + "\n"

        displaylabel_name = Label(root2, text=print_data_name, bg="bisque2", fg="black", font=("Helvetica", 15))
        displaylabel_address = Label(root2, text=print_data_address, bg="bisque2", fg="black", font=("Helvetica", 15))
        displaylabel_phone1 = Label(root2, text=print_data_phone1, bg="bisque2", fg="black", font=("Helvetica", 15))
        displaylabel_adhar = Label(root2, text=print_data_adhar, bg="bisque2", fg="black", font=("Helvetica", 15))
        displaylabel_dob = Label(root2, text=print_data_dob, bg="bisque2", fg="black", font=("Helvetica", 15))
        displaylabel_birthmark = Label(root2, text=print_data_birthmark, bg="bisque2", fg="black",
                                       font=("Helvetica", 15))
        displaylabel_deathplace = Label(root2, text=print_data_deathplace, bg="bisque2", fg="black",
                                        font=("Helvetica", 15))
        displaylabel_dateofdeath = Label(root2, text=print_data_dateofdeath, bg="bisque2", fg="black",
                                         font=("Helvetica", 15))

        Label(root2, text="Name", bg="bisque2", fg="black", font=("Helvetica", 16)).grid(row=0, column=1, padx=5,
                                                                                         pady=3)
        Label(root2, text="Address", bg="bisque2", fg="black", font=("Helvetica", 16)).grid(row=0, column=2, padx=5,
                                                                                            pady=3)

        Label(root2, text="Phone number 1", bg="bisque2", fg="black", font=("Helvetica", 16)).grid(row=0, column=3,
                                                                                                   padx=5, pady=3)
        Label(root2, text="Adhar Card ", bg="bisque2", fg="black", font=("Helvetica", 16)).grid(row=0, column=4,
                                                                                                padx=5, pady=3)
        Label(root2, text="Date of birth", bg="bisque2", fg="black", font=("Helvetica", 16)).grid(row=0, column=5,
                                                                                                  padx=5, pady=3)
        Label(root2, text="Birthmark", bg="bisque2", fg="black", font=("Helvetica", 16)).grid(row=0, column=6, padx=5,
                                                                                              pady=3)
        Label(root2, text="Death Place.", bg="bisque2", fg="black", font=("Helvetica", 16)).grid(row=0, column=7,
                                                                                                 padx=5, pady=3)
        Label(root2, text="Date of Death", bg="bisque2", fg="black", font=("Helvetica", 16)).grid(row=0, column=8,
                                                                                                  padx=5, pady=3)

        displaylabel_name.grid(row=1, column=1, padx=5, pady=5)
        displaylabel_address.grid(row=1, column=2, padx=5, pady=5)
        displaylabel_phone1.grid(row=1, column=3, padx=5, pady=5)
        displaylabel_adhar.grid(row=1, column=4, padx=5, pady=5)
        displaylabel_dob.grid(row=1, column=5, padx=5, pady=5)
        displaylabel_birthmark.grid(row=1, column=6, padx=5, pady=5)
        displaylabel_deathplace.grid(row=1, column=7, padx=5, pady=5)
        displaylabel_dateofdeath.grid(row=1, column=8, padx=5, pady=5)

        root2.mainloop()

        con.commit()
        con.close()

    #######################################################################################################################

    window = Tk()
    window.title("Death Information")
    window.geometry("1500x1000")
    window.config(bg="snow")
    frame1 = Frame(window)
    frame1.pack()
    heading_label = Label(frame1, text="Death Information Portal", bg="snow", fg="black", font=("Helvetica", 50),
                          relief="raised")
    name_label = Label(frame1, text="FULL NAME", bg="snow", fg="black", font=("Helvetica", 16))
    address_label = Label(frame1, text="ADDRESS", bg="snow", fg="black", font=("Helvetica", 16))
    phone1_label = Label(frame1, text="PHONE NUMBER", bg="snow", fg="black", font=("Helvetica", 16))
    birthmrk_label = Label(frame1, text="BIRTH MARK", bg="snow", fg="black", font=("Helvetica", 16))
    dob_label = Label(frame1, text="DATE OF BIRTH", bg="snow", fg="black", font=("Helvetica", 16))
    adhar_label = Label(frame1, text="ADHAR CARD NUMBER", bg="snow", fg="black", font=("Helvetica", 16))
    deathplace_label = Label(frame1, text="DEATH PLACE", bg="snow", fg="black", font=("Helvetica", 16))
    date_label = Label(frame1, text="DATE OF DEATH", bg="snow", fg="black", font=("Helvetica", 16))
    enterbutton = Button(frame1, text="ENTER", bg="green", fg="black", font=("Helvetica", 16), command=submit)
    showdatabutton = Button(frame1, text="SHOW DATA", bg="yellow", fg="black", font=("Helvetica", 16), command=showdata)

    input_name = StringVar()
    entry_name = Entry(frame1, textvariable=input_name)

    input_address = StringVar()
    entry_address = Entry(frame1, textvariable=input_address)

    input_phone1 = StringVar()
    entry_phone1 = Entry(frame1, textvariable=input_phone1)

    input_adhar = StringVar()
    entry_adhar = Entry(frame1, textvariable=input_adhar)

    input_dob = StringVar()
    entry_dob = Entry(frame1, textvariable=input_dob)

    input_birthmark = StringVar()
    entry_birthmark = Entry(frame1, textvariable=input_birthmark)

    input_deathplace = StringVar()
    entry_deathplace = Entry(frame1, textvariable=input_deathplace)

    input_dateofdeath = StringVar()
    entry_dateofdeath = Entry(frame1, textvariable=input_dateofdeath)

    heading_label.grid(row=0, column=0, padx=0, pady=5, ipadx=5, ipady=5, columnspan=2)
    name_label.grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5)
    entry_name.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5)
    address_label.grid(row=2, column=0, padx=5, pady=5, ipadx=5, ipady=5)
    entry_address.grid(row=2, column=1, padx=5, pady=5, ipadx=5, ipady=5)
    phone1_label.grid(row=3, column=0, padx=5, pady=5, ipadx=5, ipady=5)
    entry_phone1.grid(row=3, column=1, padx=5, pady=5, ipadx=5, ipady=5)
    adhar_label.grid(row=4, column=0, padx=5, pady=5, ipadx=5, ipady=5)
    entry_adhar.grid(row=4, column=1, padx=5, pady=5, ipadx=5, ipady=5)
    dob_label.grid(row=5, column=0, padx=5, pady=5, ipadx=5, ipady=5)
    entry_dob.grid(row=5, column=1, padx=5, pady=5, ipadx=5, ipady=5)
    birthmrk_label.grid(row=7, column=0, padx=5, pady=5, ipadx=5, ipady=5)
    entry_birthmark.grid(row=7, column=1, padx=5, pady=5, ipadx=5, ipady=5)
    deathplace_label.grid(row=9, column=0, padx=5, pady=5, ipadx=5, ipady=5)
    entry_deathplace.grid(row=9, column=1, padx=5, pady=5, ipadx=5, ipady=5)
    date_label.grid(row=10, column=0, padx=5, pady=5, ipadx=5, ipady=5)
    entry_dateofdeath.grid(row=10, column=1, padx=5, pady=5, ipadx=5, ipady=5)
    enterbutton.grid(row=11, columnspan=5, column=0, padx=5, pady=5, ipadx=5, ipady=5)
    showdatabutton.grid(row=11, columnspan=2, column=1, padx=5, pady=5, ipadx=5, ipady=5)
    btn = Button(window, text="close window", bg="red", font=("Helvetica", 16), relief="sunken",
                 command=window.destroy).pack()
    # To save the file automatically
    con.commit()
    con.close()
    window.mainloop()

front()
