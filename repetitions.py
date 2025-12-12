check=input()
output=1
curLen=1
for x in range(1,len(check)):
    if check[x]==check[x-1]:
        curLen+=1
    else:
        curLen=1
    output=max(output,curLen)
print(output)