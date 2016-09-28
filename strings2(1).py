#daniel herbowy
import os
os.system("clear")

sentence1="Hi jimmy, how are you? "   

print(sentence1)  #prints sentence
def letters(s):
    letterremoval=input("What letter would you like to remove from the sentence? ")   #asks what letter to remove
    sWithoutletters = ""
    for eachChar in s:  #makes a for loop
        if eachChar not in letterremoval:   # makes a if statement
            sWithoutletters = sWithoutletters + eachChar  
    return sWithoutletters  #returns swithoutletter


print(letters("Hi jimmy, how are you? "))


