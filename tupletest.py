import os
os.system("clear")
def main(num1, num2):
    print("PART E")
    num0=[]
    print("---------------------------------------")
    print(num1)
    print(num2)
    print("unsorted numbers^")
    print("---------------------------------------")
    num1.sort()   #sorts the numbers
    num2.sort()   
    print(num1)
    print(num2)
    print("sorted numbers^")
    print("---------------------------------------")
    num0.append(num1)  #adds the numbers to the empty list
    num0.append(num2)
    num0.sort()  #sorts the list
    print(num0)
    print("merged list^")
    print("---------------------------------------")
    
    
main([2, 4, 1, 3, 5], [9, 8, 10, 7, 6])  #deffines the numbers for the variables
    
print("PART C")    
print("---------------------------------------")
def num33(tuple1):
    print(tuple1)
    print("unsorted tuples^")
    print("---------------------------------------")
    output = sorted(tuple1, key=lambda x: x[-1])  #sorts the tuples
    print(output)
num33([(5, 3), (8, 1), (4, 5, 7), (8, 2)])
print("sorted tuples^")
print("---------------------------------------")