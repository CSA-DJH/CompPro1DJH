#daniel Hebowy
import os
os.system('clear')
def slice():
  slicelist=['a','b','c','d','e','f','g']   #defines the letters
  print(slicelist[2])      #prints the third letter
  print(slicelist[ :4])    #prints the first 4 letters

  slicelist[-1]='z'     #replaces last letter
  slicelist[-2]='y'     #replaces f 
  slicelist[-3]='x'      #replaces 3
  print(slicelist)    #prints the new one
  
slice()