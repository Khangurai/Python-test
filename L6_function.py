#function
#standard library function ori
#programmer defined function us
from math import sqrt
import math

ls=[1,2,3,4,5]

len(ls)  #prarmeter ကို length တွက်ပေးတာ
#print("the length of ls is ",len(ls))

#print("the Square root of ",sqrt(4))
#square root value
#data=int(input("please enter number to sqart: "))
#print("The square root of {} is {} ".format(data,sqrt(data)))

#length = 32423
#print("the length of square is: ",len(length)) false
#https://ioflood.com/blog/len-python/#:~:text=Working%20with%20Lists%20and%20Tuples&text=Here%2C%20len()%20returns%20the,will%20result%20in%20a%20TypeError.

#pi value
#print("the value fo pi is ",math.pi)

#exp value
#print("the exp of {} is {}".format(data,math.exp(data)))

#hex value(123456789a...)
#print("the hex value of {} is {}".format(data,hex(data)))


#programmar defined function us
'''''
def myFun():
    print("I am from myFun")
print(myFun())
'''''

def add(a,b):#function header  a,b = parameter
    return a+b#function body
#print(add(4,5)) #argument>>>(4,5)လှမ်းခေါ်တဲ့နေရာကအထဲမှာရှိတဲ့ကောင်ဆို positional argument

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

data1=int(input("Enter first Number: "))
data2=int(input("Enter second Number: "))

print("adding :",add(data1,data2))
print("sub    :",sub(data1,data2))
print("multi  :",multi(data1,data2))