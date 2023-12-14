import os
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
