def cyclic_shift_slicing(m, shift):
    # This function is the same function i created from task 1, it ensures the shift is within the valid range by using the remainder operator
    # The remainder operator (%) ensures that the shift value is always between 0 and len(m)-1
    shift = shift % len(m)

    # This IF statement checks if the shift is 0
    # If the shift is 0, it means no shifting is needed, so we return the original message
    if shift == 0:
        return m

    # Performing the cyclic shift by slicing the message

    # m[-shift:] gives the last 'shift' elements by using negative slicing
    # This slice starts 'shift' elements from the end and goes to the end of the list
    # m[:-shift] gives all elements except the last 'shift' elements
    # This slice starts at the beginning and goes up to 'shift' elements from the end (not including the 'shift' element)
    # The + operator joins the two slices together
    # So, m[-shift:] + m[:-shift] combines the end part of the list with the beginning part
    return m[-shift:] + m[:-shift]

def encrypted_message(key, message):
    # Step 1: Accept an encryption key containing 6 characters
    # Then using an if statement, check if the length of the key is exactly 6 characters
    if len(key) != 6:
        # If not, raise an error with a message
        raise ValueError("The encryption key must contain exactly 6 characters.")

    # Step 2: Accept a message m to be encrypted
    # Assign the input message to the variable of m
    m = message

    # Step 3: Extend out the message with additional “a” characters until its new length is a multiple of 8
    # I am now using a while loop, so that while the length of the message is not a multiple of 8 it adds the 'a' characters
    while len(m) % 8 != 0:
        # Add an "a" character to the end of the message
        m += 'a'

    # Step 4: Split the new message into a list of subsequences of 8 characters
    # I've now created a list of 8-character subsequences from the message
    # [m[i:i + 8] - This part slices the string m from index i to i + 8.
    # for i in range(0, len(m), 8): - This part creates a range of numbers starting from 0 up to len(m) (the length of the string m), with a step size of 8.
    # For each value of i generated by the range, it takes a substring of m starting at i and ending at i + 8 (not including i + 8).
    subsequences = [m[i:i + 8] for i in range(0, len(m), 8)]

    # Step 5: Calculate shift1 from the key
    # ord(key[0]) and ord(key[1]) get the ASCII values of the first two characters of the key
    # Adding these values together and taking the remainder when divided by 8 gives shift1
    shift1 = (ord(key[0]) + ord(key[1])) % 8

    # Step 6: Perform a right cyclic shift of size shift1 on each subsequence
    # Apply the cyclic_shift_slicing function to each subsequence with shift1
    shifted_subsequences = [cyclic_shift_slicing(subseq, shift1) for subseq in subsequences]

    # Step 7: Calculate shift2 from the key
    # ord(key[2]) and ord(key[3]) get the ASCII values of the third and fourth characters of the key
    # Adding these values together and taking the remainder when divided by 3 gives shift2
    shift2 = (ord(key[2]) + ord(key[3])) % 3

    # Step 8: Perform a cyclic shift of size shift2 on the list of subsequences
    # Apply the cyclic_shift_slicing function to the list of shifted subsequences with shift2
    shifted_list = cyclic_shift_slicing(shifted_subsequences, shift2)

    # Step 9: Concatenate the subsequences together to form the encrypted message
    # ''.join(shifted_list) joins all the subsequences into a single string
    encrypted_message_result = ''.join(shifted_list)

    # Return the encrypted message
    return encrypted_message_result

# Test cases
encryption_key = "TheKey"
original_message = "abcdefghijklmnopqrstuv"

# Encrypt the message using the provided key
encrypted_result = encrypted_message(encryption_key, original_message)

# Print the original message
print(f"Original message: {original_message}")
# Print the encrypted message
print(f"Encrypted message: {encrypted_result}")

# Additional test cases
test_cases = [
    ("abcdef", "hello world"),
    ("123456", "This is a test message"),
    ("Python", "Encrypt this text"),
]

# Loop through each test case
for test_key, test_message in test_cases:
    # Encrypt the message using the provided key
    encrypted_result = encrypted_message(test_key, test_message)
    # Print the original message
    print(f"Original message: {test_message}")
    # Print the encrypted message
    print(f"Encrypted message: {encrypted_result}")
