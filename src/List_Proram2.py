# to find the greatest integer in list
s = int(input("enter a size of list"))
l = []
for i in range(0, s):
    e = int(input("enter element"))
    l.append(e)
l.sort()
print(l[s - 1])
