#daniel Herbowy
import os
os.system("clear")
print("---------------------------------------------")

def doubleStuff(a_list):
    """ Return a new list in which contains doubles of the elements in a_list. """
    new = []                    #empty list
    for value in a_list:       #for loop
        new_elem = 2 * value    #multiplies the list
        new.append(new_elem)    #appends the new list to the emtpy list
    return new

things = [1, 2, 3, 4, 5]        #list to change
print(things)
things = doubleStuff(things)     #makes the doubled list
print(things)
print("---------------------------------------------")

def num1():
    y=[1,3,5,[7,9],'j',[4,5,99999],11]
    print(y[5][2])     #prints 99999
    
num1()
print("---------------------------------------------")

def num2():
    z="Hi I am the coolest person ever"
    x=z.split()  #splits the sentence up into a lsit
    print(x)
    
num2()
print("---------------------------------------------")
def num3():
    a=['','John, ', 'Jane, ', 'Jimmy, ', 'Jenny, ']
    num4=("Hi my name is ")
    print(num4.join(a))    #adds hi my name is before each name
    
num3()
print("---------------------------------------------")