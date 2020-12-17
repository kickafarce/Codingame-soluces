import sys
import math

tabDirInit = ['S', 'E', 'N', 'W']
dirNorm = ['SOUTH', 'EAST', 'NORTH', 'WEST']
bCasseur = False

def checkPos(pos, iTab):
    bOk = True
    tabSym = iTab[pos[0]][pos[1]]
    if tabSym == 'X' and  bCasseur:
        iTab[pos[0]] = iTab[pos[0]][:pos[1]] + ' ' + iTab[pos[0]][pos[1]+1:]
    elif tabSym == '#' or tabSym == 'X':
        bOk = False
    return bOk

def computeNextPos(pos, tab, dir):
    nextPos = pos.copy()
    posi = 0
    moveOk = False

    while not moveOk:
        if dir == 'SOUTH':
            nextPos = [pos[0]+1, pos[1]]
        elif dir == 'EAST':
            nextPos = [pos[0], pos[1]+1]
        elif dir == 'NORTH':
            nextPos = [pos[0]-1, pos[1]]
        elif dir == 'WEST':
            nextPos = [pos[0], pos[1]-1]
        moveOk = checkPos(nextPos, tab)
        if not moveOk:
            if posi != 0 or dir == dirNorm[0]:
                posi += 1
            dir = dirNorm[posi]
    return [nextPos, dir]

def main():
    global bCasseur
    res = ''
    bContinue = True
    start, end, tabG = [], [], []
    teleport = []

    dirToDisplay = []

    l, c = [int(i) for i in input().split()]
    print('l:{} c:{}'.format(l, c), file=sys.stderr, flush=True)
    for i in range(l):
        row = input()
        if '@' in row:
            start = [i, row.index('@')]
        if '$' in row:
            end = [i, row.index('$')]
        if 'T' in row:
            firstIdx = row.index('T')
            lastIdx = row.rindex('T')
            if firstIdx != lastIdx:
                teleport = [[i, firstIdx], [i, lastIdx]]
            else:
                teleport.append([i, firstIdx])
        tabG.append(row)

    '''
    l, c = 5, 5
    ttab = ['#####', '#@  #', '#   #', '#  $#', '#####']

    l, c = 10, 10
    # ttab = ['##########', '#    I   #', '#        #', '#       $#', '#       @#',  '#        #', '#       I#', '#        #', '#        #', '##########']
    ttab = ['##########', '# @      #', '# B      #', '#XXX     #', '# B      #', '#    BXX$#', '#XXXXXXXX#', '#        #', '#        #', '##########']
    for i, row in list(enumerate(ttab)):
        if '@' in row:
            start = [i, row.index('@')]
        if '$' in row:
            end = [i, row.index('$')]
        tabG.append(row)
    '''
    print('start:{} end:{}'.format(start, end), file=sys.stderr, flush=True)

    pos = start.copy()
    dirR = dirNorm[0]
    cptStopLoop = 0
    while(bContinue):
        res = computeNextPos(pos, tabG, dirR)
        pos = res[0]
        newDir = res[1]
        if pos == end:
            bContinue = False
        # print(newDir)
        dirToDisplay.append(newDir)
        dirR = newDir

        symbTab = tabG[pos[0]][pos[1]]
        if not symbTab == ' ':
            if symbTab in tabDirInit:
                idxPos = tabDirInit.index(symbTab)
                dirR = dirNorm[idxPos]
            if symbTab == 'I':
                dirNorm.reverse()
                tabDirInit.reverse()
            elif symbTab == 'B':
                bIntermed = not bCasseur
                bCasseur = bIntermed
            elif symbTab == 'T':
                if [pos[0], pos[1]] == teleport[0]:
                    pos = teleport[1]
                else:
                    pos = teleport[0]
        cptStopLoop += 1
        if cptStopLoop > 2* l * c:
            bContinue = False
            nbrElemts = len(dirToDisplay)
            for i in range(nbrElemts):
                dirToDisplay.pop()
            dirToDisplay.append('LOOP')

    for disp in dirToDisplay:
        print(disp)

if __name__ == '__main__':
    main()
