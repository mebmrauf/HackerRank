# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list

def printLinkedList(head):
    temp = head
    
    while temp:
        print(temp.data)
        temp = temp.next