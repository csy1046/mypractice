import time
t0=time.time()
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.available=[]
        self.value=0

def rowNum(p,sudoku):
    row=set(sudoku[p.y*4:(p.y+1)*4])
    row.remove(0)
    return row #set type  

def colNum(p,sudoku):
    col=[]
    length=len(sudoku)
    for i in range(p.x,length,4):
        col.append(sudoku[i])
    col=set(col)
    col.remove(0)
    return col #set type  

def blockNum(p,sudoku):
    block_x=p.x//2
    block_y=p.y//2
    block=[]
    start=block_y*2*4+block_x*2
    for i in range(start,start+2):
        block.append(sudoku[i])
    for i in range(start+4,start+4+2):
        block.append(sudoku[i])
    block=set(block)
    block.remove(0)
    return block #set type  

def initPoint(sudoku):
    pointList=[]
    length=len(sudoku)
    for i in range(length):
        if sudoku[i]==0:
            p=point(i%4,i//4)
            for j in range(1,5):
                if j not in rowNum(p,sudoku) and j not in colNum(p,sudoku) and j not in blockNum(p,sudoku):
                    p.available.append(j)
            pointList.append(p)
    return pointList


def tryInsert(p,sudoku):
    availNum=p.available
    for v in availNum:
        p.value=v
        if check(p,sudoku):
            sudoku[p.y*4+p.x]=p.value
            if len(pointList)<=0:
                t1=time.time()
                useTime=t1-t0
                showSudoku(sudoku)
                #print('\nuse Time: %f s'%(useTime))
                exit()
            p2=pointList.pop()
            tryInsert(p2,sudoku)
            sudoku[p2.y*4+p2.x]=0
            sudoku[p.y*4+p.x]=0
            p2.value=0
            pointList.append(p2)
        else:
            pass


def check(p,sudoku):
    if p.value==0:
        print('not assign value to point p!!')
        return False
    if p.value not in rowNum(p,sudoku) and p.value not in colNum(p,sudoku) and p.value not in blockNum(p,sudoku):
        return True
    else:
        return False

def showSudoku(sudoku):
    for j in range(4):
        for i in range(4):
            print('%d '%(sudoku[j*4+i]),end='')
        print('')

if __name__=='__main__':
    sudoku=[
        3,0,0,4,
        0,0,3,0,
        0,0,0,2,
        4,0,0,0
            ]
    pointList=initPoint(sudoku)
    showSudoku(sudoku)
    print('\n')
    print([{'available': i.available,
            'x': i.x,
            'y': i.y,
            'value': i.value} for i in pointList])
    p=pointList.pop()
    tryInsert(p,sudoku)

