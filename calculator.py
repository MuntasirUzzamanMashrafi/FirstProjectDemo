def calculator(ope):
    num1=0
    num2=0
    result=0
    try:
        if ope==1:
            num1=int(input('give the first number: '))
            num2=int(input('give the second number: '))
            return f'{num1+num2}'
        elif ope==2:
            num1=int(input('give the first number: '))
            num2=int(input('give the second number: '))
            return f'{num1-num2}'
        elif ope==3:
            num1=int(input('give the first number: '))
            num2=int(input('give the second number: '))
            return f'{num1*num2}'
        elif ope==4:
            if num2==0:
                print("Can't divide by zero")
                return 0
            return f'{num1/num2}'
        elif ope==5:
            return 5
        else:
            print('\n======== ERROR: Choose a correct operation=======')

            
        
    except ValueError:
        print('\n==== ERROR: Choose a correct operation ===')
    


while True:
    try:
        ope = int(input('\nchoose your operation: \n1. Addition\n2. subtract\n3. Multiplication\n4. Division\n5. Exit\nYour want to: '))
    except ValueError:
        print('\n=== ERROR: Choose a correct operation===')

    if ope==5:
        print("\n===========Thank You================")
        break
    else:
        result=calculator(ope)
        if result is None:
            pass
        else:
            print(f'\n========     Your result is: {result}     ================') 
