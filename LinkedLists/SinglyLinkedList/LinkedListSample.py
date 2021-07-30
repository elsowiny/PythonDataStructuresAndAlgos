import LinkedList as LL
llist = LL.LinkedList(["a", "b", "c", "d", "e"])

# Traverse the linked list
print("Traversing the linked list")
print("LinkedList 1")
for node in llist:
    print(node.data)

# Adding to the front of the linked list
print("\nAdding to the list")
print("LinkedList 2")
llist2 = LL.LinkedList()
llist2.add_first(LL.Node("a"))
llist2.add_first(LL.Node("b"))
print(llist2)

# Adding to the end of the linked list
print("\nAdding to the end of the list")
print("LinkedList 3")
llist3 = LL.LinkedList()
llist3.add_last(LL.Node("x"))
llist3.add_last(LL.Node("y"))
llist3.add_last(LL.Node("z"))
print(llist3)

# Removing a node from the list
print("\nRemoving a node from the list")
print("LinkedList 4")
llist4 = LL.LinkedList(["a", "b", "c", "d", "e"])
print(llist4)
print('Removing letter b')
llist4.remove_node("b")
print(llist4)

