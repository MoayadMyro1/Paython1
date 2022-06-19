import random
#print("Wellcom to python")
def multiplicationtable(pars):
    for  x  in range(1,11):
        print(f"{x} x {pars} = "+ str( x*pars))
multiplicationtable(12)


def commoncharacters(msg1,msg2):
    set1=set(msg1)
    set2=set(msg2)
    set3=(set1&set2)
    msg=''.join(set3)
    return msg

v = random.randint(1,10)
def Guessingnumber():
  msg = ""
  print(str(v))
  g = int(input())
  if(v < g):
       msg = "Too big"
  elif(v > g):
       msg = "Too small"
  else:
       msg = "You are SUPER"
  return msg

def main():
 print(commoncharacters("beE","peEr"))
 print(Guessingnumber())
if __name__ == "__main__":
    main()