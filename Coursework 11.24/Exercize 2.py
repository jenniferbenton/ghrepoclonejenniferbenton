#This is my introduction. The user is prompted to enter their name by using the input function and the system then greets them and explains the question.
#The user is then prompted to answer the given question, again, using the input function in a range from 1-10. i used \n to space it out onto new lines. The f string allowed me to import the
#user's input value into the string.
print("Hello and welcome to MoodSense! Today i will analyzing your mood based on your rating of how you feel today.")
name = input("First question is can you please give me your name?: ")
print(f"Nice to meet you {name}. Lets get started. \nOn a scale of 1-10, 1 being bad and 10 being great, how would you rate your mood recently?")
score = int(input("Please answer here: "))
#I then use conditional statements to tailor the systems response depending on the user input's value. I firstly use the if statement for the first condition. If the input is false according to
#the 'if' statement, I then created an elif statement for another condition. If the user's input is also false according to the elif statement, I created an else statement for every other condition.
if score <= 3:
    print(f"You have rated your mood as a {score}. I'm sorry you feel this way {name}. Chatting to family and friends can help take the burden off. For more information please visit the NHS mental wellbeing site.")
elif score >=8:
    print(f"You have rated your mood as a {score}. Fantastic! I'm so glad you feel this way {name}. Do remember that even during this period of happiness, it's still okay to feel down time to time.")
else:
    print(f"You have rated your mood as a {score}. It seems like your mood is in mid-range. Remember to take time for yourself and consider journaling to help understand your feelings.")