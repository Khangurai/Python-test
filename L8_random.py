#random

#Random
#random.random() return floating point 0.0 and 1.0 #default result

#Use Int(return)     
#         /\
#        /  \
#randint    randrange

#randint  >> a<= number <=b randint(0,9)

#randrange >> radndrange(0,10,2) (start,stop, step)
#                                the step is optional default is 1

#_____________________________________

#random.choice random with (list,name,any element)

#_________________________________________________

#random.seed(5)>>(5)parameter
#_________________________________________________
#random.shuffle() list tuple dict set
#_________________________________________________
#integer ဆို randint နဲ့ randrange(x,y,z)
#float ဆို random.uniform နဲ့ random.triangular(x,y,z)

import random

'''''
print(random.random())
# 0.0 to 0.1
'''
#randint() and randrange()
'''''
print('printing random integer(randint)',random.randint(0,9))
print('printing random intger(randrange)',random.randrange(0,10,2))
'''''
#random.choice
'''''
name=['aung','kaung','khant','ray','python','roadmap']
print('select element "{}" '.format(random.choice(name)))
'''''
#random.sample ဘယ်နှခုလိုချင်တာလဲ ရေးတဲ့ဟာ
#print က list အနေနဲ့ထုတ်ပေးတာ
'''''
name=['aung','kaung','khant','ray','python','roadmap']
print('select element "{}" '.format(random.sample(name,3)))
'''''
#random.seed(5)
'''''
random.seed(9) #value ထည့်ရင် result တူ
print('random number from seed()',random.random())
'''''
#random.shuffle() list tuple dict set
'''''
name=['aung','kaung','khant','ray','python','roadmap']
print('before shuffle',name)
random.shuffle(name)
print('after shuffle',name)
'''''
#random.uniform(start,end)  #floating point
'''''
print('uniform',random.uniform(10.5,20.5))
'''''
#random.triangular(start,end,move)
'''''
print('traiangular',random.triangular(10.5,20.5,2.5))
'''''