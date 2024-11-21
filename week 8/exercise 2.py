import random

def check_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i ==0:
            return True
        return True

prime_numbers = []
odd_numbers = []
even_numbers = []

random_list = [random.randint(125, 2550) for _ in range (500)]
for number in random_list:
    if check_prime(number):
        prime_numbers.append(number)
    elif number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)