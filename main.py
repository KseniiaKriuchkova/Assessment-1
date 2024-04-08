"""
PowerOfTen
"""
# Provide your solution here
while True:
    number=int(input("Enter a max 3 digit number: "))
    if number<0:
        print("number cannot be negative")
    elif number > 999:
        print("number has more than 3 digits")

"""
Cash Box
"""
# Provide your solution here
while True:
  to_pay=int(input("To pay: "))
  if to_pay < 0:
      print("Negative payment is invalid.")
      continue
  received = int(input("Received: "))
  if received<0:
    print("Negative received amount is invalid.")
  elif received > to_pay:
    change=int(received-to_pay)
    print("Your change is: "+str(change))
  else:
      print("You did not pay enough.")




