import main_menu
import admission
def ADM_MENU( ):
    while True:
        #admission menu:-
        print("*********************************************************************************")
        print("*                                     SCHOOL MANAGEMENT SYSTEM                                       *")
        print("*********************************************************************************")
        print("**-----------ADMISSION-----------**")
        print(" 1. Admission details :- ")
        print(" 2. Show Admission Details:- ")
        print(" 3. Update Admission Details :- ")
        print(" 4. Search student record :- ")
        print(" 5. Deletion of Records :- ")
        print(" 6. Return :- ")
        print("---------------------------------------")
        print(" ")
        a=int(input("Input your Choice:- "))
        if a==1:
            admission.admin_details()
        elif a==2:
            admission.show_admin_details()
        elif a==3:
            admission.update_admin_details()
        elif a==4:
            admission.search_admin_details()
        elif a==5:
            admission.delete_admin_details()
        elif a==6:
            return
        else:
            print("EROOR: Invalid choice ,try again...")
            conti="Press any key to return to main menu.."
def admin_details( ):
    try:
            import pickle
            stu={}
            stufile=open("stu.dat","wb")
            ans="y"
            while ans=="y":
                admno=int(input("Admission no:-"))
                name=input("Name")
                clas=int(input("Class:-"))
                fn=input("Fathers name:-")
                mn=input("Mothers name:-")
                dob=input("Date of birth:-")
                add=input("Address:-")
                mobno=int(input("Mobile no. :-"))
                stu["Admission no"]=admno
                stu["Name"]=name
                stu["Class"]=clas
                stu["Fathers name"]=fn
                stu["Mothers name"]=mn
                stu["Date of birth"]=dob
                stu["Address"]=add
                stu["Mobile number"]=mobno
                pickle.dump(stu,stufile)
                ans=input("wants to enter more records?(y/n):-")
            stufile.close()
    except:
        print("ERROR")
def show_admin_details( ):
        import pickle
        emp={}
        empfile=open("stu.dat","rb")
        try:
            while True:
                emp=pickle.load(empfile)
                print(emp)
        except:
            empfile.close()
def update_admin_details( ):
        import pickle
        stu={}
        f=False
        upd=open("stu.dat","rb+")
        try:
            while True:
                r=upd.tell()
                stu=pickle.load(upd)
                y=int(input("admisssion no"))
                z=input("name")
                za=input("Class")
                if stu["Admission no"]==y:
                    stu["Name"]=z
                    upd.seek(r)
                    pickle.dump(stu,upd)
                    stu["Class"]
                    upd.seek(r)
                    pickle.dump(stu,upd)
                    f=True
        except:
            if f==False:
                print("sorry,no matching record file found.")
            else:
                print("Record successfuly updated")
            upd.close()
def search_admin_details( ):
    import pickle
    stu={}
    f=False
    fin=open("stu.dat","rb")
    a=int(input("enter admission no.:-"))
    sk=[a]
    try:
        while True:
            stu=pickle.load(fin)
            if stu["Admission no"] in sk:
                print(stu)
                f=True
    except:
        if f==False:
            print("No such records found in the file")
        else:
            print("search successful.")
        fin.close()
def delete_admin_details( ):
    import pickle as p
    import os
    f=False
    f1=open("stu.dat","rb")
    f2=open("temp.dat","wb")
    adm=int(input("enter admission no."))
    while True:
        try:
            d=p.load(f1)
            if adm==d["Admission no"]:
                f=True
            else:
                p.dump(d,f2)
        except:
            break
    if f==False:
        print("record not found!!")
    else:
        print("record found and deleted")
    f1.close()
    f2.close()
    import pickle
    emp={}
    empfile=open("temp.dat","rb")
    try:
        while True:
            emp=pickle.load(empfile)
            print(emp)
    except:
        empfile.close()

                
                
                
