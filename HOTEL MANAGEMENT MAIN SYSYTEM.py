# THIS IS THE MAIN SCREEN
import os
while True:
    print("\t\t................................................")
    print("\t\t*********Welcome to PARAMOUNT Hotel*****************")
    print("\t\t................................................")
    print("\t\t          PARAMOUNT HOTEL WELCOMES YOU          ")
    print("\t\t------------------------------------------------")
    print("")
    print("\t\t 1. MENU ")
    print("\t\t 2. NEW CUSTOMER REGISTRATION")
    print("\t\t 3. UPDATE CUSTOMER REGISTERED")
    print("\t\t 4. DELETE CUSTOMER REGISTERED")
    print("\t\t 5. ROOM NO. ALLOTER")
    print("\t\t 6. BILL CALUCATION")
    print("\t\t 7. EXIT")
    print("")
    print("\t\t------------------------------------------------")
    ch=int(input("\t\t--> ENTER THE CHOICE= "))
    print("\t\t------------------------------------------------")
    
    if ch==1:
        #PROGRAM FOR SHOWING THE MAIN MENU
        def menu():
            print("")
            print("\t\t............................................")
            print("\t\t****WELCOME TO HOTEL MANAGEMENT SYSYTEM****")
            print("\t\t............................................")
            print("\t\t         PARAMOUNT HOTEL WELCOMES YOU          ")
            print("")
            print("")
            print("\t*********************MAIN MENU*************************")
            print("\t     ROOM TYPE    	           COST(1 NIGHT STAY)")
            print("\t*******************************************************")
            print("\t 1 BED (NON AC)\t\t \tRs.1000/-(+500/-PER NIGHT)")
            print("\t (FOOD CHARGES EXCLUSIVE)")
            print("\t 1 BED (AC)\t\t \tRs.1300/-(+600/-PER NIGHT)")
            print("\t (FOOD CHARGES EXCLUSIVE)")	
            print("\t 1 BED (LUXURY)\t\t \tRs.2000/-(+800/-PER NIGHT)")
            print("\t (FOOD CHARGES INCLUSIVE)")
            print("\t 1 BED (DELUXE)\t\t \tRs.2500/-(+1000/-PER NIGHT)")
            print("\t (FOOD CHARGES + CLOTH WASHING INCLUSIVE)")
            print("\t ********************************************************")
            print("\t 2 BED (NON AC)\t\t \tRs.1200/-(+600/-PER NIGHT)")
            print("\t (FOOD CHARGES EXCLUSIVE)")
            print("\t 2 BED (AC)\t\t \tRs.1500/-(+750/-PER NIGHT)")
            print("\t (FOOD CHARGES EXCLUSIVE)")
            print("\t 2 BED (LUXURY)\t\t \tRs.2500/-(+1000/-PER NIGHT)")
            print("\t (FOOD CHARGES INCLUSIVE)")
            print("\t 2 BED (DELUXE)\t\t \tRs.3000/-(+1500/-PER NIGHT)")
            print("\t (FOOD CHARGES + CLOTH WASHING INCLUSIVE)")
            print("\t ********************************************************")
            print("\t 3 BED (NON AC)\t\t \tRs.1800/-(+1000/-PER NIGHT)")
            print("\t 3 BED (AC)\t\t \tRs.2500/-(+1500/-PER NIGHT)")
            print("\t ********************************************************")
            print("\t ADDITIONAL Rs.500 FOR THE FOOD CHARGES (IF INCLUDED)")
            print("\t ********************************************************")
        menu()
        
    elif ch==2:
        #PROGRAM FOR NEW CUSTOMER REGISTRATION
        print("\t\t:::::ENTER THE DETAILS OF THE CUSTOMER:::::")
        print("\t\t------------------------------------------------")
        def NEW_REGISTRATION():
            while True:
                f=open("hotel.txt","a",newline='')
                N=input("\t\t-->ENTER THE NAME= ")
                while True:
                    PN=int(input("\t\t-->ENTER THE PHONE NUMBER= "))
                    if len(str(PN))==10:
                        NP=int(input("\t\t-->ENTER THE NUMBER OF PEOPLE= "))
                        while True:
                            RCAT=input("\t\t-->ENTER THE ROOM CATEGORY= ")
                            if RCAT in ("1BDNA,1BA,1BD,1BL,2BDNA,2BA,2BD,2BL,3BDNA,3BA"):
                                DSTAY=int(input("\t\t-->ENTER THE DAYS OF STAY= "))
                                if RCAT in ("1BD,1BL,2BD,2BL"):
                                    def roomno():
                                        r = open("hotel.txt","r")
                                        rc=RCAT
                                        rec=[]
                                        roop=["IS EMPTY","IS EMPTY","IS EMPTY","IS EMPTY","IS EMPTY"]
                                        s=r.readlines()
                                        print("\t\t ROOM CATEGORY  \t\t ROOM NO.")
                                        for line in s:
                                            rec=line.split(",")
                                            for i in range(1,6):
                                                if int(rec[3])==i and rc==str(rec[4]):
                                                    roop[i-1]="IS OCCUPIED"
                                        r.close()
                                        for i in range(0,5):
                                            print("\t\t   ",rc," \t\t\t",i+1,"\t\t",roop[i])
                                    roomno()
                                    RNO=int(input("\t\t-->ENTER THE ROOM NUMBER= "))
                                    CIN=input("\t\t-->ENTER THE CHECK-IN TIME= ")
                                    COUT=input("\t\t-->ENTER THE CHECK-OUT TIME= ")
                                    r=N +","+str(PN) +","+str(NP)+","+str(RNO)+","+RCAT+","+str(DSTAY)+","+"N"+","+CIN+","+COUT+"\n"
                                else:
                                    FC=input("\t\t-->ENTER THE FOOD CHARGES (Y/N)= ")
                                    def roomno():
                                        r = open("hotel.txt","r")
                                        rc=RCAT
                                        rec=[]
                                        roop=["IS EMPTY","IS EMPTY","IS EMPTY","IS EMPTY","IS EMPTY"]
                                        s=r.readlines()
                                        print("\t\t ROOM CATEGORY  \t\t ROOM NO.")
                                        for line in s:
                                            rec=line.split(",")
                                            for i in range(1,6):
                                                if int(rec[3])==i and rc==str(rec[4]):
                                                    roop[i-1]="IS OCCUPIED"
                                        r.close()
                                        for i in range(0,5):
                                            print("\t\t   ",rc," \t\t\t",i+1,"\t\t",roop[i])
                                    roomno()
                                    RNO=int(input("\t\t-->ENTER THE ROOM NUMBER= "))
                                    CIN=input("\t\t-->ENTER THE CHECK-IN TIME= ")
                                    COUT=input("\t\t-->ENTER THE CHECK-OUT TIME= ")
                                    r=N +","+str(PN) +","+str(NP)+","+str(RNO)+","+RCAT+","+str(DSTAY)+","+FC+","+CIN+","+COUT+"\n"
                                f.write(r)
                                break                 
                            else:
                                print("\t\t   !!!!ROOM CATEGORY NOT VALID!!!!")
                                continue
                        break
                    else:
                        print("\t\t   !!!!PHONE NO. NOT VALID!!!!")
                        continue
                ch=input("\t\t-->MORE RECORDS? (Y/N)")
                if ch=='n' or ch=='N':
                    break
                else:
                    continue
            
            f.close()
            f=open("hotel.txt","r")
            k=open("temp.txt","w")
            t=f.readlines()
            for line in t:
                k.write(line)
            f.close()
            k.close()
            os.remove("hotel.txt")
            os.rename("temp.txt","hotel.txt")
        NEW_REGISTRATION()
        print("\t\t------------------------------------------------")
    
    elif ch==3:
        #PROGRAM FOR UPDATING SOMEONES INFORMATION
        r = open("hotel.txt","r")
        w = open("temp.txt","w")
        print("\t\t------------------------------------------")
        print("\t\t*********** DATA TO BE UPDATED ***********")
        print("\t\t------------------------------------------")
        print("\t\t-->1.NAME")
        print("\t\t-->2.NO OF PEOPLE CHECKING IN")
        print("\t\t-->3.ROOM NUMBER")
        print("\t\t-->4.ROOM CATEGORY")
        print("\t\t-->5.DAYS OF STAY")
        print("\t\t-->6.FOOD CHARGES INCLUDED(Y/N)")
        print("\t\t-->7.CHECK IN TIME")
        print("\t\t-->8.CHECK OUT TIME")
        print("\t\t-->9.PHONE NUMBER")
        print("\t\t-->10.ALL FIELDS")
        print("\t\t-------------------------------------------")
        while True:
            phno=int(input("\t\t-->ENTER THE PHONE NO. TO SEARCH :- "))
            if len(str(phno))==10:
                s=r.readlines()
                for line in s:
                    L=line.split(",")
                    while int(L[1])==phno:
                        k=int(input("\t\t-->ENTER THE ENTRY TO BE UPDATED= "))
                        if k==1:
                            name=input("\t\t-->ENTER THE NAME:- ")
                            w.write(name +","+ str(phno) +","+ str(L[2]) +","+ str(L[3]) +","+ L[4] +","+str(L[5])+","+ L[6] +","+ L[7] +","+ L[8])
                            print("\t\t!! ENTRY UPDATED SUCCESSFULLY!!")
                        elif k==2:
                            nop=int(input("\t\t-->NO. OF PEOPLE CHECKING IN:- "))
                            w.write(L[0] +","+ str(phno) +","+ str(nop) +","+ str(L[3]) +","+ L[4] +","+str(L[5])+","+ L[6] +","+ L[7] +","+ L[8])
                            print("\t\t!! ENTRY UPDATED SUCCESSFULLY!!")
                        elif k==3:
                            rn=int(input("\t\t-->ROOM NUMBER:- "))
                            w.write(L[0] +","+ str(phno) +","+ str(L[2]) +","+ str(rn) +","+ L[4] +","+str(L[5])+","+ L[6] +","+ L[7] +","+ L[8])
                            print("\t\t!! ENTRY UPDATED SUCCESSFULLY!!")
                        elif k==4:
                            rc=input("\t\t-->ROOM CATEGORY:- ")
                            w.write(L[0] +","+ str(phno) +","+ str(L[2]) +","+ str(L[3]) +","+ str(rc) +","+str(L[5])+","+ L[6] +","+ L[7] +","+ L[8])
                            print("\t\t!! ENTRY UPDATED SUCCESSFULLY!!")
                        elif k==5:
                            dos=int(input("\t\t-->NUMBER OF DAYS OF STAY: "))
                            w.write(L[0] +","+ str(phno) +","+ str(L[2]) +","+ str(L[3]) +","+ L[4] +","+str(dos)+","+ L[6] +","+ L[7] +","+ L[8])
                            print("\t\t!! ENTRY UPDATED SUCCESSFULLY!!")
                        elif k==6:
                            fc=input("\t\t-->FOOD CHAREGES(Y/N):- ")
                            w.write(L[0] +","+ str(phno) +","+ str(L[2]) +","+ str(L[3]) +","+ L[4] +","+str(L[5])+","+ fc +","+ L[7] +","+ L[8])
                            print("\t\t!! ENTRY UPDATED SUCCESSFULLY!!")
                        elif k==7:
                            cit=str(input("\t\t-->CHECK IN TIME:- "))
                            w.write(L[0] +","+ str(phno) +","+ str(L[2]) +","+ str(L[3]) +","+ L[4] +","+str(L[5])+","+ L[6] +","+ cit +","+ L[8])
                            print("\t\t!! ENTRY UPDATED SUCCESSFULLY!!")
                        elif k==8:
                            cout=str(input("\t\t-->CHECK OUT TIME:- "))
                            w.write(L[0] +","+ str(phno) +","+ str(L[2]) +","+ str(L[3]) +","+ L[4] +","+str(L[5])+","+ L[6] +","+ L[7] +","+ cout)
                            print("\t\t!! ENTRY UPDATED SUCCESSFULLY!!")
                        elif k==9:
                            ph=int(input("\t\t-->ENTER THE NEW PHONE NUMBER:- "))
                            w.write(L[0] +","+ str(ph) +","+ str(L[2]) +","+ str(L[3]) +","+ L[4] +","+str(L[5])+","+ L[6] +","+ L[7] +","+ L[8])
                            print("\t\t   !! ENTRY UPDATED SUCCESSFULLY !!")
                        elif k==10:
                            name=input("\t\t-->ENTER THE NAME:- ")
                            nop=int(input("\t\t-->NO. OF PEOPLE CHECKING IN:- "))
                            rc=input("\t\t-->ROOM CATEGORY:- ")
                            dos=int(input("\t\t-->DAYS OF STAY:- "))
                            fc=input("\t\t-->FOOD CHARGES(Y/N): ")
                            rn=int(input("\t\t-->ROOM NO. ALLOTED:- "))
                            cit=str(input("\t\t-->CHECK IN TIME:- "))
                            cout=str(input("\t\t-->CHECK OUT TIME:- "))
                            w.write(name +","+ str(phno) +","+ str(nop) +","+ str(rn) +","+ rc +","+str(dos)+","+ fc +","+ cit +","+ cout)
                            print("\t\t   !! ENTRY UPDATED SUCCESSFULLY !!")
                        else:
                            print("\t\t  !! ENTRY NOT VALID !!")
                            continue
                        break
                    else:
                        w.write(line)
                break
            else:
                print("\t\t  !! PHONE NOT VALID !!")
                continue
        w.close()
        r.close()
        os.remove("hotel.txt")
        os.rename("temp.txt","hotel.txt")
        print("\t\t------------------------------------------------")

    elif ch==4:
        #PROGRAM FOR DELETING SOMEONES INFORMATION
        def delete_data():
            r = open("hotel.txt","r")
            w = open("temp.txt","w")
            s=r.readlines()
            i=0
            while True:
                phno=int(input("\t\t-->ENTER THE PHONE NO. WHOSE RECORD IS TO BE DELETED:- "))
                if len(str(phno))==10:
                    for line in s:
                        rec=line.split(",")
                        if int(rec[1])==phno:
                            i=i+1
                            continue
                        else:
                            w.write(str(line))
                    break
                else:
                    print("\t\t !!!!!!!!!!PHONE NUMBER NOT VALID!!!!!!!!!!")
                    continue
            if i==0:
                print("\t\t ******NO SUCH RECORD EXISTS******")
            else:
                print("\t\t\t\t !!RECORD SUCCESSFULLY DELETED!!")
                
            w.close()
            r.close()
            os.remove("hotel.txt")
            os.rename("temp.txt","hotel.txt")
        delete_data()
        print("\t\t------------------------------------------------")
        
    elif ch==5:
                #PROGRAM FOR ALLOTING ROOM NO.
        def roomno():
            r = open("hotel.txt","r")
            rec=[]
            roop=["IS EMPTY","IS EMPTY","IS EMPTY","IS EMPTY","IS EMPTY"]
            s=r.readlines()
            while True:
                rc=input("\t\t-->ENTER THE ROOM CATEGORY:- ")
                if rc in ("1BDNA,1BA,1BD,1BL,2BDNA,2BA,2BD,2BL,3BDNA,3BA"):
                    print("\t\t ROOM CATEGORY  \t\t ROOM NO.")
                    for line in s:
                        rec=line.split(",")
                        for i in range(1,6):
                            if int(rec[3])==i and rc==str(rec[4]):
                                roop[i-1]="IS OCCUPIED"
                else:
                    print("\t\t   !!!!ROOM CATEGORY NOT VALID!!!!")
                    continue
                break
            r.close()
            for i in range(0,5):
                print("\t\t   ",rc," \t\t\t",i+1,"\t\t",roop[i])
        roomno()
        print("\t\t------------------------------------------------")
        
    elif ch==6:
        #PROGRAM FOR THE BILL CALCULATION
        def totalcost():
                r=open("Hotel.txt","r")
                s=r.readlines()
                i=0
                while i==0:
                        phno=int(input("\t\t-->ENTER THE PHONE NUMBER TO BE SEARCHED FOR:-"))
                        if len(str(phno))==10:
                                for line in s:
                                        L=line.split(",")
                                        if int(L[1])==phno:
                                                i=i+1
                                                n=L[4]
                                                z=L[0]
                                                m=L[6]
                                                if n=="1BNA":
                                                        a= 1000
                                                        i=int(L[5])
                                                        m=L[6]
                                                        h=500
                                                        if m=="y" or m=="Y":
                                                                f=500
                                                                k=1000+500*(i-1)+f
                                                        else:
                                                                k=1000+500*(i-1)
                                                elif n=="1BA":
                                                        a= 1300
                                                        i=int(L[5])
                                                        m=L[6]
                                                        h=600
                                                        if m=="y" or m=="Y":
                                                                f=500
                                                                k=1300+600*(i-1)+f
                                                        else:
                                                                k=1300+600*(i-1)
                                                elif n=="1BL":
                                                        a= 2000
                                                        i=int(L[5])
                                                        h=800
                                                        k=2000+800*(i-1)
                                                elif n=="1BD":
                                                        a= 2500
                                                        i=int(L[5])
                                                        h=1000
                                                        k=2500+1000*(i-1)
                                                elif n=="2BNA":
                                                        a= 1200
                                                        i=int(L[5])
                                                        m=L[6]
                                                        h=600
                                                        if m=="y" or m=="Y":
                                                                f=500
                                                                k=1200+600*(i-1)+f
                                                        else:
                                                                k=1200+600*(i-1)
                                                elif n=="2BA":
                                                        a= 1500
                                                        i=int(L[5])
                                                        m=L[6]
                                                        h=750
                                                        if m=="y" or m=="Y":
                                                                f=500
                                                                k=1500+750*(i-1)+f
                                                        else:
                                                                k=1500+750*(i-1)
                                                elif n=="2BL":
                                                        a= 2500
                                                        i=int(L[5])
                                                        h=1000
                                                        k=2500+1000*(i-1)
                                                elif n=="2BD":
                                                        a= 3000
                                                        i=int(L[5])
                                                        h=1500
                                                        k=3000+1500*(i-1)
                                                elif n=="3BNA":
                                                        a= 1800
                                                        i=int(L[5])
                                                        m=L[6]
                                                        h=1000
                                                        if m=="y" or m=="Y":
                                                                f=500
                                                                k=1800+1000*(i-1)+f
                                                        else:
                                                                k=1800+1000*(i-1)
                                                elif n=="3BA":
                                                        a= 2500
                                                        i=int(L[5])
                                                        m=L[6]
                                                        h=1500
                                                        if m=="y" or m=="Y":
                                                                f=500
                                                                k=2500+1500*(i-1)+f
                                                        else:
                                                                k=2500+1500*(i-1)
                                                else:
                                                        print("\t\t    Sorry no such category of rooms available.")
                                if i==0:
                                        print("\t\t    !! NO SUCH RECORD EXIST !!")
                                        continue
                                else:
                                        print("\t\t................................................")
                                        print("\t\t*********Welcome to BHAPT Hotel*****************")
                                        print("\t\t................................................")
                                        print("\t\t------------------------------------------------")
                                        print("\t\t             CUSTOMER BILL       ")
                                        print("\t\t\t -->Name= ",str(z))
                                        print("\t\t\t -->Phone No.= ",phno)
                                        print("\t\t\t -->DAYS OF STAY=",i)
                                        print("\t\t\t -->ROOM TYPE=", n)
                                        print("\t\t\t -->COST(1st NIGHT)= Rs.",a)
                                        print("\t\t\t -->COST(PER NIGHT)= Rs.",h)
                                        if m=="Y" or m=="y":
                                                print("\t\t\t -->(FOOD CHARGES INCLUDED)= Rs.",500)
                                        print("\t\t\t -->TOTAL COST= Rs.",k)
                                        print("\t\t------------------------------------------------")
                                        print("\t\t****************THANK YOU***********************")
                                        print("\t\t**************PLEASE VISIT AGAIN****************")
                        else:
                                print("\t\t     !! PHONE NUMBER NOT VALID !!")
                                continue
        totalcost()
        print("-----------------------------------------------------------------------------------------------")
        
    elif ch==7:
        print("\t\t**********THANK YOU PLEASE VISIT AGAIN**********")
        print("\t\t------------------------------------------------")
        break
    else:
        print("")
        print("")
        print("\t\t\t !!!!PLEASE ENTER A VALID CHOICE!!!!")
        print("")
        print("")
        continue




