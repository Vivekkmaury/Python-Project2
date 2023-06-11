import main_menu
import fee_details
def FEE_DETAILS( ):
        print("*********************************************************************************")
        print("*                                     SCHOOL MANAGEMENT SYSTEM                                                  *")
        print("*********************************************************************************")
        print("**----------- FEE DETAILS -----------**")
        def fee_detail():
            print("     FEE-TYPE            AMOUNT       DURATION ")
            print("  ~ ~ ~ ~ ~ ~ ~ ~      ~ ~ ~ ~ ~ ~ ~    ~ ~ ~ ~ ~ ~ ~ ~")
            print("1.Admission Fee          Rs.10000/-          1 year    ")
            print("2.  Exam Fee                Rs.500/-            per exam  ")
            print("3.Monthly Fee             Rs.3500/-         per month ")
            print("4.Lab Fee(Phy+Chem) Rs.1000/-           1 year     ")
            print("5.Lab Fee(Bio)             Rs.800/-             1 year     ")
            print("4.Lab Fee(CS)              Rs.800/-             1 year     ")
            print("7.Sports Fee                 Rs.750/-             1 year     ")
            print("8.Other Fee                  Rs.1000/-           1 year     ")
            re=int(input("how many students fee  record have to enter:-"))
            for i in range(re):
                a=int(input("Enter Admission no"))
                b=input("Name :-")
                c=input("Class :-")
                d=int(input(" Admission fee:-"))
                e=int(input("Exam fee:-"))
                f=int(input("Monthly fee:-"))
                g=int(input("How many months fee :-"))
                h=int(input("Lab fee(choose your required lab):-"))
                i=int(input("Sports fee:-"))
                j=int(input("Other fee:-"))
                z=d+e+(f*g)+h+i+j
                print("The student of Admission no.",a,",",b,"Of class",c,"have total fee amount is",z)
        fee_detail()

            
