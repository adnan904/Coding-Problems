# Implements the stack data structure and sort it in ascending order. The back of the list represents the top
# The top element will be the smallest
# The bottom element the largest
# So when we pop the entire stack the elements will be in ascending order
# Takes O(n^2) time as each element in the main stack will cause at max n pop's in the temp stack
class stack:
    def __init__(self, input: list=None):
        self.stack = []
        if input:
            self.stack = input

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        try:
            return self.stack.pop()
        except:
            print("Empty stack, cannot pop")

    def peek(self):
        try:
            return self.stack[len(self.stack) - 1]
        except:
            print("Empty stack, cannot peek")

    def is_empty(self):
        if len(self.stack):
            return False
        else:
            return True

    def print(self):
        print(self.stack)


if __name__ == '__main__':
    s = stack([11, 91, 93, 44, 55])
    s.print()
    temp_stack = stack()
    # We pop elements from the main stack until it is empty
    # For each element popped we check if the top elements of the temp stack are smaller than it.
    # If the top of temp stack is small we pop it and push it back into the main stack
    # This way we maintain that the temp stack has the highest elements at the bottom
    while not s.is_empty():
        k = s.pop()
        while not temp_stack.is_empty() and temp_stack.peek() < k:
            s.push(temp_stack.pop())
        temp_stack.push(k)
    temp_stack.print()
