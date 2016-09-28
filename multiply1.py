#daniel HErbowy
#multiplying txt


import os
os.system("clear")
print("multiplyed values")
fileref=open('/storage/sdcard0/Download/multiply.txt','r')
for aline in fileref:
    val=aline.split()
    if len(val)<2:
        fileref.close()
        quit()
    else:
        val=aline.split()
        num1=int(val[0]) 
        num2=int(val[1])
        print(num1*num2)
        
fileref.close()   


