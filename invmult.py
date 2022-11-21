import sys

if len(sys.argv) == 3:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
else:
    a = int(input('a: '))
    b = int(input('b: '))

while b != 1:
    r = a % b
    q = a // b
    
    print(f"{a:3} {b:3} {q:3} {r:3}")
    a = b
    b = r
    if b == 0:
        break