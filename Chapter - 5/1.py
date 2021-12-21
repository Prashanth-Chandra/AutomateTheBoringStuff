board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

def chessBoard(board):
    wKing, bKing, wPieces, bPieces,wPawns, bPawns=0,0,0,0,0,0
    check=True
    all_pos_avail=[]

    for x in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
        for y in range(1,9):
            all_pos_avail.append(str(y)+str(x))
            
    for k,v in board.items():
        if k not in all_pos_avail:
            print('Position is wrong for ',k,v)
            check = False
        #try:
         #   all_pos_avail.remove(k)
        #except:
        #    print("ERROR : Either the position is wrong or trying to place two or more pieces into a single block ",k)
        if(v=='wking'):
            wKing += 1
        if(v=='bking'):
            bKing += 1
        if(v=='wpawn'):
            wPawns += 1
        if(v=='bpawn'):
            bPawns += 1
        if(v[0]=='w'):
            wPieces += 1
        if(v[0]=='b'):
            bPieces += 1
            
    if(wKing!=1):
        print('White King Error \nThere are : ',wKing,' White King(s)')
        check = False
    if(bKing!=1):
        print('Black King Error \nThere are : ',bKing,' Black King(s)')
        check = False
    if wPieces > 16:
        print('Total white pieces on board > 16: ',wPieces)
        check = False
    if bPieces > 16:
        print('Total black pieces on board > 16: ',bPieces)
        check = False
    if wPawns > 8:
        print('White pawns on board > 8: ',wPawns)
        check = False
    if bPawns > 8:
        print('Black pawns on board > 8: ',bPawns)
        check = False
  
    if check:
        return True
    else:
        return False    
print('\n')
print("Final check : ",chessBoard(board))
