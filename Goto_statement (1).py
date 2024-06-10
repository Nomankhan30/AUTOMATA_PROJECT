import re 
import time
import os
d=["word","numb"] #valid data types

def low(s):
    if s=='numb' or s=='word':
        return False
    else:
        w=s.lower()
        return w

def goto_exp(s):
  pattern = r'^(numb|word)\s+([a-zA-Z_][a-zA-Z0-9_]*\s*(,\s*[a-zA-Z_][a-zA-Z0-9_]*)*)\s*(=\s*[-+]?[0-9]*\.?[0-9]+|=\s*[\'"]?[a-zA-Z_][a-zA-Z0-9_]*[\'"]?)?(\s*,\s*[a-zA-Z_][a-zA-Z0-9_]*\s*(=\s*[-+]?[0-9]*\.?[0-9]+|=\s*[\'"]?[a-zA-Z_][a-zA-Z0-9_]*[\'"]?)?)*}$'


  return re.match(pattern,s) is not None

def valid(inp):
 rw=(goto_exp(inp))
 #covering null body case
 z=inp[:-1]
 if inp[-1]=="}" and all(x==" " for x in z):
          return True 
 


 p = r'\bnumb word|numb numb|word word|word numb\b'
 m=re.search(p,inp)

 if rw and not m: # covering word word or numb numb case
      for a in inp:
         if low(a) and a in d: #wOrd numb
           return False
          
      return True
  
 
 else:
    #a=2 or a="h"
    #only variable initialization 
    pat2=r'^[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*(-?\d+(\.\d+)?|\'[^\']*\'|\"[^\"]*\")(\s*,\s*[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*(-?\d+(\.\d+)?|\'[^\']*\'|\"[^\"]*\"))*}$'

    q=re.match(pat2,inp)
    if q:
      return True
    

 return False



def goto(str):
  a=len(str)
  if "{" in str and a>1 :
    s=str.split("{")
    sub1=s[0]
    sub2=s[1]
    sub1=(sub1 +"{")
   
    pat1= r'goto\((?:(numb|word)\s+)?([a-zA-Z_]\w*)\s*=\s*([^;]+)\s*;\s*([^;]+)\s*;\s*([a-zA-Z_]\w*\s*=\s*(?:(?:[a-zA-Z_]\w*|\d+)\s*[\+\-\*/]\s*(?:[a-zA-Z_]\w*|\d+))|(?:[a-zA-Z_]\w*|\d+))\)\s*;?{'

    if re.search(r'\b(?:word|numb)\s*=', str): #covering word=0 or numb=10
        print("Invalid Goto Statement\n")
        return
    res1=re.match(pat1,sub1)
    res2=valid(sub2)
    if res1 and res2:
      print("Valid Goto Statement\n")
      return 
    else:
      print("invalid Goto Statement\n")
      return
    
  else:
    print("Invalid Goto Statement\n")
    return
  

def time_delay():
    time.sleep(5)
    # clear the screen
    if os.name == 'nt':         # for windows
        os.system('cls')
    else:                       # for mac and linux
        os.system('clear')


def main():
    while (1):
        time_delay()
        print("1. Press 1 to check goto Statement")
        print("2. Press 2 to exit\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            inp = input("Enter Your goto Statement: ")
            goto(inp)
        elif choice == 2:
            break
        else:
            print("invalid choice")


main()





 