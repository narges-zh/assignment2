import random

user_score=0
c1_score=0
c2_score=0
counter=0
r=1

print('welcome to the game***')
while(counter<5):
    c1_choose=random.randint(1,2)
    c2_choose=random.randint(1,2)
    print('''please choose:
    1.palam
    2.plich''')

    user_choose=int(input('please choose_'))
    counter+=1

    if(c1_choose==c2_choose==1 and user_choose==2 or c1_choose==c2_choose==2 and user_choose==1):
        user_score+=1
        print('ure winner' , round)
        print('user score:' , user_score)
        print('computer1 score:' , c1_score)
        print('computer2 score:' , c2_score)

    elif(c1_choose==user_choose==1 and c2_choose==2 or c1_choose==user_choose==2 and c2_choose==1 ):
        c2_score+=1
        print('computer 2 is winner' , round)
        print('user score:' , user_score)
        print('computer1 score:' , c1_score)
        print('computer2 score:' , c2_score)

    elif(c2_choose==user_choose==1 and c1_choose==2 or c2_choose==user_choose==2 and c1_choose==1 ):
        c1_score+=1
        print('computer 1 is winner' , round)
        print('user score:' , user_score)
        print('computer1 score:' , c1_score)
        print('computer2 score:' , c2_score)
         
    elif(c1_choose==c2_choose==user_choose):
        print('bazi barabar shod:' , round)
        print('user score:' , user_score)
        print('computer1 score:' , c1_score)
        print('computer2 score:' , c2_score)
        break

    else:
        if(c1_score>user_score and c1_score>c2_score):
            print('computer 1 is winner')
        elif(c2_score>user_score and c2_score>c1_score):
            print('computer 2 is winner')
        elif(user_score>c1_score and user_score>c2_score):
            print('user is winner') 
        else:
            print('nobody is winner')       







