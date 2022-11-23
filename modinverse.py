def modInverse(a, m):

    for x in range(1, m):
        if (((a % m) * (x % m)) % m == 1):
            return x
    return -1


# Driver Code
a = int(input("N: "))
m = int(input("mod: "))

# Function call
print("Inverso Multiplicativo:", modInverse(a, m))
