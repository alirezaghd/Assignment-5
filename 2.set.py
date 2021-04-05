list_1 = []

n = int(input("ye adad bede :) : "))

for i in range(n):
     list_1.append(int(input("hala be andaze adadi k dadi adad bede :))) : ")))

print(list_1)

list_2 = []

m = int(input("ye adad dg bede :) : "))

for i in range(m):
     list_2.append(int(input("hala be andaze adadi k dadi adad dg bede :))) : ")))

print(list_2)

set1 = set(list_1)
set2= set(list_2)

set3 = set1.union(set2)
print("Your union list : ",set3)

set4 = set1.intersection(set2)

print("Your intersection list : ",set4)
