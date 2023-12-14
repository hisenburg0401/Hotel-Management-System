import os
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
