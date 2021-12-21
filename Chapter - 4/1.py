a=list(map(str,input().split()))
ans="' "
for i in range(0,len(a)):
    if(i!=len(a)-1):
        ans+=a[i]
        ans+=', '
    else:
        ans+=a[i]
ans+=" '"
print(ans)
