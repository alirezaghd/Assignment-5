f0, f1, f2 = 1, 0, None

counter = 0
li = []
n = int(input())
while counter < n:
    f2 = f0 + f1
    li.append(f2)

    f0 = f1
    f1 = f2
    counter += 1

tuple1 = tuple(li)
print(tuple1)
