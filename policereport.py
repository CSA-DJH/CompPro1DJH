#Daniel Herbowy
import string, time, os
criminals=[''] 
def menu():
    os.system('clear')
    print('--------------------')
    print('''Press 1 to enter the criminal's name and offence
press 2 to see how many people made an offence
press 3 to see how many people committed crimes
press 4 to quit
--------------------''')       #asks what to do
    num1=input('Entry: ')
    if num1=='1':
        entry()                #if 1 runs entry
    elif num1=='2':          #if 2 runs crimecount
        crimecount() 
    elif num1=='3':        #if three prints the criminals
        print(criminals)
        time.sleep(5)
        menu()
    elif num1=='4':        #if four quits
        quit() 
    else:
        print('Invalid entry')  #if anything else is entered it runs the menu again
        time.sleep(2)
        menu()

def entry():
    os.system('clear')
    global criminals 
    name=input("criminal's name (please insert full name) ")    #asks for a name
    name=name.title()    #titles the name
    criminals.append(name)   #adds it to the empty list
    off=input("what is the criminal's offence ")    #asks for the offence
    criminals.append(", ")    #adds a , to the list
    criminals.append(off)     #adds the offence to the list
    print(''.join(criminals))  
    criminals.append("; ")   #adds a ; to the list
    menu() 
def crimecount(): 
    os.system('clear')
    global criminals 
    num4=input('What offence do you want to count? ')    #asks for an offence to count
    num5=criminals.count(num4)    #counts the number of a certain offence
    if num5==0:   #if it doesnt find anything, prints no one made that offence
        print('no one has made that offence')
    else:
        print('The total number of offences %s is %i' %(num4,num5))  #if it find something, adds how many and name to a print
        time.sleep(5) 
    menu() 
    

menu() 