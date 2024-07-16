u=int(input('enter 0 for rock,1 for paper,2 for scissor:'))
if(u==0):
    print('✊->rock')
elif(u==1):
    print('🫱->paper')
else:
    print('✌️->scissor')
import random
c=random.randint(0,2)
print('computer choice ='+ ' ' + str(c))
if(c==0):
    print('✊->rock')
elif(c==1):
    print('🫱->paper')
else:
    print('✌️->scissor')
if(u==0 and c==0):
    print("it's a draw")
elif(u==0 and c==1):
    print('you lose')
elif(u==0 and c==2):
    print('you win')
elif(u==1 and c==0):
    print('you win')
elif(u==1 and c==1):
    print("it's a draw")
elif(u==1 and c==2):
    print('you lose')
elif(u==2 and c==0):
    print('you lose')
elif(u==2 and c==1):
    print("you win")
elif(u==2 and c==2):
    print("it's a draw")
