#calculator program
#+ - * /
#print operation error fix(insert opearaion string in if condition)
#try again etype error
#if you type 5 the result is not print you must enter first

print("Press 1: for add")
print("Press 2: for subtract")
print("Press 3: for multiply")
print("Press 4: for divide")

userInput = int(input("Enter Something: "))
#print(type(userInput))

firstNumber = int(input("Please Enter First Number: "))
secondNumber = int(input("Please Enter Second Number: "))

if userInput == 1:
    result = firstNumber + secondNumber
    operation = '+'
elif userInput == 2:
    result = firstNumber - secondNumber
    operation = '-'
elif userInput == 3:
    result = firstNumber * secondNumber
    operation = '*'
elif userInput == 4:
    result = firstNumber / secondNumber
    operation = '/'
else:
    print("You must enter 1/2/3/4!!!!",'\n')
  
'''''
if userInput ==1:
    def add(a,b):
    return a+b
    def sub(a,b):
    return a-b
    def multi(a,b):
    return a*b
    def divide(a,b):
    return a/b
'''''

#print('The number of {} {} {} is {} '.format(firstNumber, operation, secondNumber, result))


