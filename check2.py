import os
os.system("clear")
def check(entry,file1,file2):
    num1=(entry+"\n")
    found=False
    ref1=open(file1,"r")
    for line in ref1:
        #line.replace("\n","")
        if num1==line:
            print("Entry found in file1")
            return(found==True)
            break
    ref2=open(file2,"r")
    for line in ref2:
        if num1==line:
            print("Entry found in file2")
            return(found==True)
            break
    if found==False:
        print("Entry not found")
check(input("what is the address"),"/storage/sdcard0/Download/business.txt","/storage/sdcard0/Download/house.txt")