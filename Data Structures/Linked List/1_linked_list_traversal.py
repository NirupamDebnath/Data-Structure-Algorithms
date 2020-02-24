class Node():

    def __init__(self, next=None, data=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"data -> {self.data}"


class LinkedList():

    def __init__(self):
        self.head = None
        
    def print_linked_list(self):
        print()
        start = self.head
        while start:
            print(f"{start.data} -> ",end = "")
            start = start.next
        print('None')

    def reverse_linear(self):
        prev = None
        curr = self.head

        # import pdb; pdb.set_trace()
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        self.head = prev

    def add_number(self, head, curr, num):
        if curr.next == None:
            curr.data += num
            carry, curr.data = divmod(curr.data,10)
            return carry,head
        else:
            carry, head= self.add_number(head, curr.next, num)
            if carry != 0:
                curr.data += carry
                carry, curr.data = divmod(curr.data,10)
                if head != curr:
                    return carry, head
                else:
                    while carry != 0:
                        carry, data = divmod(carry,10)
                        head = Node(head,data)
                    return carry, head
                         
            return 0, head

# if __name__ == "__main__":
#     llist = LinkedList()
#     llist.head = Node(None,0)
#     end = llist.head

#     for i in range(1,11):
#         end.next = Node(None,i)
#         end = end.next
    
#     llist.print_linked_list()

#     llist.reverse_linear()

#     llist.print_linked_list()

"""
Adding a number assuming the linked list is a number
"""
if __name__ == "__main__":
    llist = LinkedList()
    
    llist.head = Node(None, 9)
    llist.head.next = Node(None, 9)
    llist.head.next.next = Node(None, 3)

    llist.print_linked_list()

    _, llist.head = llist.add_number(llist.head , llist.head, 99999999)

    llist.print_linked_list()