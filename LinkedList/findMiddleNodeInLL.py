# Suppose we have a standard linked list. 
# Construct an in-place (without extra memory) algorithm 
# thats able to find the middle node!
# ================================================
# Using Bruteforce method means iterating through whole linked list finding the size
# and again iterating throgh the linked list upto middle.
# This will have O(N**2) time complexity.

# Time Complexity: O(N), 
# where N is the number of nodes in the given list.

# Space Complexity: O(1), the space used by slow and fast pointers.

class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

def findMiddleInLinkedList(a):
    slowPointer = a
    fastPointer = a
    while fastPointer and slowPointer:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
    return slowPointer.value

if __name__ == '__main__':
    a, a.next, a.next.next, a.next.next.next, a.next.next.next.next, a.next.next.next.next.next= ListNode(2), ListNode(14), ListNode(3),ListNode(6), ListNode(44), ListNode(23)
    middleNum = findMiddleInLinkedList(a)
    print(f"Middle number is: {middleNum}")