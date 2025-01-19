num1 = int(input('Enter the first number:'))
num2 = int(input('Enter the second number:'))
oprations = input('Choose the operation (+, -, *, /):')
result = 0
match oprations:
  case "+":
    result = num1 + num2
    print(f'The result is {result}')
  case "-":
    result = num1 - num2
    print(f'The result is {result}')
  case "*":
    result = num1*num2
    print(f'The result is {result}')
  case "/":
    if num2 == 0:
      print("Invalid opration")
    else:
      result = num1/num2