def sum_even_num(user_provided_number):
    """

    :param user_provided_number: user provided integer num
    :return: sum of numbers in int/whole number
    """
    sum_even = 0
    for i in range(0, user_provided_number+1, 2):
        if i == 0:
            continue
        else:
            sum_even +=i
        print(i)
        print(f'Sum of even numbers at {i} is {sum_even}')

if __name__ == "__main__":
    sum_even_num(20)




