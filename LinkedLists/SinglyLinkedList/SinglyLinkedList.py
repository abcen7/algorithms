class SinglyLinkedList:
    head = None

    class Node:
        element = None
        next_node = None

        def __init__(self, element, next_node=None):
            self.element = element
            self.next_node = next_node

    def append(self, element):
        if self.head is None:
            self.head = self.Node(element)
            return element
        node = self.head

        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(element)

    def out(self):
        node = self.head

        while node.next_node:
            print(node.element)
            node = node.next_node
        print(node.element)

    def __len__(self) -> int:
        counter = 0
        node = self.head
        while node.next_node:
            counter += 1
            node = node.next_node
        counter += 1
        return counter

    def get_tail(self):
        node = self.head
        while node.next_node:
            node = node.next_node
        return node.element

    def insert_at(self, index, element):
        i = 0
        node = self.head
        previous_node = self.head

        while i < index:
            previous_node = node
            node = node.next_node
            i += 1

        previous_node.next_node = self.Node(element, next_node=node)

        return element

    def assign(self, index, element):
        node = self.head
        i = 0

        while i < index:
            node = node.next_node
            i += 1

        node.element = element

    def remove_at(self, index):
        if index == 0:
            self.head = self.head.next_node

        node = self.head
        i = 0
        previous_node = node
        while i < index:
            previous_node = node
            node = node.next_node
            i += 1

        previous_node.next_node = node.next_node
        element = node.element

        del node
        return element


sll = SinglyLinkedList()
sll.append(10)
sll.append(141)
sll.append(1324)
sll.append(142341)
sll.remove_at(0)
sll.assign(1, 2222222)
sll.append(11)
print(f'LENGTH OF SLL >> {len(sll)}')
sll.out()
