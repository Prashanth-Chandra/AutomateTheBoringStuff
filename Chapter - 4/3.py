grid=[['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
ans=[]
for i in range(0,len(grid)):
    for j in range(0,len(grid[1])):
        if(grid[i][j]=='.'):
            grid[i][j]=' . '


print(type(grid[1][1]))
for i in range(len(grid[1])):
    temp=[]
    for j in range(len(grid)):
        temp.append(grid[j][i])
    ans.append(temp)

for i in range(0,len(ans)):
    print(*ans[i])
