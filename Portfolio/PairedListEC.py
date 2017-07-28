number = int(input("Enter a two digit number.\n"))
request = input("Press 1 to check if the number is divisible by 5 or 2 to check if it is prime.\n")

#Create multiple of 5 function
def MultOf5():
    if number % 5 == 0:
        return True
    else:
        return False

#Create prime number function
def PrimeNumber():
    if number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        return True
    else:
        return False

#Call multiple of 5 function
if request == "1":
    print(MultOf5())

#Call prime number function
if request == "2":
    print(PrimeNumber())
