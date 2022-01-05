# Given two link lists with each element within the range of 0-9.
# The head of the lists point to the least significant digit
# We don't know the number of elements in a Linked List

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


def add_two_lls(l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0
    result = ListNode()
    prev = result

    while l1 or l2 or carry:
        summ = 0
        if l1:
            summ += l1.val
            l1 = l1.next
        if l2:
            summ += l2.val
            l2 = l2.next
        if carry:
            summ += carry
        carry = summ // 10
        digit = summ % 10
        node = ListNode(val=digit)
        prev.next = node
        prev = node

    return result.next


def reverse_ll(ll: ListNode) -> ListNode:
    prev = None
    while ll:
        temp = ll.next
        ll.next = prev
        prev = ll
        ll = temp
    return prev


def calc_length(ll:ListNode) -> int:
    """
    Given a LL calculates how many nodes are there in the LL
    :param ll: head of a Linked list
    :return: length of the LL
    """
    count = 0
    while ll:
        count += 1
        ll = ll.next
    return count


def add_two_LLs_MSB(l1: ListNode, l2: ListNode) -> ListNode:
    '''
    # We first add the digits at the consecutive positions in the LL's LSB-wise without caring if the sum is 2 digits
    # We store the sums of consecutive digits in a new LL but we add new nodes before the head of the LL and make the
    # new node as the head then. This was this summed LL will have the LSB as the head at the end and then worrying
    # about the carry will become easy
    '''
    # Counting the length of each LL
    l1_length = calc_length(l1)
    l2_length = calc_length(l2)
    dummy_head = ListNode()
    if l1_length != l2_length:
        while l1_length != l2_length:
            node = ListNode()
            if l2_length > l1_length:
                dummy_head.val = l2.val
                l2 = l2.next
                l2_length -= 1
            else:
                dummy_head.val = l1.val
                l1 = l1.next
                l1_length -= 1
            node.next = dummy_head
            dummy_head = node

    while l1 and l2:
        summ = l1.val + l2.val
        l1 = l1.next
        l2 = l2.next
        node = ListNode()
        dummy_head.val = summ
        node.next = dummy_head
        dummy_head = node

    summed_ll_lsb = dummy_head.next

    # Taking care of the carry now and creating a new LL and adding new nodes towards the front
    dummy_head = ListNode()
    carry = 0
    while summed_ll_lsb:
        summ = summed_ll_lsb.val + carry
        digit = summ % 10
        carry = summ // 10
        dummy_head.val = digit
        node = ListNode()
        node.next = dummy_head
        dummy_head = node
        summed_ll_lsb = summed_ll_lsb.next
    if carry:
        dummy_head.val = carry
        node = ListNode()
        node.next = dummy_head
        dummy_head = node

    return dummy_head.next


if __name__ == '__main__':
    l1 = [5,6,4]

    l2 = [9, 9, 9, 9]
    l1_head = create_ll(l1)
    l2_head = create_ll(l2)
    result = add_two_lls(l1_head, l2_head)
    print(print_ll(l1_head))
    print(print_ll(l2_head))
    print(f"Head as LSB: {print_ll(result)}")

    # If the head is pointing to the MSB then we would need to reverse the LL's first
    # l1_reverse = reverse_ll(l1_head)
    # l2_reverse = reverse_ll(l2_head)
    # result = add_two_lls(l1_reverse, l2_reverse)
    # result = reverse_ll(result)
    # print(f"Head as MSB: {print_ll(result)}")

    # Adding two LL'S with Head point to MSB without reversing
    result = add_two_LLs_MSB(l1_head, l2_head)
    print(f"Head as MSB without reversing: {print_ll(result)}")
