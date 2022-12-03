# This subroutine creates a random pin number for us in every single time.
def pinpicker(num):
  import random
  pin = ''
  for i in range(num):
    pin += str(random.randint(1, 9))
  return pin
pin = pinpicker(4)
print(pin)
