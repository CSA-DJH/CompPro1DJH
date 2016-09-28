#Daniel Herbowy
def print_triangular_numbers(n):   #makes a function
    print("n", '\t', "result")      #makes a table
    print("---", '\t', "------")    #makes a table
    x = 1    #makes x 1
    while x <= n:  #while statement
        equation = x * (x + 1) / 2   #makes the equation a variable
        print (x,'\t', equation)     #makes the numbers into a table
        x += 1
        
x=input('Enter a number')
x=int(x)                             #asks for an input
print_triangular_numbers(x)   #runs the function
