def fizzbuzz(a):
    if a%3==0 and a%5==0:
        print('FizzBuzz')
    elif a%3==0 and a%5!=0:
        print('Fizz')
    elif a%3!=0 and a%5==0:
        print('Buzz')
    else:
        print(a)

for i in range(3):
    s = input()
    try:
        s = int(s)
        if i == 0:
            fizzbuzz(s+3)
            break
        elif i == 1:
            fizzbuzz(s+2)
            break
        else:
            fizzbuzz(s+1)
            break

    except:
        pass

    