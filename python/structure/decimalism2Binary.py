from stack import Stack

def decimalism2Binary(deci):
    stack_dec = Stack()
    while deci > 0:
        remainder = deci % 2
        stack_dec.push(remainder)
        deci = deci // 2

    binary_string = ''
    for i in range(stack_dec.size() -1, -1, -1):
        binary_string += str(stack_dec.list()[i]) 
    return binary_string
        
if __name__ == '__main__':
    print(decimalism2Binary(233))
