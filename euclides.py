n = int(input("N: "))
div = int(input("D: "))
resto = 100
while resto != 0:
    quo = n//div
    resto = n%div

    print("Quoc: ", quo)
    print("Rest: ", resto)
    print("--"*10)
    n = div
    print("N:", n)
    div = resto
    print("D: ", div)

