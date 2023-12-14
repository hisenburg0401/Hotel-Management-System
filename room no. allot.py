#program for alloting room no
def roomno():
    r = open("hotel.txt","r")
    rec=[]
    roop=["IS EMPTY","IS EMPTY","IS EMPTY","IS EMPTY","IS EMPTY"]
    s=r.readlines()
    while True:
        rc=input("ENTER THE ROOM CATEGORY:- ")
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

            
            







            
            


