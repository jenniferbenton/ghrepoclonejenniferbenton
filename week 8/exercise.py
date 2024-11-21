user_num = int(input("Please enter a number: "))
result = 0
for i in range(1, user_num + 1):
    result += i

print(f"The sum of all the number from 1 to {user_num} is {result}")

def sum_n_num(number):
    """

    :param number: user entered number
    :return: sum of the n number in the iteration
    """
    sum_n = 0
    for num in range(number):
        sum_n +=num

    return sum_n

if __name__ == '__maim__':
    user_num = int(input(f"Please enter a whole number"))
    sum_of = sum_n_num(user_num)
    print(f"The sum of 1 to {user_num} is {sum_of}")



