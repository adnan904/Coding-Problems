# Given head to a Linked list, checks whether it is a palindrome or not
# Does it without reversing the whole LL
# Initially we maintain two pointers slow and fast pointing to the head node.
# Fast moves twice as fast as the slow one to find the middle node of the LL
# Slow pointer will point to the node after the middle. For 6 noded LL -> 4th node, for 7 noded -> 5th
# The nodes beyond slow pointer need to be reversed. The fast pointer points to the head
# Until slow is none we compare the two pointer, if values don't match anywhere Not a palindrome. Else a Palindrome

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_ll(elements_list: list) -> ListNode:
    head = ListNode(val=elements_list[0])
    prev = head
    for i in range(1, len(elements_list)):
        node = ListNode(elements_list[i])
        prev.next = node
        prev = node
    return head


def print_ll(head: ListNode) -> str:
    if head is None:
        return "Empty LL"

    ll_string = ""

    while head.next is not None:
        ll_string += f"{head.val} -> "
        head = head.next
    ll_string += str(head.val)
    return ll_string


def reverse_ll(head):
    prev = None
    dummy_head = head
    while dummy_head:
        temp = dummy_head.next
        dummy_head.next = prev
        prev = dummy_head
        dummy_head = temp
    return prev


if __name__ == '__main__':
    elements_list = [1, 2, 3, 4, 3, 2, 1]
    head = create_ll(elements_list)
    print(print_ll(head))

    slow = head
    fast = head

    # For even LL fast at end would be None and slow would point to the right place from where to reverse and compare
    # 1, 2, 2, 1 : slow would be at index 2(starting from 0)
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    # For odd LL, fast would be pointing to the last node and slow to the exact middle node
    # We move slow one step ahead to only make the necessary comparisons ( Middle number need not be considered)
    # 1, 2, 3, 2 , 1: slow would be pointing to 3 , so we move it ahead to point ot 2
    if fast is not None and fast.next is None:
        slow = slow.next

    # reverse the rightmost part of the LL beyond the middle element
    # 1, 2, 3, 2 , 1 -> 1, 2, 3, 1, 2
    # fast points to the first 1, and slow to the 2nd 1
    fast = head
    slow = reverse_ll(slow)

    # compare until slow is not None. If any comparison value not equal then not a  palindrome
    flag = True
    while slow:
        if slow.val != fast.val:
            print("Not a Palindrome")
            flag = False
            break
        fast = fast.next
        slow = slow.next

    if flag:
        print("Palindrome")
