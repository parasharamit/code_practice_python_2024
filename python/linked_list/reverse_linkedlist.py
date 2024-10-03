
def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    if head and head.next and head.next.next:
        p = head
        c = head.next
        f = head.next.next

    head.next = None

    while f.next:
        p.next = head
        head = p
        p = c
        c = f
        f = f.next
    p.next = head
    c.next = head
    head = c

    return head