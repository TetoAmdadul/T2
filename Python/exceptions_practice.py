try: 
   number  = int(input("Please enter a valid number: "))
   result = 100/ number
  
except ValueError:
       print("please enter valid number.")

except ZeroDivisionError:
       print("number cannot be Zero.")

else:
    print(result)

finally:
   print("program finished.")
