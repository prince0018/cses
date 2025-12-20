n=int(input())
arr=[]
arr = list(map(int, input().split()))
res=0
for x in range(1,len(arr)):
    if arr[x]<arr[x-1]:
        res+=(arr[x-1]-arr[x])
        arr[x]=arr[x-1]
print(res)...