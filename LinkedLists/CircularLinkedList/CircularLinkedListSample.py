import CircularLinkedList as CLL

circular_ll = CLL.CircularLinkedList()

a = CLL.Node("a")
b = CLL.Node("b")
c = CLL.Node("c")
d = CLL.Node("d")

a.next = b 
b.next = c
c.next = d
d.next = a

circular_ll.head = a

circular_ll.print_list()
