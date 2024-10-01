def tri(n):
    for i in range(1, n+1):
        print('*'*i)
    for i in range(n-1, 0, -1):
        print('*'*i)

tri(5)

for i in range(1, 11):
    print((2*i)**3)