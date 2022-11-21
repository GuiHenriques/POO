import time

rigth = wrong = 0
rank = []
code = 15645692845
while True:
    start = time.time()
    n = int(input())
    end = time.time()
    if n == code:
        rank.append(end - start)
        rigth += 1
    elif n == 0:
        break
    else:
        print("\033[31mError\033[m")
        wrong += 1

for i in sorted(rank):
    print(i)
print(f"Right: {rigth} Wrong: {wrong}\nMed: {sum(rank)/len(rank)}")
