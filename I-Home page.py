import main_menu
import admission
import stu_details
import fee_details
import lib_lab
while True:
    #Main Menus:-
    print("*********************************************************************************")
    print("*                                     SCHOOL MANAGEMENT SYSTEM                  *")
    print("*********************************************************************************")
    print("*                                        STAR PUBLIC SCHOOL                     *")
    print("*                  --*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*")
    print("*                                     MUKHERJI NAGAR,NEW DELHI                      *")
    print("*                  --*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*")
    print("*********************************************************************************")
    print(" ")
    print("=> Choose your desired option :-")
    print("1. About School -")
    print("2. Admission -")
    print("3. Student Details -")
    print("4. Fees Details -")
    print("5. Library and Lab -")
    print("6. About Hostel -")
    print("7. Exit -")
    print("----------------------------------------------------------------------------------------------")
    print(" ")
    choice=int(input("Enter Your Choice :-"))
    if choice==1:
        about=open("about.txt","r")
        r=about.read()
        print(r)
        about.close()
    if choice==2:
        admission.ADM_MENU()
    if choice==3:
        stu_details.STU_MENU()
    if choice==4:
        fee_details.FEE_DETAILS()
    if choice==5:
        lib_lab.Lib_Lab()
    if choice==6:
        ah=open("hostel.txt","r")
        h=ah.read()
        print(h)
        ah.close()
    if choice==7:
        break
    else:
        print("EROOR: Invalid choice ,try again...")
        conti="Press any key to return to main menu.."
    
    

