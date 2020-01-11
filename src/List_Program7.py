# to print the sum of all even no. and sum of all odd no. in the list
l = [2, 3, 4, 1, 2, 3, 7, 6, 9]
s1 = 0
s2 = 0
for i in l:
    if i % 2 == 0:
        s1 = s1 + i
    else:
        s2 = s2 + i
