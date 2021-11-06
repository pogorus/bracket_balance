class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return  self.stack[-1]

    def size(self):
        return  len(self.stack)


def bracket_balance(brackets):
    if len(brackets) % 2 != 0:
        return 'Несбалансированно'
    for bracket in brackets:
        if bracket in '([{':
            stack.push(bracket)
        else:
            if stack.is_empty():
                return 'Несбалансированно'
            else:
                if stack.peek() == '(' and bracket == ')':
                    stack.pop()
                elif stack.peek() == '[' and bracket == ']':
                    stack.pop()
                elif stack.peek() == '{' and bracket == '}':
                    stack.pop()
                else:
                    return 'Несбалансированно'
    if not stack.is_empty():
        return 'Несбалансированно'
    else:
        return 'Сбалансированно'

stack = Stack()

print(bracket_balance('(((([{}]))))'))
print(bracket_balance('[([])((([[[]]])))]{()}'))
print(bracket_balance('{{[()]}}'))

print(bracket_balance('}{}'))
print(bracket_balance('{{[(])]}}'))
print(bracket_balance('[[{())}]'))


