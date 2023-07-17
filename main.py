class car_rent:
    def __init__(self):  # constraint
        self.total_car = 20  # total car in go dam
        self.__db = {}  # data store of person

    def bill_print(self,*data):
        printing_bill = f'''
        welcome to car rental
        cus_name = {data[0]}
        aadhar no = {data[1]}
        no of car = {data[2]}
        no of days = {data[3]}
        total bill = {data[4]}
         Thank you '''
        file_name = data[1]+".txt"
        p = open(file_name, "w")
        p.write(printing_bill)
        p.close()

    # method
    def rented_sys(self):  # peron pick up the car
        no_car = int(input("enter your req car :"))
        if no_car <= car.total_car:
            no_day = int(input("How many day : "))
            cus_name = input("Enter your name :")
            aadhar_no = input("Enter your aadhar no :")
            bill = no_day*no_car*500
            print("your bill : ",bill)
            conferm = input("Are you conferm y/n :")
            if conferm == "y":
                print("Car Successfully booked")
                self.__db[aadhar_no] = [cus_name, no_car, no_day, bill]
                self.bill_print(cus_name, aadhar_no, no_car, no_day, bill)
                self.total_car = self.total_car - no_car
            else:
                print("Thank you for visiting")

        else:
            print("not available")


    def deposit_sys(self):  # person depositing car
        adhar_no = input("Enter your aadhar no :")
        if adhar_no in self.__db:
            dpt_car = int(input("how many car u sumit :"))
            if dpt_car < self.__db[adhar_no][1]:
                self.__db[adhar_no][1] = self.__db[adhar_no][1] - dpt_car
                self.total_car = self.total_car + dpt_car
            elif dpt_car == self.__db[adhar_no][1]:
                del self.__db[adhar_no]
                self.total_car = self.total_car + dpt_car
            elif dpt_car > self.__db[adhar_no][1]:
                print("Wrong Input")
        else:
            print("aadhar no not exit")

    def show_database(self):
        print(self.__db)

car = car_rent()  # object
print("Welcome to Car Agency")
while True:  # to show the car details and rental
    print("Total No of Car :", car.total_car)
    option = input('''
    1. car on rent 
    2. car deposit
    3. exit : ''')
    if option =="1":
        if car.total_car > 0 :
             print("1 Car for 1 Day at rupee 500/-")
             conferm = input("conferm y/n :")
             if conferm == "y":
                 car.rented_sys()
             else:
                 print("Thank You")
    elif option == "2":
        car.deposit_sys()
    elif option == "3":
        print("Thank You")
        break
    else:
        print("Wrong input")
    car.show_database()

