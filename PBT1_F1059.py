import csv
import os

class clinic:
    def __init__(self): #constructor
        print("****CLINIC SYSTEM MANAGEMENT****")
        print("1.Add Patient")
        print("2.Display Patient")
        print("3.Exit")
                        
    def add_patient(self): 
        
        with open('dataclinic.csv','a',newline='')as csvfile: #tambah data patient
            write = csv.writer(csvfile)

            try:
                #input type
                name = input("\nInput Name:")
                age = int(input("Input Age:"))
                noic = int(input("Input No Ic:"))
                noreg = input("Input No Registration:")
                medicalhistory = input("Medical History:")
                date = input("Date:")
                
                write.writerow([name,age,noic,noreg,medicalhistory]) #masukkan data in csv
                
            except ValueError: #exception handling
                print("\nPlease input the correct value")

    def search_patient(self):
        
        with open('dataclinic.csv','r') as file: #display data patient from csv
            reader = csv.reader(file)
            for DATA in reader: 
                print(DATA)
                
obj = clinic()

if not os.path.exists("dataclinic.csv"):#check file jika xde write,jika ada xperlu write 
    with open('dataclinic.csv','w',newline='')as csvfile:
        write = csv.writer(csvfile)
        ROW = (['Name','Age','No Ic','No Registration','Medical History'])
        write.writerow(ROW)

while True:
    try:
        choice = int(input("input a number:")) #input pilihan add / display data patient
        match choice:
            case 1:
                obj.add_patient() #calling function
        
            case 2:
                obj.search_patient() #calling function
                
            case 3:
                print("\nThank you for using the system. Exiting now...")
                break
            case _:
                print("\nINVALID INPUT! Please input the correct value")
    except ValueError: #exception handling
        print("\nError!! Please Try Again")
        break

    try:            
        sambung = input("\ndo you want to continue? (yes/no) : ").lower()
        print("\n")
        if sambung == 'yes':
            continue
        elif sambung == 'no':
            print("Thank you for using the system. Exiting now...")
            break
    except ValueError: #exception handling
            print("\nError!! Please Try Again")
            break
        

        

        

        
        
            

    
