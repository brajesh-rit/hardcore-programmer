"""
https://www.geeksforgeeks.org/design-and-implement-special-stack-data-structure/
https://www.geeksforgeeks.org/design-and-implement-special-stack-data-structure/
Design a data-structure SpecialStack that supports all the stack operations like push(), pop(), isEmpty(), isFull()
and an additional operation getMin() which should return minimum element from the SpecialStack.
Your task is to complete all the functions, using stack data-Structure.


Example 1:

Input:
Stack: 18 19 29 15 16
Output: 15
Explanation:
The minimum element of the stack is 15.

Your Task:
Since this is a function problem, you don't need to take inputs. You just have to complete 5 functions,
push() which takes the stack and an integer x as input and pushes it into the stack;
pop() which takes the stack as input and pops out the topmost element from the stack;
isEmpty() which takes the stack as input and returns true/false depending upon whether the stack is empty or not;
isFull() which takes the stack and the size of the stack as input and returns true/false
        depending upon whether the stack is full or not (depending upon the given size);
getMin() which takes the stack as input and returns the minimum element of the stack.
Note: The output of the code will be the value returned by getMin() function.

"""
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
            return
        else:
            return self.array[self.top]

# A class that supports all the stack operations and one additional operation getMin() that returns the
# minimum element from stack at any time.  This class inherits from the stack class and uses an
# auxiliary stack that holds minimum elements

class SpecialStack(stack):
    def __init__(self):
        super().__init__()
        self.Min = stack()

    def push(self, x):

        if self.isEmpty():
            super().push(x)
            self.Min.push(x)
        else:
            super().push(x)
            y = self.Min.peek()
            if x <= y:             # why '=' ? because two equal element is min then both an entry in special stack
                self.Min.push(x)


    def pop(self):
        x = super().pop()
        if x == self.Min.peek():
            self.Min.pop()
        return x

    # function should return minimum element from the stack
    def getmin(self):
        x = self.Min.peek()
        return x

ss = SpecialStack()
ss.push(18)
ss.push(19)
ss.push(29)
print(ss.getmin())
ss.push(15)
print(ss.getmin())
ss.push(15)
print(ss.getmin())
ss.pop()
ss.push(5)
print(ss.getmin())
ss.pop()
print(ss.getmin())  # 15
ss.pop()
print(ss.getmin()) # 18
ss.pop()           #29
print(ss.getmin()) #18
ss.pop()           #19
print(ss.getmin()) #18
ss.pop()           #18
print(ss.getmin()) #18
ss.pop()
print(ss.getmin()) # empty