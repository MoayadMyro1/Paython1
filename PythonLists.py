import random

def eightball():
 answers = [ "It is certain", "It is decidedly so", "Without a \
 doubt", "Yes, definitely", "You may rely on it", "As I see it, \
 yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
 "Reply hazy try again", "Ask again later", "Better not tell you \
 now", "Cannot predict now", "Concentrate and ask again", "Don ' t \
 count on it", "My reply is no", "My sources say no", "Outlook \
 not so good", "Very doubtful" ]
 print("Wellcom to our programme please ask or type quite or 0 to end the programme :")
 while True:
  nswr = random.choice(answers)
  input_user = input()
  if(input_user == "quite" or input_user == "0"):
   print("you choice quite thanks for useing our programme and goodbye.")
   break
  else:
   print("Your answer is : " + nswr)
   print("Ask again or type quite to end the programme :")
   
def FIFO():
 processes = []
 print("Wellcom to our programme please ask or press Enter to end the programme :")
 while True:
  input_user = input()
  if(input_user == ""):
   print("You end the prograame thanks for useing our programme and goodbye.")
   break
  elif(input_user == "?"):
   msg = "Empty fifo add a new values"
   if( len(processes) > 0):
    msg = processes[0]
   print("Your FIFO is : " + msg)
  else:
   processes.insert(0,input_user)
   print("Value added succsufully")

def Fibonacci():
   n1, n2 = 0, 1
   msg =""
   for x in range(9):
    msg+=str(n1)+" "
    nth = n1 + n2
    n1 = n2
    n2 = nth
   return print(msg)

def counting_number(strng):
 rslt = ""
 zz = 1
 print(str(len(strng)))
 for char in strng:
  for x in range(zz,len(strng)):
   if(char != strng[x]):
    rslt += char
    break
  zz+=1
 print(str(len(rslt))) # 2
 print(rslt) # 2

def main():
 #eightball()
 #FIFO()
 #Fibonacci()
 counting_number("hghjh")

if __name__ == "__main__":
    main()
