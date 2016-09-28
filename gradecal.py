#daniel HErbowy
import os
os.system("clear")
def main():
    grades=[]          #makes an empty lsit
    name=input("what is your name?")
    print("hello "+name+"!")    #prints greeting
    num1=input("how many classes did you take? between 1 and 8")    #asks for how many classes and ints it
    num1=int(num1)
    
    for k in range(0, num1):      #for loop that runs as many times as the entered number of classes
        num2=input("is your grade for that class?")
        grades.append(num2)       #appends the grades to the empty list
        
    grades=[int(i) for i in grades]    #ints the entire list
    num3=sum(grades)   #adds the grades together
    num4=(num3/num1)      #gets the avarage
    num5=((num4/20)-1)    #equation for the gpa
    num5=str(num5)    
    print("your GPA is "+num5)     #prints the gpa
    
main()
    
    
    