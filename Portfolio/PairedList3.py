random_numbers = [29, 68, 69, 30, 20, 91, 62, 28, 36, 67, 40, 71, 71, 82, 71, 84, 96, 34, 40, 92, 57, 56, 86, 63, 88, 79, 48, 22, 12, 74,
86, 54, 94, 19, 73, 25, 23, 72, 74, 56,53, 52, 55, 10, 37, 48, 82, 84, 57, 45, 85, 48, 58, 56, 95, 21, 47, 98, 71, 38, 24, 51, 28, 71,
52, 33, 78, 78, 77, 24,17, 31, 85, 87, 86, 63, 23, 73, 40, 64, 35, 29, 10, 43, 99, 38, 63, 61, 76, 91, 64, 48, 23, 26, 19, 21, 17, 49, 15, 62]

#Create empty list of primes
primes = []

#Add prime numbers to list
for x in random_numbers:
    if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0:
        primes.append(x)

#Adds all prime numbers together
answer = 0
for z in (primes):
    answer += z

print(answer)
