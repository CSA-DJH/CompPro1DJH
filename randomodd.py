import random, os, time
os.system("clear")
y=0
for i in range(100):
    x=random.randrange(0,1001)   #for loop that runs 100 times amking 100 numbers between 0 and 1000
    if x%2==1:      #checks if the number odd
        print(x)
        time.sleep(.05)
        y+=x        #adds the odd number to the list
os.system("clear")
time.sleep(1)
print(y,'Is the total sum of one-hundred random odd numbers between zero and one-thousand.') #prints the total number of odds
