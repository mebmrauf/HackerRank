# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse

def reversePrint(llist):
    if llist != None:
        reversePrint(llist.next)
        print(llist.data)