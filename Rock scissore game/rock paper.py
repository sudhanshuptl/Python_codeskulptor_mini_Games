# rock scissors lizard paper Spok Game 
        # Sudhanshu Patel
        #  NIT ROURKELA

import random #

def name_to_number(name): #convert name to number 
    if(name=='rock'):
        return 0
    elif(name=='Spock'):
        return 1
    elif(name=='paper'):
        return 2
    elif(name=='lizard'):
        return 3
    elif(name=='scissors'):
        return 4
    else:
        return 100 ## error handeling if non of above found
        
def number_to_name(number):
            if(number==0):
                return 'rock'
            elif(number==1):
                return 'Spock'
            elif(number==2):
                return 'paper'
            elif(number==3):
                return 'lizard'
            elif(number==4):
                return 'scissors'
            else:
                return 'Wrong !!'
                
def rpsls(name):
    player_number=name_to_number(name)
  
    comp_number=random.randrange(0,5,1)
    diff = player_number - comp_number
    
    print 'Player choose ',name
    print 'Computer choose ',number_to_name(comp_number)
    
    # check winner from diff
    
    if(diff>0 and diff<=2 and player_number in (2,3,4)):
        print 'Player wins!'
    elif(player_number == 0 and diff in (-4,-3)):
        print 'Player wins!'
    elif(player_number == 1 and diff in(-3,1)):
        print 'Player wins!'
    elif(diff == 0):
        print 'Player and Computer tie!'
    elif(diff>4 or diff<-4):
        print 'Error occure'
    else:
        print 'Computer wins!'
        
    print ''
         
rpsls('rock')
rpsls('Spock')
rpsls('paper')
rpsls('lizard')
rpsls('scissors')