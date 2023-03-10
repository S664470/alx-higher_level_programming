#!/user/bin/python3
for i in range(0, 10):
    for j in range(i + 1):
        if j != i:
            print("{}{},". format(i, j), end=" ")
