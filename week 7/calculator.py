def calculate(num1:float, num2:float, operation:str):
    """

    :param num1: The first argument should be a number
    :param num2: The second argument, also a number
    :param operation: Should either be one of the following: add, subtract, multiply, divide
    :return: return a float output
    """
    if operation.lower() == 'add':
        result = num1 + num2

    elif operation.lower() == 'subtract':
        result = num1 - num2

    elif operation.lower() == 'multiply':
        result = num1 * num2

    elif operation.lower() == 'divide':
        result = num1/num2

    else:
        raise Exception

    return result
if __name__ == '__main__':
    number_1 = float(input(f'Please enter the first number:  '))
    number_2 = float(input(f'Please enter the second number: '))
    operat_input = input(f'Please enter the operation to pick from (add, multiply, subtract, divide')
    result = calculate(number_1, number_2, operat_input)
    print(f'You have entered number 1 as {number_1}')
    print(f'You have entered number 2 as {number_2}')
    print(f'You want to perform {operat_input} on {number_1} and {number_2}')