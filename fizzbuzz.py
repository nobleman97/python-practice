for num in range(0, 100):
    num +=1
    

    if num % 3 == 0 and num % 5 == 0:
        print('fizzBuzz')
    elif num % 3 ==0 and num % 5 != 0:
        print('fizz')
    elif num % 5 ==0 and num % 3 != 0:
        print('buzz')
    else:
        print(num)
