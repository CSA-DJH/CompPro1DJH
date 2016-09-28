infile = open("/storage/sdcard0/Download/animals.txt", "r")
outfile = open("/storage/sdcard0/Download/animalhome.txt", "w")

aline = infile.readline()
while aline:
    items = aline.split()
    dataline = items[0] + ',' + items[4]
    outfile.write(dataline + '\n')
    aline = infile.readline()
    

infile.close()
outfile.close()
