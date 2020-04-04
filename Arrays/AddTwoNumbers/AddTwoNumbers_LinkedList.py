
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Define variables
        resultedList = ListNode(0)
        tmpList = resultedList
        carry = 0
        sum = 0
        print("adding the numbers")
        # Loop through the list while l1, l2 or carry exists
        while l1 or l2 or carry:
            # check if l1 node is not null then add its value to sum
            if l1:
                sum += l1.val
                l1 = l1.next
            # check if l1 node is not null then add its value to sum
            if l2:
                sum += l2.val
                l2 = l2.next
            # Add carry to the sum
            sum += carry
            # replace carry value with the new carry value (i.e quotient after diving sum by 10).
            carry = sum // 10
            # save reminder in temporary Listnode 
            tmpList.next = ListNode(sum % 10)
            # reset sum value
            sum = 0
            tmpList = tmpList.next
        return resultedList.next

if __name__ == '__main__':
    solution = Solution()
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    result = solution.addTwoNumbers(a, b)
    # print (result.val, result.next.val, result.next.next.val)
    print (f"{result.val} -> {result.next.val} -> {result.next.next.val}")





             
            
        