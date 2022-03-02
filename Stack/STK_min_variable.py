#https://www.geeksforgeeks.org/design-and-implement-special-stack-data-structure/
#Design a Data Structure SpecialStack that supports all the stack operations like push(), pop(), isEmpty(), isFull()
# and an additional operation getMin() which should return minimum element from the SpecialStack.
# All these operations of SpecialStack must be O(1). To implement SpecialStack,
# you should only use standard Stack data structure and no other data structure like arrays, list, . etc.
# Your task is to complete all these function's
# function should append an element on to the stack
class stack:
    def __init__(self):
        self.array = []
        self.top = -1
        self.max = 100

    def push(self, data):
        if self.isFull():
            print('Stack OverFlow')
            return
        else:
            self.top += 1
            self.array.append(data)

    # Function should pop an element from stack
    def pop(self):
        if self.isEmpty():
            print('Stack UnderFlow')
            return
        else:
            self.top -= 1
            return self.array.pop()

    def isFull(self):
        if self.top == self.max - 1:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def peek(self):
        if self.isEmpty():
            print('Stack is empty')
            exit(0)
        else:
            return self.array[self.top]

# A class that supports all the stack operations and one additional operation getMin() that returns the
# minimum element from stack at any time.  This class inherits from the stack class and uses an
# auxiliary stack that holds minimum elements

class SpecialStack(stack):
    def __init__(self):
        super().__init__()
        self.Min = None

    def push(self, x):

        if super().isEmpty():
            super().push(x)
            self.Min = x
        else:
            if x >= self.Min:
                super().push(x)
            else:
                super().push(x * 2 - self.Min)
                self.Min = x

    def pop(self):
        if super().peek() >= self.Min:
            val = super().pop()
        else:
            val = self.Min
            x = super().pop()
            self.Min = 2 * self.Min - x
        return val

    def peek(self):
        if super().peek() >= self.Min:
            val = super().peek()
        else:
            val = self.Min
        return val
    # function should return minimum element from the stack
    def getmin(self):
        return self.Min



ss = SpecialStack()
ss.push(18)
ss.push(19)
ss.push(29)
print(ss.getmin())
ss.push(15)
print(ss.getmin())
ss.push(15)
print(ss.getmin())
print(ss.pop())
ss.push(5)
print(ss.getmin())
print(ss.pop())
print(ss.getmin())  # 15
print(ss.pop())
print(ss.getmin()) # 18
print(ss.pop())          #29
print(ss.getmin()) #18
print(ss.pop())         #19
print(ss.getmin()) #18
print(ss.pop())          #18
print(ss.getmin()) #18
print(ss.pop())
print(ss.getmin()) # empty