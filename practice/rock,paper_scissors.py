import random
a=['rock','paper','scissor']
us=0
pcs=0
while True:
    q=input('wanna play one more time:')
    if q=='Y' or q=='y':
        pc=random.choice(a)
        u=(input('lets play rock paper scissor:  '))
        print(' choosen by pc: ',pc)

        if  pc==u  :
            print('tie lets go again')
        elif pc=='rock' and u=='paper':
            us+=1
            print(' YOU win')
        elif pc=='rock'and u=='scissor':
            pcs+=1
            print('aha...loose')   
        elif pc=='paper' and u=='scissor':
            us+=1
            print(' YOU win')
        elif  pc=='paper' and u=='rock':
            pcs+=1
            print(' oh dear you are loosing')
        elif pc=='scissor'  and u=='paper':
            pcs+=1
            print(' hehehe....loose')
        elif pc=='scissor'  and u=='rock' :
            us+=1
            print(' YOU win')  

    else:
        print('sad to see you go')
        print('total score of your:',us)
        print('total score of computer:',pcs)
        break
    