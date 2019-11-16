'''
Reverse Polish Notation
Michael Streyle

'''
#!/usr/bin/env python3


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



def postfix_eval(postfix_expr: str) -> int:
    '''Evaluate a postfix expression'''
    operandStack = Stack()
    tokenList = postfix_expr.split()
    for token in tokenList:
        if token in "abcdefghijklmnopqrstuvwxyz":
            raise TokenError("Unknown token: {}".format(token))
        elif token == '=' and operandStack.is_empty():
            raise StackError('Stack is empty')
        elif token == '=':
            pass
        elif token.isnumeric():
            operandStack.push(int(token))
        else:
            try:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                result = do_math(token, operand1, operand2)
                operandStack.push(result)
            except:
                continue
    if operandStack.size() == 1:
        return operandStack.pop()
    else:
        raise StackError('Stack is not empty')


def do_math(op: str, op1: int, op2: int) -> int:
    if op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "*":
        return op1 * op2
    elif op == "/":
        try:
            return op1 / op2
        except:
            raise ZeroDivisionError('division by zero')
            
    elif op == "//":
        try:
            return op1 // op2
        except:
            raise ZeroDivisionError('integer division or modulo by zero')
        
    elif op == "**":
        return op1 ** op2
    elif op == "%":
        try:
            return op1 % op2
        except:
            raise ZeroDivisionError('integer division or modulo by zero')
    else:
        raise TokenError("Unknown operation: {}".format(op))


def rpn_calc(filename: str) -> int:
    with open(filename, 'r') as filename:
        count = 0
        for line in filename:
            try:
                x = postfix_eval(line.strip('\n'))
                count += x
            except:
                pass
    return count


def main():
    try:
        with open('rpn_input_1.txt') as filename:
            for line in filename:
                try:
                    print("%-75s %s" % (line.strip('\n'), postfix_eval(line)))
                except Exception as e:
                    print("%-75s %s" % (line.strip('\n'), 'Error: {}'.format(e)))
        rpn_calc('rpn_input_1.txt')
    except FileNotFoundError:
        print("File does not exist")
    checksum = rpn_calc('rpn_input_1.txt')
    print('Checksum is %.2f' % checksum)




if __name__ == '__main__':
    main()