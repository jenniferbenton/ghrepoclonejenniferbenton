#System Health Monitoring Bot"

#This is my introduction. The system greets them and asks them to enter their name and what computer model they're using.
# I use the input function to make 'name' and 'computer' become a variable that can be given a value of anything depending on what the user types.
# I then print an f string so that i can then add these variables to make the sentence personalised to the user.
print("Hello! Please enter your name and your computer model")
name = input("Name: ")
computer = input("Computer Model: ")
print(f"Hi {name}, today i will be monitoring your {computer}'s CPU usage and memory usage to determine it's utilisation.")
#Now, i have created two new variables called 'CPU' and 'memory' using the input function. The user gives these a value based off of what their CPU usage and memory usage is.
# I put % and GB in brackets so the user will just enter an integer and know what the format is.
CPU = float(input("Please enter your CPU percent usage (%): "))
memory = float(input("Now, enter your memory usage (GB): "))
# Now i am using conditional statements to determine what answer will be returned from the system regarding their CPU optimisation.
# I first create an IF statement for the first condition being if the CPU is overloaded.
# If the IF statement is false dependent on the user's input, i have created an ELIF statement as an additional condition for if the CPU is underutilised.
# If the user's input is false according to the IF and ELIF statement, I have created an ELSE statement for any other value inputted by the user. This will tell them their CPU usage is optimal
if CPU > 75:
    print(f"{name}, your {computer}'s CPU is overloaded. You may experience reduced system performance, battery consumption and hardware overheating. ")
elif CPU < 40:
    print(f"{name}, your {computer}'s CPU is underutilized. Your system may run smoother and have a reduced chance of crashing, however your CPU is in insufficient use so you should maybe consider downsizing.")
else:
    print("Your CPU is optimal! Try and keep it this way for sufficient optimisation.")
# I am now doing the same for the memory usage.
# I first create an IF statement for the first condition being if the memory usage is overloaded.
# If the IF statement is false dependent on the user's input, i have created an ELIF statement as an additional condition for if the memory usage is underutilised.
# If the user's input is false according to the IF and ELIF statement, I have created an ELSE statement for any other value inputted by the user. This will tell them their memory usage is optimal.
if memory > 8:
    print("Your memory seems to be overloaded. This means your systems may run slower.")
elif memory < 4:
    print("Your memory seems to be underutilized. This means your system should run smooth, however your memory is isn't in sufficient use, so you should consider downsizing. ")
else:
    print("Your memory seems to be optimal. Try and keep it this way for sufficient optimisation.")
