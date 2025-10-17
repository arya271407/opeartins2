try:
  a = float(input("enter first number"))
  b = float(input("enter second number"))
  print(f"addition:{a+b}")
  print(f"subtraction:{a-b}")
except ValueError:
  print("please enter a valid number.")
