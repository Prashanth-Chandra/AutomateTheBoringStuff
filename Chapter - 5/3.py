def displayInventory(inv):
    print("Inventory :\n")
    count=0
    for k,v in inv.items():
        print(v,k,"\n")
        count+=v
    print("Total Number Of Items : ",count)

def addToInventory(inv,loot):
    for i in range(0,len(loot)):
        if loot[i] in inv.keys():
            inv[loot[i]]+=1
        else:
            p_inv[loot[i]]=1


p_inv={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(p_inv,dragonLoot)
displayInventory(p_inv)

