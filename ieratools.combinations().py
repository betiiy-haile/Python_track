from itertools import combinations
S,k = input().split()
k = int(k)

for i in range(1,k+1):
    for j in list(combinations(sorted(S),i)):
        print(''.join(j))