class Node():

    def __init__(self, next=None, data=None):
        self.data = data
        self.next = next


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
            


if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(None,0)
    end = llist.head

    for i in range(1,11):
        end.next = Node(None,i)
        end = end.next
    
    llist.print_linked_list()

    llist.reverse_linear()

    llist.print_linked_list()
        