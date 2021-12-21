import re
inp=input()
spa=re.compile(r'^\s+|\s+$')
spaces=len(spa.findall(inp))
ans=''
if(spaces>0):
    ans=spa.sub("",inp)
print(ans)
