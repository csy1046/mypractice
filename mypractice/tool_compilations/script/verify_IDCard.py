Wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
Y = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
def verify(ID=None):
    if not ID:
        return '没有'
    if not len(ID) == 18:
        return False
    Ai = list(ID[0:18])
    S = list(map(lambda x,y:int(x)*int(y),Wi, Ai))
    S = sum(S)
    verify = Y[(S % 11)]
    print(verify)
    return verify == ID[-1].upper()


def fake(ID=None):
    #id_num = input('You id: ')
    ids = [int(c) for c in ID]
    Wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    S = sum([x * y for x in ids for y in Wi]) % 11
    Y = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
    if Y[int(S)] != ID[-1]:
        print('You are not human')
    else:
        print('Nearly human')


if __name__ == '__main__':
    print(verify('220106199212260222'))
    print(fake('220106199212260222'))