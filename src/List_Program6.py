# to print the index of all occurence of a given element in a list
l = [2, 3, 4, 0, 3, 1, 2, 4, 3, 0]
e = 0
for i in l:
    if i == e:
        print(l.index(i))
        l[l.index(i)] = ''
