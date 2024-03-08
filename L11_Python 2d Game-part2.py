import secrets
secureNumber = secrets.SystemRandom()

while True:
    
    print('______welcome to 2D lottery game_______')
    press1=int(input('Press 1 to Read Rule or Press 2 to Play Game>>> '))

    while press1 not in {1, 2}:
        print('You must enter 1 or 2!')
        press1 = int(input('Press 1 to Read Rules or Press 2 to Play Game>>> '))

    if press1==1:
        print('>Age must be more than 18: ')
        print('>Show money more than 5000ks:')
        print('>You must use more than 1000 each time:')
        

    if press1==2:
        print('U can play game now')
    
        uName = input('Enter Name>>> ')
        uAge = int(input('Enter Age>>> '))

        while len(uName)>2 and uAge>17:
            print('#####################')
            print('You can play game now')
            print('Welcome :> ',uName)
            while True:
                sMoney = int(input('please enter your Show Money: '))
                while sMoney>4999:
                        while True:
                            print('This is your money {}Ks '.format(sMoney))
                            inputMoney=int(input('Please enter money to Play:> '))
                            luckyNumber=int(input('please enter your lucky Number:>'))
                            print('#####################')
                            systemNumber=secureNumber.randint(10,99)
                            
                            #AI method
                            if luckyNumber == 23:
                                
                                print('### You win in 2D game, LuckyNumber is {} ###'.format(systemNumber))
                                print('#####################')
                                sMoney = (inputMoney * 10) + (sMoney - inputMoney)
                                print('This is your All Money with bonus: {} Ks'.format(sMoney))
                                toQuit = int(input('Press 0 to continue : '))
                                if toQuit == 0:
                                    break
                            else:
                                print('Try again... LuckyNumber is ', systemNumber)
                                sMoney = sMoney - inputMoney

                            if sMoney < 1000:
                                print('You have not enough money {}Ks'.format(sMoney))
                                break



                            '''''''''#old method
                            while luckyNumber== 23:
                                print('###You are win in 2D game, LuckyNumber is {} ###'.format(systemNumber))
                                #sMoney=sMoney-inputMoney
                                sMoney=(inputMoney*10)+(sMoney-inputMoney)
                                
                                print('This is your All Money with bonus:{}Ks'.format(sMoney))
                                toQuit=int(input('Press 0 to continue:> '))
                                if toQuit==0:
                                    break
                                break
                            break
                        print('Try again ... LuckyNumber is ',systemNumber)
                        sMoney=sMoney-inputMoney
                        if sMoney<1000:
                            print('you have not enough money $',sMoney)
                            break
                            '''''''''
                print('###Please More Money###')
                

        print('Please read again the rule')
    
        


