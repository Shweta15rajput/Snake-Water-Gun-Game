import random


"""
1 for snake
-1 for water
0 for gun

"""

Computer= random.choice([-1,0,1])

YouStr=input('Enter your choice: ').lower()
YourDict={'s':1, 'w':-1, 'g':0}
ReverseDict={1:'snake',-1:'water',0:'gun'}

You=YourDict[YouStr]

print(f'You chose {ReverseDict[You]}')
print (f'Computer chose {ReverseDict[Computer]}')

#Game Logic

if Computer==You:
     print('Its a draw')
else:  
    if('Computer==-1 and You==1'):
     print('You Win')
    
    elif('Computer==-1 and You==0'):
       print('You Lose')

    elif('Computer==1 and You==-1'):
       print('You lose')
    
    elif('Computer==1 and You==0'):
       print('You Win')
    
    elif('Computer==0 and You==-1'):
       print('You Win')
   
    elif('Computer==0 and You==1'):
        print('You Lose')

    else:
       print('Something went wrong!')

