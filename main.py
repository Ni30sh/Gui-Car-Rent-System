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

            def data_sumit(*args):
                global  conn, cur
                NAME_val = name.get()
                AADHAR_val = aadhar.get()       
                CARS_val = cars.get()
                DAYS_val = days.get()
                DATE_val = time.strftime("%d-%m-%Y")
                use_database = "USE CarRentalSystem"
                cur.execute(use_database)
                cur = conn.cursor()
                # var1 = "INSERT INTO AgencyDetails VALUES (%s,%s,%s,%s,%s)"
                # var2 = (NAME_val, AADHAR_val, CARS_val,DAYS_val, DATE_val )
                cur.execute("INSERT INTO AgencyDetails VALUES (%s,%s,%s,%s,%s)",(NAME_val, AADHAR_val, CARS_val, DAYS_val, DATE_val))
                conn.commit()
                messagebox.showinfo("Bill",
                                    f"Name : {NAME_val} \n Aadhar : {AADHAR_val} \n No of Cars : {CARS_val}"
                                    f" \n No of Days : {DAYS_val} \n date : {DATE_val}")
                # def bill_printing(self, *data):
                # print_bill = f"""
                #     customer Name = {NAME_val}
                #     aadhar = {AADHAR_val}
                #     cars = {CARS_val}
                #     days = {DAYS_val}"""
                # file_name = AADHAR_val + ".txt"
                # p = open(file_name, "w")
                # p.write(print_bill)
                # p.close()
                # print_bill()

            car1 = Tk()
            car1.title("Costumer Portal")
            car1.config(bg="red")
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

            name = StringVar()
            aadhar = StringVar()
            cars = StringVar()
            days = StringVar()

            entry1 = Entry(car1,textvariable=name,font=("chillers",15, "bold"))
            entry1.place(x=200,y=60,height=30,width=250)
            entry2 = Entry(car1,textvariable=aadhar,font=("chillers",15, "bold"))
            entry2.place(x=200,y=100,height=30,width=250)
            entry3 = Entry(car1,textvariable=cars,font=("chillers",15, "bold"))
            entry3.place(x=200,y=145,height=30,width=250)
            entry4 = Entry(car1,textvariable=days,font=("chillers",15, "bold"))
            entry4.place(x=200,y=188,height=30,width=250)

            button = Button(car1,text="Sumit",font=("times",20,"bold"),bg="blue",fg="white",
                            activebackground="white",activeforeground="black", command=data_sumit)
            button.place(x=180,y=240,height=40,width=140)
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
        var2 = """CREATE TABLE IF NOT EXISTS AgencyDetails (
                     CUSTOMER_NAME VARCHAR(255), 
                     AADHAR BIGINT, 
                     CAR VARCHAR(255), 
                     NO_OF_DAYS VARCHAR(255),
                     DATE VARCHAR(255) )"""
        cur.execute(var2)
        conn.commit()
        messagebox.showinfo("Database", "Successfully connected")
    except:
        strin = "USE CarRentalSystem"
        cur.execute(strin)
        messagebox.showinfo("Notification", "NOW YOU ARE CONNECTED TO THE DATABASE")

data_base()

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

car.mainloop()


