# https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list


def insertNodeAtHead(llist, data):
    new = SinglyLinkedListNode(data)
    new.next =llist
    return new