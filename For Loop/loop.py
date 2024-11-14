listnum = (25, 33, 72, 81, 49, 50, 101, 23)
initalgreatnum = 0
for num in listnum:
    if initalgreatnum < num:
        initalgreatnum = num

print(initalgreatnum)