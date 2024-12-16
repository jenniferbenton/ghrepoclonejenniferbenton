def cyclic_shift_slicing(m, shift):
    # This new function ensures the shift is within the valid range by using the remainder operator (%)
    # This handles cases where the shift is greater than the length of whatever m is
    shift = shift % len(m)

    # I've used this if statement so that if the shift is 0, it returns the original message as no shift is needed
    if shift == 0:
        return m

    # Now the system will perform the cyclic shift by slicing the message
    # m[-shift:] gives the last 'shift' elements bu using negative slicing. This slice starts shift elements from the end and goes to the end of the list
    # m[:-shift] gives all elements except the last 'shift' elements. This slice starts at the beginning and goes up to shift elements from the end (not including the shift element)
    # The + operator joins the two slices together. So, m[-shift:] + m[:-shift] combines the end part of the list/ with the beginning part.
    return m[-shift:] + m[:-shift]


# These are my test cases to verify the function works correctly with different types of inputs

# Test case 1: m is a string
print(cyclic_shift_slicing("This is a secret message", 2))  # Expected: "geThis is a secret messa"

# Test case 2: m is a list of numbers
print(cyclic_shift_slicing([1, 2, 3, 4, 5], 2))  # Expected: [4, 5, 1, 2, 3]

# Test case 3: m is a list of strings
print(cyclic_shift_slicing(["a", "b", "c", "d"], 1))  # Expected: ["d", "a", "b", "c"]

# Test case 4: m is a list of lists
print(cyclic_shift_slicing([[1, 2], [3, 4], [5, 6]], 1))  # Expected: [[5, 6], [1, 2], [3, 4]]