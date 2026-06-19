print('Enter an Integer:')
n = int(input())
if n%3 == 0 and n%5 ==0:
      print('Fizz Buzz')
elif n%3 == 0:
    print('Fizz')
elif n%5 == 0:
     print('Buzz')
#elif n%3 == 0 or n%5 ==0:
 #     print('Fizz Buzz')
else:
    print(n)
