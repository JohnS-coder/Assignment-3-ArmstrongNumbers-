number = input("Enter a number: ")
if set(number).issubset(set("1234567890-,.")) == False:
  print("Do not use any entries other than numeric values")
elif set((",",".")).isdisjoint(set(number)) == False:
  print("Please enter an integer")
elif int(number) > 0: 
  x = 0 
  for i in [int(digit)**len(number) for digit in number]:
    x += i
  if x == int(number):
   print(f"{number} is an Armstrong number")
  else:
    print(f"{number} is not an Armstrong number")
elif int(number) <0:
  print("Please enter a positive number")
else:
  print("Do not use any entries other than numeric values")