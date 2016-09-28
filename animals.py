
fileref=open('/storage/sdcard0/Download/animalplace.txt','r')


import os
os.system("clear")

for aline in fileref:
    val=aline.split()
    if len(val)==5:
        print("%s lives in %s."%(val[0],val[3]))
    elif len(val)==6:
        print("%s lives in %s %s."%(val[0],val[3],val[4]))
fileref.close()



