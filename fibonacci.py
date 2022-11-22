# 1 2 3 4 5 6 7  8
# 1 1 2 3 5 8 13 21 

n = int(input())

a = 1
b = 1
for i in range(n-2):
    c = a + b
    a = b
    b = c
print(b)
