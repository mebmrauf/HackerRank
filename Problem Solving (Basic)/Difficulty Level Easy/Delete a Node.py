# https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list

def deleteNode(llist, position):
    temp = llist
    count = 0
    if position == 0:
        llist = llist.next
    else:
        while temp:
            if (count == position-1) and (temp.next != None):
                temp.next = temp.next.next
            count+=1
            temp = temp.next
    return llist