def romanToInt(s: str) -> int:
    conversor = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    # "CIV"
    num = 0
    cont = 0
    while cont < len(s):
        if conversor[s[cont]] > conversor[s[cont + 1]]:
            num += conversor[s[cont]]
            cont += 1
        else:
            num += conversor[s[cont + 1]] - conversor[s[cont]]
            cont += 2
    return num


print(romanToInt("MCMXCIV"))
