# to print a list of N  prime numbers
N = int(input("enter size"))
l = []
for i in range(2, 1000 * N):
    for j in range(2, i + 1):
        if (i % j) != 0:
            l.append(i)
    if l.index(i) == (N - 1):
        break;
print(l)
