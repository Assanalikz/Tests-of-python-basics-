import math
def squareofnumber():
    squared_value = value ** 2
    print(squared_value)

def rootofnumber():
    sqrtvalue = (math.sqrt(value2))
    print(sqrtvalue)

while True:
    print('You want to square the number?')
    answer = input()
    if answer == 'yes':
        print('Put your values')
        value = int(input())
        squareofnumber()
    else:
        print('put your number')
        value2 = int(input())
        rootofnumber()
    if input('Do you want to repeat(y/n)') == 'n':
        break