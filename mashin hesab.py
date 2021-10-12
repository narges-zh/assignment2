import math

while True:
  #a=int(input('enter a:'))
  #b=int(input('enter b:'))

  #print("welcome to sajjad:")
  #print("+ sum")
  #print("- sub")
  #print("* mul")
  #print("/ dev")
  #print("exit")

  op=input('''welcome :
 + sum:
  - sub:
  * mul:
 / dev:
 sin:
 cos:
 tg:
 cot:
 log:
 exit ''')

  if op=='+':
     a=int(input('enter a:'))
     b=int(input('enter b:'))
     result = a+b 
     print(result)

  elif op=='-':
     a=int(input('enter a:'))
     b=int(input('enter b:'))
     result = a-b
     print(result)

  elif op=='*':
     a=int(input('enter a:'))
     b=int(input('enter b:'))
     result = a*b
     print(result)

  elif op=='/':
    a=int(input('enter a:'))
    b=int(input('enter b:'))
    if b!=0:
     result = a/b
    else:
      result='this is wrong'
      print(result)

  elif op=='sin':
      a=int(input('enter a:'))
      math.radians=a/360*2*math.pi
      result=math.sin(math.radians)
      print(result)

  elif op=='cos':
      a=int(input('enter a:'))
      math.radians=a/360*2*math.pi
      result=math.cos(math.radians)
      print(result)

  elif op=='tg':
      a=int(input('enter a:'))
      math.radians=a/360*2*math.pi
      result=math.tan(math.radians)
      print(result)

  elif op=='cot':
      a=int(input('enter a:'))
      math.radians=a/360*2*math.pi
      result=math.atan(math.radians)
      print(result)

  elif op=='log':
      a=int(input('enter a:'))
      result=math.log(a)
      print(result)

  elif op=='exit':
    break 
   