

#Parent Class Technicians
class Technicians:
    name = "Jess"
    email = "jess@gmail.com"
    password = "1234abcd"

    def getRegistrationInfo(self):
        reg_name = input("Enter your name: ")
        reg_email = input("Enter your email: ")
        reg_password = input("Enter your password: ")
        if (reg_email == self.email and reg_password == self.password):
            print("{}, you already have an account. Please log in.".format(reg_name))
        else:
            print("Thank you for signing up!")
    
                

#Child Class Phlebotomists
class Phlebotomist(Technicians):
    base_pay = 15.00
    department = "Lab"
    lab_number = "6590"

    def getRegistrationInfo(self):
        reg_name = input("Enter your name: ")
        reg_email = input("Enter your email: ")
        reg_lab_number = input("Enter your lab number: ")
        if (reg_name == self.name and reg_lab_number == self.lab_number):
            print("Welcome back, {}!".format(reg_name))
        else:
            print("The lab number is incorrect.")

#Another Child Class Histologists
class Histologist(Technicians):
    base_pay = 16.50
    department = "Pathology"
    pathology_id = "7784"

    def getRegistrationInfo(self):
        reg_name = input("Enter your name: ")
        reg_email = input("Enter your email: ")
        reg_path_id = input("Enter your pathology ID: ")
        if (reg_name == self.name and reg_path_number == self.pathology_id):
            print("Welcome back, {}!".format(reg_name))
        else:
            print("The pathology ID is incorrect.")


employee = Technicians()
employee.getRegistrationInfo()

phleb = Phlebotomist()
phleb.getRegistrationInfo()

histo = Histologist()
histo.getRegistrationInfo()
