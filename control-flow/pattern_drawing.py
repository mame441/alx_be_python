length = int(input('Enter the size of the pattern:'))
base = 1
while base <= length:
  width = 1
  while width <= length:
    print("*", end="")
    width +=1
  print()
  base +=1