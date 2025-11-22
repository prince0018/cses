n=int(input())
lst=input().split(" ")
hashSet=set()
for i in (lst):
    hashSet.add(int(i))
for x in range(1,n+1):
    if x not in hashSet:
        print(x) 

