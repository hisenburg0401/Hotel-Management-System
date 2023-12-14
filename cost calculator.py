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
