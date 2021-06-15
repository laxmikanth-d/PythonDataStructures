class Node:

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    

class CircularLinkedList:

    CCLResult = ''

    def __init__(self):
        self.head = None


    def add(self, new_data: Node = None):

        if not self.head:
            self.head = Node(new_data.data)
            self.head.next = self.head
        else:
            node: Node = new_data
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next

            current_node.next = new_data
            new_data.next = self.head 


    def display(self, current_node: Node = None):

        current_node: Node = self.head

        while current_node.next != self.head:
            self.CCLResult += '{} ->'.format(current_node.data)
            current_node = current_node.next
        
        self.CCLResult += '{}'.format(current_node.data)
        return self.CCLResult


Cll = CircularLinkedList()

Cll.add(Node("data1"))
Cll.add(Node("data2"))
Cll.add(Node("data3"))
Cll.add(Node("data4"))
Cll.add(Node("data5"))

print(Cll.display())

print(Cll.display(None, False))

