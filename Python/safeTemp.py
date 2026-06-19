print('Enter C if temparature in celcius, or F if it is Farenhite')
scale = input()
print('Enter tempartes in number')
degrees = int(input())
if scale == 'C':
   if degrees >= 16 and degrees <= 38:
      print('safe') 
   else:
        print('dangerous') 
elif scale == 'F':
     if degrees >= 60 and degrees <= 100:
        print('safe')
     else:
          print('dangerous')
else:
     print('Invalid Input')
