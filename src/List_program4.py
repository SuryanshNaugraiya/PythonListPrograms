# to print a list of N  prime numbers
N = int(input("enter no of prime no."))
s = 0
c = 0
l = [2]
for i in range(3, 100 * N):
    for j in range(2, i):
        if (i % j) == 0:
            s = s + 1
    if s == 0:
        l.append(i)
        c = c + 1
    if c == N - 1:
        break
    s = 0
print(l)
