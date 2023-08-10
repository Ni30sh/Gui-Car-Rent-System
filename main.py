import time
from tkinter import *
from tkinter import messagebox
import mysql.connector
class car_rent_system:
    def __init__(self):
        self.Total_cars = 100
    def car_on_rent(self):
        var = messagebox.askyesno("Notification", "Cars in Agency :" + str(self.Total_cars) + " \n To confirm Yes/No....",)
        if var == True:
            def data_sumit():
                global conn, cur
                NAME_val = name_var.get()
                AADHAR_val = AADHAR_var.get()
                CARS_val = cars_var.get()
                DAYS_val = days_var.get()
                DATE_val = time.strftime("%d-%m-%Y")

                # Check if AADHAR_val is a valid integer before inserting into the database
                if AADHAR_val.isdigit():
                    # Convert AADHAR_val to an integer before inserting
                    AADHAR_val = int(AADHAR_val)
                else:
                    messagebox.showerror("Error",
                                         "Invalid AADHAR_var value. Please enter a valid integer value for AADHAR_var.")
                    return  # Stop further execution if AADHAR is invalid

                cur = conn.cursor()
                use_database = "USE CarRentalSystem"
                cur.execute(use_database)

                cur.execute(
                    "INSERT INTO AgencyDetails (CUSTOMER_NAME, Aadhar_no, CAR, NO_OF_DAYS, DATE) VALUES (%s, %s, %s, %s, %s)",
                    (NAME_val, AADHAR_val, CARS_val, DAYS_val, DATE_val))
                conn.commit()
                messagebox.showinfo("Bill",
                                    f"Name: {NAME_val}\nAADHAR: {AADHAR_val}\nNo of Cars: {CARS_val}\nNo of Days: {DAYS_val}\nDate: {DATE_val}")


            car1 = Tk()
            car1.title("Costumer Portal")
            car1.config(bg="sky blue")
            car1.geometry("500x300")

            label2 = Label(car1, text="Your Name", font=("times", 15, "bold"),anchor="w",bg="red")
            label2.place(x=15, y=60, height=30, width=150)
            Frame(car1,bg="black").place(x=15,y=89,height=2,width=100)
            label3 = Label(car1, text="Your Aadhar ", font=("times", 14, "bold"),anchor="w")
            label3.place(x=15,y=100,height=30,width=150)
            Frame(car1, bg="black").place(x=15, y=120, height=2, width=100)
            label4 = Label(car1, text="Required Car ", font=("times", 14, "bold"),anchor="w")
            label4.place(x=15,y=145,height=30,width=150)
            Frame(car1, bg="black").place(x=15, y=169, height=2, width=100)
            label5 = Label(car1, text="How Many Days ", font=("times", 14, "bold"),anchor="w")
            label5.place(x=15,y=188,height=30,width=150)
            Frame(car1, bg="black").place(x=15, y=190, height=2, width=100)

            name_var = StringVar()
            AADHAR_var = StringVar()  # Changed the name from AADHAR to AADHAR as a StringVar
            cars_var = StringVar()
            days_var = StringVar()

            entry1 = Entry(car1, textvariable=name_var ,font=("chillers", 15, "bold"))
            entry1.place(x=200, y=60, height=30, width=250)
            entry2 = Entry(car1, textvariable=AADHAR_var, font=("chillers", 15, "bold"))
            entry2.place(x=200, y=100, height=30, width=250)
            entry3 = Entry(car1, textvariable=cars_var, font=("chillers", 15, "bold"))
            entry3.place(x=200, y=145, height=30, width=250)
            entry4 = Entry(car1, textvariable=days_var, font=("chillers", 15, "bold"))
            entry4.place(x=200, y=188, height=30, width=250)

            button = Button(car1, text="Sumit", font=("times", 20, "bold"), bg="blue", fg="white",
                            activebackground="white", activeforeground="black", command=data_sumit)
            button.place(x=180, y=240, height=40, width=140)
            car1.mainloop()

        else:
            rt = messagebox.askyesno("Notification", "Do you want to exit?")
            if rt == True:
                car.destroy()
    def car_deposit(self):
       pass
    def potal_exite(self):
        pass

def data_base():
    global  cur, conn
    host = "localhost"
    user ="root"
    password = "123@Never#settle"
    try:
        conn = mysql.connector.connect(
           host=host,
           user=user,
           password=password)
        cur = conn.cursor()
        var = "CREATE DATABASE IF NOT EXISTS CarRentalSystem"
        cur.execute(var)
        var1 = "USE CarRentalSystem"
        cur.execute(var1)
        var2 = """CREATE TABLE AgencyDetails (
                     CUSTOMER_NAME VARCHAR(255),
                     `Aadhar_no` BIGINT,  
                     CAR int(11), 
                     NO_OF_DAYS int(11),
                     `DATE` VARCHAR(255) )"""
        cur.execute(var2)
        conn.close()
        messagebox.showinfo("Database", "Successfully connected")
    except:
        strin = "USE CarRentalSystem"
        cur.execute(strin)
        messagebox.showinfo("Notification", "NOW YOU ARE CONNECTED TO THE DATABASE")


car = Tk()
car.title("Car Agency")
car.geometry("500x500+400+120")

label1 = Label(car,text="Car Rent Agency ",font=("times",25,"bold"))
label1.place(x=10,y=17,height=40,width=480)

car_rent = car_rent_system()  #  create an intence of  the  car_ent_system class

button1 = Button(car, text="RENT",font=("times",20,"bold"),bg="blue",fg="white",activebackground="white",activeforeground="black",
                command = car_rent.car_on_rent)
button1.place(x=160,y=100,height=80,width=180)
button2 = Button(car, text="Deposit",font=("times",20,"bold"),bg="blue",fg="white",activebackground="white",activeforeground="black",
                 command=car_rent.car_deposit )
button2.place(x=160,y=210,height=80,width=180)
button3 = Button(car, text="Exit",font=("times",20,"bold"),bg="blue",fg="white",activebackground="white",activeforeground="black",
                 command=car_rent.potal_exite)
button3.place(x=160,y=330,height=80,width=180)

data_base()
car.mainloop()


