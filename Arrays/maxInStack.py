# The aim is to design an algorithm that can return 
# the maximum item of a stack in O(1) running time complexity. 
# We can use O(N) extra memory!

# Hint: we can use another stack to track the max item

# ======================================================
class MaxStack:
    def __init__(self):
        self.mainStack = []
        self.maxStack = []

    def push(self, data):
        self.mainStack.append(data)
        if (len(self.mainStack) == 1):
            self.maxStack.append(data)
            return
        if data>self.maxStack[-1]:
            self.maxStack.append(data)
        else:
            self.maxStack.append(self.maxStack[-1])
        return
    
    def pop(self):
        self.maxStack.pop()
        return self.mainStack.pop()

    def get_max(self):
        return self.maxStack.pop()

if __name__ == '__main__':
    max_stack = MaxStack()
    max_stack.push(21)
    max_stack.push(5)
    max_stack.push(12)
    max_stack.push(511)
    max_stack.push(25)
    max_stack.push(76)

    maxItem = max_stack.get_max()
    print(f"Max item in stack is: {maxItem}")




