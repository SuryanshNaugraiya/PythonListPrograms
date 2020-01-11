# to create a list of squares of first N natural numbers
l = []
N = int(input("enter N"))
for i in range(1, N + 1):
    l.append(i * i)
print(l)
