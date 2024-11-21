#print all multiples of 2 from 50 to 123 given a list containing 1-150
#[start:stop:step]
list_150 = [i for i in range(1 , 151)]
list_of_2 = [list_150[1:123:2]]
print(list_of_2)

n = 0
ex_list = []
while n <= 150:
    ex_list .append(n)
    n += 1
print(ex_list)

