import main_menu
import stu_details
def STU_MENU( ):
    while True:
        print("*********************************************************************************")
        print("*                                     SCHOOL MANAGEMENT SYSTEM                                       *")
        print("*********************************************************************************")
        print("**-----------STUDENT DETAILS-----------**")
        print(" 1. Add student record :- ")
        print(" 2. Show student Details:- ")
        print(" 3. Append student Details :- ")
        print(" 4. Exit :- ")
        print("---------------------------------------")
        print(" ")
        a=int(input("Input your Choice:- "))
        if a==1:
            stu_details.add_records()
        elif a==2:
            stu_details.show_stu_details()
        elif a==3:
            stu_details.append_stu_details()
        elif a==4:
            return
        else:
            print("EROOR: Invalid choice ,try again...")
            conti="Press any key to return to main menu.."
        print(" -------------------------------------------------")
def add_records( ):
    try:
        import csv
        a=open("stud.csv","w")
        b=csv.writer(a)
        b.writerow(["Roll No.","Name","Class","DOB","Mobno"])
        ra=int(input("How many student records has to enter:-"))
        print(" ")
        for c in range (ra):
            roll=input("Enter roll no.:-")
            name=input("Enter name:-")
            clas=input("Enter class:-")
            dob=input("Enter dob:-")
            mobno=input("Enter mob no:-")
            g=[roll,name,clas,dob,mobno]
            b.writerow(g)
        print("data is successfuly uploaded")
    except:
        print("ERROR")
def show_stu_details( ):
    import csv
    fh=open("stud.csv","r",newline='\r\n')
    creader=csv.reader(fh)
    for rec in creader:
        print(rec)
    fh.close()
def append_stu_details():
    import csv
    a=open("stud.csv","a")
    b=csv.writer(a)
    ra=int(input("How many student records have to append:-"))
    print(" ")
    for c in range (ra):
        roll=int(input("Enter roll no.:-"))
        name=input("Enter name:-")
        clas=int(input("Enter class:-"))
        dob=input("Enter dob:-")
        mobno=int(input("Enter mob no:-"))
        g=[roll,name,clas,dob,mobno]
        b.writerow(g)
    print("data is successfuly uploaded")
    print("Press 2 for view appending records")
