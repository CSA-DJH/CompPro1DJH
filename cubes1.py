import os, time
os.system('clear')
def cubes(n):
    print("n", '\t', "result")   #prints the result
    print("---", '\t', "------")
    x = 1
    while x <= n: 
        equation = x**3       #runs the equation as many times as asked
        print (x,'\t', equation)
        x += 1

def check():
    x=int(input('Enter a number between 1-100'))
    if x>100:
        print("Please enter a number lower than 100.")   #asks for a num beteen 1 and 100 and checks if lower than 101
        time.sleep(2)
        check()
    else:
        cubes(x)    #runs the first function with the variable x
check()
