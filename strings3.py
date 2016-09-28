#daniel herbowy
import os
os.system('clear')
def count(p):   #makes a function
    lowerc = "abcdefghijklmnopqrstuvwxyz"    #defines all the lower case letters
    upperc =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"   #defines all the upper case letter

    num1 = 0
    num2 = 0
    for num3 in p:           
        if num3 in lowerc or num3 in upperc:      
            num2 = num2 + 1
            if num3 == 'a':                        #counts how many letters of the one letter
                num1 = num1 + 1

    percent_with_a = (num1 / num2) * 100   #makes a percentage 
    print("Your text contains", num2, "alphabetic characters of which", num1, "(", percent_with_a, "%)", "are 'a'.")  #prints the result


p = '''
Using the sources from the MLA Documentation Exercise, I want you to discuss a theme in poetry in a 5 paragraph essay. You can match your quotes with three poems, or use the quotes to discuss three examples from a single poem.
'''
                           #sentance to check
count(p)
