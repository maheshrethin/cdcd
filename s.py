# hospital management system
# hospital details to show in list,tuple,set,dict
# list
departments = ["Cardiology", "Neurology", "Orthopedics", "Pediatrics", "Oncology"]
print("Departments:", departments)
floor_no_for_department = (
    "Cardiology= 1",
    "Neurology= 2",
    "Orthopedics= 3",
    "Pediatrics= 4",
    "Oncology= 5")
# tuple
print("Floor numbers for each department:", floor_no_for_department)
# dict
doctors_available_for_each_dept={
    "Pediatrics": ["Dr. Davis", "Dr. Garcia"],
    "Neurology": ["Dr. Williams", "Dr. Brown"],
    "Cardiology": ["Dr. Smith", "Dr. Johnson"],
    "Orthopedics": ["Dr. Jones", "Dr. Lee"],
    "Oncology": ["Dr. Patel", "Dr. Kim"]
    
}
print("Doctors available for each department:", doctors_available_for_each_dept)

# function for patient details plus if else for doctor name based on department
def patient_details(name, age, gender, department, doctor):
    if department== "Cardiology":
       print("doctor=Dr. Smith")
    elif department== "Neurology":
       print("doctor=Dr. Williams")
    elif department== "Orthopedics":
       print("doctor=Dr. Jones")
    elif department== "Pediatrics":
       print("doctor=Dr. Davis")
    elif department== "Oncology":
       print("doctor=Dr. Patel")
patient_details("John Doe", 45, "Male", "Cardiology", "Dr. Smith")
patient_details("Bob Johnson", 60, "Male", "Neurology", "Dr. Williams")
patient_details("Charlie Brown", 35, "Male", "Orthopedics", "Dr. Jones")
patient_details("Eve Garcia", 5, "Female", "Pediatrics", "Dr. Davis")   
patient_details("Frank Lee", 50, "Male", "Oncology", "Dr. Patel")   

# set
patients_in_each_dept = {
    "Cardiology": {"John Doe"},
    "Neurology": {"Bob Johnson"},
    "Orthopedics": {"Charlie Brown"},
    "Pediatrics": {"Eve Garcia"},
    "Oncology": {"Frank Lee"}
}
print("Patients in each department:", patients_in_each_dept)

# to show room booked patients in for loop
for patients in patients_in_each_dept:
    print(f"Patients in {patients} department: {patients_in_each_dept[patients]}")  
    
# to register the room of the patient in while loop

room=1
while room<=5:
    amount=int(input("Enter the amount "))
    if amount>=200:
         print("Seat Booked @",room)
    else:
        print("Unable to book seat")
        

# billing in constructor
class Billing:
    def patient1(self):
        print("Patient Name: John Doe")
        print("Treatment: Heart Surgery")
        print('bill per day is$1000')
        print('no of days stayed is 5')
        print("Total Bill: $5000")
class Billing2(Billing):
    def patient2(self):
        print("Patient Name: Bob Johnson")
        print("Treatment: Brain Surgery")
        print('bill per day is$1500')
        print('no of days stayed is 7')
        print("Total Bill: $10500")

class Billing3(Billing2):
    def patient3(self):
        print("Patient Name: Charlie Brown")
        print("Treatment: Bone Fracture Surgery")
        print('bill per day is$800')
        print('no of days stayed is 3')
        print("Total Bill: $2400")
h=Billing3()
h.patient1()
h.patient2()
h.patient3()


# rooms type 
# abstraction
from abc import ABC
class room(ABC):
    def firstclass (self):
        print("Luxury windows withn beach nature view, tv, ac, fridge, sofa, bed")
class secondclass(room):
    def secondclass(self):
        print("tv+ac")
class thirdclass(room):
    def thirdclass(self):
        print("only tv")
A=room()
A.firstclass()                
l=secondclass()
l.secondclass()
c=thirdclass()
c.thirdclass()

# # crud operation

doctors_available_for_each_dept = {
    "Cardiology": ["Dr. Smith", "Dr. Johnson"],
    "Neurology": ["Dr. Williams", "Dr. Brown"],
    "Orthopedics": ["Dr. Jones", "Dr. Lee"],
    "Pediatrics": ["Dr. Davis", "Dr. Garcia"],
    "Oncology": ["Dr. Patel", "Dr. Kim"]
    }

# create
doctors_available_for_each_dept["Dermatology"] = ["Dr. Adams", "Dr. Baker"]
# read
print("Doctors available for each department:", doctors_available_for_each_dept)
# update
doctors_available_for_each_dept.update({"Cardiology": ["Dr. Smith", "Dr. Johnson", "Dr. Thompson"]})
print("Updated doctors available for Cardiology:", doctors_available_for_each_dept["Cardiology"])
# delete
del doctors_available_for_each_dept["Oncology"]
print("Doctors available for each department after deleting Oncology:", doctors_available_for_each_dept)

# check in check out using geter and setter for doctors using shift timings
class Doctor:
    def __init__(self, name, department):
        self.__name = ''
        self.__department = ''
        self.__shift_timings = ''
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_department(self, department):
        self.__department = department
    def get_department(self):
        return self.__department
    def set_shift_timings(self, shift_timings):
        self.__shift_timings = shift_timings
    def get_shift_timings(self):
        return self.__shift_timings
m=Doctor("Dr. Smith", "Cardiology")
m.set_name("Dr. Smith")
m.set_department("Cardiology")
m.set_shift_timings("9 AM - 5 PM")
print('doctors name:', m.get_name())
print('department:', m.get_department())
print('shift timings:', m.get_shift_timings())

# polymorphisim overloading
class room:
    def Add(self,a):
        print(a)
    def Add(self,a,b):
        print(a+b)
    def Add(self,a,b,c):
        print(a+b+c)
s=room()
s.Add(10,20,30)



# error handling for lab reports 
# # name error handling for vaccine name
Vaccine_Name='Pfizer'
print(Vaccine_Name)
try:
    # error handling for lab reports
    Vaccine_Name=input("Enter the Name")
    print(Vaccine_Namee)
    
except NameError as e:
    print(e)
    Vaccine_Name=input("Enter the Name")
    print(Vaccine_Name)
    print("vaccine   not found") 

# file handling for nurses details
print("nurses details")
nurses_details = open("nurses_details.txt", "w")
nurses_details.write("Nurse Name: Sarah Johnson\n")
nurses_details.write("Shift: Morning\n")
nurses_details.write("Nurse Name: Emily Davis\n")
nurses_details.write("Shift: Evening\n")
print(nurses_details.writable())
print(nurses_details.readable())
print(nurses_details.mode)
nurses_details.write("Nurse Name: Olivia Brown\n")
nurses_details.write("Shift: Night\n")
print('appended new nurse details')
nurses_details.close()


















