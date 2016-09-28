infile = open("/storage/sdcard0/Download/classroster.txt", "r")
outfile = open("/storage/sdcard0/Download/sorted.txt", "w")


aline = infile.readlines()
aline[-1]=aline[-1]+('\n')
aline.sort()
for line in aline:
    outfile.write(line)
    
infile.close()
outfile.close()
