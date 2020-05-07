# Construct an in-place algorithm to reverse a linked list!
# ==============================================

# Time complexity: O(N)
# Space complexity: O(1)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseLinkedList(a:ListNode)->ListNode:
    # here "a" is pointing to head
    currentNode = a
    prevNode = None
    nextNode = None

    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = prevNode # here reference is reveresed
        prevNode = currentNode
        currentNode = nextNode
    
    a = prevNode
    return a

if __name__ == '__main__':
    a, a.next, a.next.next, a.next.next.next, a.next.next.next.next, a.next.next.next.next.next= ListNode(2), ListNode(4), ListNode(3),ListNode(6), ListNode(7), ListNode(23)
    reveresedLL = reverseLinkedList(a)
    print(f"{reveresedLL.val}->{reveresedLL.next.val}->",
        f"{reveresedLL.next.next.val}->{reveresedLL.next.next.next.val}->{reveresedLL.next.next.next.next.val}",
        f"->{reveresedLL.next.next.next.next.next.val}")
