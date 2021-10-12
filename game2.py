import random
from typing import Counter

user=0
computer=0
Counter=0

print('welcome to the game')

while(Counter<5):

  computer=random.randint(1 , 3)

  print('''1-sang
  2-kaghaz:
  3-gheichi:
  4-exit''')

  user=int(input('please choose'))
  Counter += 1

  if(user==computer):
    print('barabar')

  if(user==1 and computer==3 or user==2 and computer==1 or user==3 and computer==2):
    print('yore winner')
    user+=1

  if(computer==1 and user==3 or computer==2 and user==1 or computer==3 and user==2):
    print('youre loser')
    computer+=1

  if(computer==4):
    print('exit')
    break

  else:
       print('barande nahaii:')
  if(Counter==5):
   
   if(user>computer):
       print('tabrik**shoma barande shodid')

   elif(user<computer):
       print('motasefane shoma bazande hastid')
   
   elif(user==computer):
       print('bazi barabar shod')
       break




