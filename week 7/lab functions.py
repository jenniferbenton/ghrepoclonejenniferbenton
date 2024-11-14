def max_of_two(x, y):
    if x > y:
        return x

    elif y > x:
        return y

    else:
        return None



x = float(input("Please enter a value for x: ")    )
y = float(input("Please enter a value for y: ")    )

print(f"The larger value is {max_of_two(x, y)}")

max_of_two = lambda x, y: x if x > y else y if y > x else None

x = float(input("Please enter a value for x: "))
y = float(input("Please enter a value for y: "))

print(f"The larger value is {max_of_two(x, y)}")





