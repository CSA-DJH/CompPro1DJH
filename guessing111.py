import random, os
os.system('clear')
def main():
    
    def compare():
            
        numguess1=guess()        
        totalroll1=diceroll()
        if numguess1==totalroll1:          
            print("YAY YOU WIN!!!")      #checks if number is right
        elif (numguess1>totalroll1):
            print("Your guess was too high")     #checks if number is to high
        elif (numguess1<totalroll1):
            print("Your guess was too low.")   #checks if number is to low

    def guess():
        guess=input("What is your guess? ")    #asks for a guess
        intguess=int(guess)    #ints the guess
        return intguess       
    def diceroll(): 
        roll1=random.randrange(1,11)    #makes a random number
        total=roll1
        print(total)
        return total
            
            
    def greeting(): 
        print("Hello!")
        name=input("Whats your name? ") #asks for a name
        return name
    def names():
        
        player1=greeting()
        print("Hello "+player1)     #prints a greeting
    names()
    compare()
main()