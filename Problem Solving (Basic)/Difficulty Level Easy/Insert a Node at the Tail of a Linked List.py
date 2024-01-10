# https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list

def insertNodeAtTail(head, data):
    new = SinglyLinkedListNode(data)
    if head == None:
        return new
    temp = head
    while temp.next:
        temp=temp.next
    temp.next = new
    return head