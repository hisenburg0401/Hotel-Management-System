#program for taking input
import os
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
#read()
