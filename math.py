try:
  a = float(input("enter first number"))
  b = float(input("enter second number"))
  print(f"addition:{a+b}")
  print(f"subtraction:{a-b}")
  print(f"multiplication:{a*b}")
  if b != 0:
        print(f"division:{a/b}")
  else:
        print("division by zero is not allowed")
except ValueError:
  print("please enter a valid number.")
