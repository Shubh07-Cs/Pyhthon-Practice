a=int(input())
i=0
while a>10:
    a=a/3
    i=i+1
print(i)    


a=int(input())
for i in range(a):
    print(2*i,end=" ")

s=0
for i in range(10,20):
    if i%2==0:
        print(i)
        s=s+i
print('even sum:',s)