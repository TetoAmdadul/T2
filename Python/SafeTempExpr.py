print('Enter C or F:')
scale = input()
print('Enter the Temp:')
degrees = int(input())
if (scale == 'C' and degrees >= 16 and degrees <= 32) or (scale == 'F' and 60<=degrees <= 100):
print('safe')
else:
print('danger')
