'''

Reverse Polish Notation

Michael Streyle

'''



class Stack:
    '''Stack implementation'''
    def __init__(self):
        self._items = []
    def is_empty(self):
        return self._items == []
    def size(self):
        return len(self._items)
    def push(self, new_item):
        self._items.append(new_item)
    def pop(self):
        return self._items.pop()
    def peek(self):
        return self._items[-1]


class StackError(Exception):
    '''Stack errors'''
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class TokenError(Exception):
    '''Token errors'''
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

def rev_string_simple(my_str):
    '''Reverse characters in a string without using a stack'''
    my_str = my_str[::-1]
    return my_str

def rev_string_stack(my_str):
    '''Reverse characters in a string using a stack'''
    l = len(my_str)
    my_stack = Stack()
    for i in range(0,l,1): 
        Stack.push(my_stack,my_str[i]) 
    my_str = ''
    for i in range(0,l,1): 
        my_str += Stack.pop(my_stack)
    return my_str

def par_checker(line):
    '''Textbook implementation'''
    s = Stack()
    balanced = True
    i = 0
    while i < len(line) and balanced:
        symbol = line[i]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        i = i + 1
    if balanced and s.is_empty():
        return True
    else:
        return False

def par_checker_file(filename):
    '''Check expressions in the file'''
    with open(filename, 'r') as name:
        for line in name:
            tf = par_checker(line.strip('\n'))
            if tf == True:
                print('{} is balanced'.format(line.strip()))
            else:
                print('{} is NOT balanced'.format(line.strip()))


def base_converter(dec_num, base):
    '''Convert any decimal number to any base'''
    hex_digits = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    remstack = Stack()
    new_str = ""
    bas = [2, 8, 16]
    if base not in bas:
        return ValueError('Base must be 2, 8, or 16')
    if dec_num >= base and base!=16:
        while dec_num > 0:
            rem = dec_num%base
            remstack.push(rem)
            dec_num = dec_num//base
        while not remstack.is_empty():
            new_str = new_str + str(remstack.pop())
    elif dec_num>=base:
        rem = dec_num%base
        remstack.push(rem)
        dec_num = dec_num//base
        new_str = str(dec_num) + hex_digits[remstack.pop()]
    elif dec_num < base:
        new_str = hex_digits[dec_num]
    else:
        raise ValueError
    return new_str

def rpn_calc(postfix_expr):
    '''Evaluate a postfix expression'''
    operandStack = Stack()
    tokenList = postfix_expr.split()
    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            try:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
            except:
                if token in "abcdefghijklmnopqrstuvwxyz":
                    raise TokenError("Unknown token: {}".format(token))
                else:
                    raise StackError('Stack is empty')
            result = do_math(token, operand1, operand2)
            operandStack.push(result)
    if operandStack.size() == 1:
        return operandStack.pop()
    else:
        raise StackError('Stack is not empty')


def do_math(op, op1, op2):
    if op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    else:
        raise TokenError("Unknown token: {}".format(op))
