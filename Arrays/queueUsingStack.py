# The aim is to design a queue abstract data type with the help of stacks.
# Queue: FIFO, Stack: LIFO

# Implemented using single stack with recursion.
class Queue:
    def __init__(self):
        self.mainStack = []

    # add data to stack
    def enqueue(self, data):
        self.mainStack.append(data)

    # get the first item (FIFO) from queue
    def dequeue(self):
        #  if stack has only one item remaining then that item is the first inserted item
        #  and that item we want to pop to make it queue.
        if len(self.mainStack) == 1:
            return self.mainStack.pop()
        item = self.mainStack.pop()
        # call function recursively
        dequedItem = self.dequeue()
        # after poping the first inserted item, 
        # now append all the remaining items back to stack
        self.mainStack.append(item)

        return dequedItem

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(12)
    queue.enqueue(9)
    dequedItem = queue.dequeue()
    print(f"Dequeued Item is: {dequedItem}")
    queue.enqueue(22)
    queue.enqueue(112)
    queue.enqueue(5)

    dequedItem = queue.dequeue()
    print(f"Dequeued Item is: {dequedItem}")
