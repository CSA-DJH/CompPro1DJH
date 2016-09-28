#daniel herbowy
import os, random
os.system('clear')


def house():  #makes a function
    num1=input("what is your name?")  #asks for a name
    x=num1.title()  #capitalizes the make
    print("hi"+x)  #prints a greeting
    num2=input("what price do you want to pay for the house in between 100 and 500? in the thousands")  #asks for a price
    num2=int(num2) #ints num2
    while num2>500:  #ckecks if the input is greater than 500
        print("enter a number under 500")
        num2=input("what price do you want to pay for the house in between 100 and 500? in the thousands")
        num2=int(num2)
    while num2<100:   #checks if the number is under 100
        print("enter a number above 100")
        num2=input("what price do you want to pay for the house in between 100 and 500? in the thousands")
        num2=int(num2)
        
    
        
    num3=random.randrange(100, 500)   #makes a random price
    num4=0
    while num3!=(num2):   #if the input doesnt match with the random price, runs again
        num3=random.randrange(100, 500)
        print(num3)
        num4+=1   #counts how many times it ran
        
    num4=str(num4)
    print("it will take "+ num4 +" days to find")   #prints how long it will take
        
   
house()  #runs the function
