n = int(input())
s = input().strip()
toffees = [1] * n
for i in range(n-1):
    if s[i] == 'R':  
        toffees[i+1] = max(toffees[i+1], toffees[i] + 1)
    elif s[i] == 'L':  
        toffees[i] = max(toffees[i], toffees[i+1] + 1)
for i in range(n-2, -1, -1):
    if s[i] == 'R': 
        toffees[i+1] = max(toffees[i+1], toffees[i] + 1)
    elif s[i] == 'L':  
        toffees[i] = max(toffees[i], toffees[i+1] + 1)
print(*toffees)
