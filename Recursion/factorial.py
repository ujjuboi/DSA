# basic factorial problem using recursion:

def factorial(number):
  if number == 0:
    return 1
  elif number < 0:
    return -1
  return number * factorial(number - 1)

# I dont know the use of this name == main, gonna update after research:
if __name__ == '__main__':
  # if user enters something other than an integer value:
  try:
    number = int(input("Please enter a number: "))
  except:
    number = int(input("Input Error! Please enter the number again: "))
  finally:
    if factorial(number) < 0:
      number = int(input("Please enter a whole number: "))
    print("Factorial of this number is: " + str(factorial(number)))