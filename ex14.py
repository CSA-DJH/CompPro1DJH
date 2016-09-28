import os
os.system("clear")
def main():
    old = ("john")
    new = ("Johnny")
    string1 = ("john is a great guy. john is so much fun. Really, I like john. Yay Johnny!")
    num1=string1.replace(old, new)  #replaces john with jonny
    print(string1)
    print("-----------------------------------------------------------------------------------------")
    print(num1)
    
main()