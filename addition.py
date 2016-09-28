#daniel herbowy
#checking additions
import os
os.system("clear")
infile=open("/storage/sdcard0/Download/addition.txt", "r")
afile=infile.readlines()

for i in range(6):

    x=afile[i].split()   #splits lines
    
    num3=(x[0])
    num4=(x[1])  #gets the two numbers
    num3=int(num3)
    num4=int(num4)
    num5=(num3+num4)  #adds the two numbers
    
    num2=int(afile[i+6])   #gets the number two compare
 
    if num5==num2:   #compairs the two numbers
        print("correct!")
    else:
        print("not correct!")
infile.close()
