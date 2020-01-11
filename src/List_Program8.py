# to print distinct list elements along with their frequency of occurence in the list
l1 = []
l2 = [2, 3, 4, 5, 1, 2, 3, 4, 2, 1, 5, 6, 5]
for i in l2:
    if i not in l1:
        print(i, l2.count(i))
        l1.append(i)

