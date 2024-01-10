# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list

def insertNodeAtPosition(llist, data, position):
    temp = llist
    new_node = SinglyLinkedListNode(data)
    count = 0
    prev_node = None
    if position == 0:
        new_node.next = llist
        llist = new_node
    else:
        while temp:
            if count == position:
                new_node.next = temp
                prev_node.next = new_node
                break
            prev_node = temp
            temp = temp.next
            count += 1
    return llist