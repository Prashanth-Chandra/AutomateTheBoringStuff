def displayInventory(inv):
    print("Inventory :\n")
    count=0
    for k,v in inv.items():
        print(v,k,"\n")
        count+=v
    print("Total Number Of Items : ",count)
p_inv={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(p_inv)
