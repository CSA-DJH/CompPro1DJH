#Daniel herbowy
print("n", '\t', "2**n")   #makes table headings
print("---", '\t', "-----")
num1 = input("what is your number?")  #asks for input
num1=int(num1)      #ints input
for x in range(0, num1):   #makes a for loop
    print(x, '\t', 2**x)


