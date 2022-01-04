# Given a list of elements and 'n', creates a linked list and then deletes the nth element from the back
# We don't know the number of elements in a Linked List
# Hence we maintain 2 pointers, slow and fast. The fast pointer will be n steps ahead of slow
# Once fast reaches the last element, slow will be n elements behind and we just need to update the slow

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


def remove_nth(head: ListNode, n: int) -> ListNode:
    fast = head
    slow = head

    for _ in range(n):
        fast = fast.next

    if fast is None:
        return head.next

    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return head


if __name__ == '__main__':
    elements_list = [1, 2, 3, 4, 5]
    n = 2
    head = create_ll(elements_list)
    print(f"Before: {print_ll(head)}")
    head = remove_nth(head, n)
    print(f"After: {print_ll(head)}")
