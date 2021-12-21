tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    l1=max(table[0],key=len)
    l2=max(table[1],key=len)
    l3=max(table[2],key=len)
    for i in range(0,len(table[1])):
        print(table[0][i].rjust(10),table[1][i].rjust(10),table[2][i].rjust(10))
printTable(tableData)

