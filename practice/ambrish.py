
n=int(input())
s=0
for i in range(n+1):
    for j in range(n,0,-1):
        if i*j==n:
            s+=i
print(s)            