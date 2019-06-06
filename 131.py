a1=int(input())
n=a1//2
d=0
for x in range(2,n+1):
    if a1%x==0:
        d=1 
if d==0:
    print('yes')
else:print('no')
