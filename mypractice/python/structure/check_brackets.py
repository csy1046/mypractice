from stack import Stack

left_b = '{[('
right_b = '}])'
def brackets(bracket):
    stack = Stack()
    flag = False
    for i in bracket:
        if i in left_b:
            stack.push(i)
        elif i in right_b:
            if not stack.isEmpty() and check_brackets(stack.peek(), i):
                stack.pop()
                flag = True
            else:
                flag = False
                break
    return flag

def check_brackets(left, right):
        if left_b.index(left) == right_b.index(right):
            return True
        return False
if __name__ == '__main__':
    print(brackets('())]'))
