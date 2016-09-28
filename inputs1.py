import os
os.system('clear')

def inputs1():
    num1=input("what number?")   #asks for the first number
    num2=input("what is the second number?")   #asks for the second number
    num1=int(num1)     #integers the two numbers
    num2=int(num2)
    print(num1)    #prints the two numbers
    print(num2)
    if num1>num2:                                #checks if the first number is higher
        print("the first number is higher")    
        
    if num2>num1:                                #checks if the second number is higher
        print("the second number is higher")
        
    if num1==num2:                                #checks if the numbers are equal
        print("the numbers are equal")
        
inputs1()