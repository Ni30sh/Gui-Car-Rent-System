from tkinter import *
from tkinter import messagebox
class car_rent_system:
    def __init__(self):
        self.Total_cars = 100

    def car_on_rent(self):
        var = messagebox.askyesno("Notification", "Cars in Agency :" + str(self.Total_cars)+ " \nTo confirm Y/N....",)
        if var == True:
            car1 = Tk()
            car1.title("Costumer Portal")
            car1.config(bg="red")
            car1.geometry("500x300")
            label2 = Label(car1, text="Your Name", font=("times", 14, "bold"))
            label2.place(x=15, y=60, height=30, width=140)
            label3 = Label(car1, text="Your Aadhar ", font=("times", 14, "bold"))
            label3.place(x=15,y=100,height=30,width=140)
            label4 = Label(car1, text="Required Car ", font=("times", 14, "bold"))
            label4.place(x=15,y=145,height=30,width=140)
            label5 = Label(car1, text="How Many Days ", font=("times", 14, "bold"))
            label5.place(x=15,y=188,height=30,width=140)

            entry1 =  Entry(car1,font=("chillers",15, "bold"))
            entry1.place(x=200,y=60,height=30,width=250)








            # Label(car1,text="To Continue.......").place(x=5,y=90,height=40,width=190)
             # Button(car1,text="Yes",font=("times",11,"bold"),bg="blue",fg="white",
            # activebackground="white",activeforeground="black",).place(x=20,y=190,height=30,width=60,)
            # Button(car1,text="No",font=("times",11,"bold"),bg="blue",fg="white",
            # activebackground="white",activeforeground="black",).place(x=190,y=190,height=30,width=60,)
            car1.mainloop()
    def car_deposit(self):
       pass
    def potal_exite(self):
        pass





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


