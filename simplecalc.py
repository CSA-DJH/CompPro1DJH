import os
os.system("clear")

outfile = open("/storage/sdcard0/Download/solutions1.txt", "w")

num1=input("how many times would you like to add?")
num1=int(num1)

for i in range(num1):
    num2=input("what is the first number?")
    num3=input("what is the second number?")
    num2=int(num2)
    num3=int(num3)
    num4=(num2+num3)
    num4=str(num4)
    outfile.write(num4 + '\n')
    os.system("clear")
   
    
    


outfile.close()
