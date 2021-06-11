class Node:

    def __init__(self, data, previous = None, next = None):
        self.previous = previous
        self.data = data
        self.next = next


class DoubleLinkedList:

    result: any = ''

    def __init__(self):
        self.node = Node(None)

    
    def add(self, new_node: Node, node: Node = None):

        if node == None:
            node = self.node
        
        # first node 
        if node.previous == None and node.data == None and node.next == None:
            node.data = new_node.data        
        elif node.previous == None and node.data != None and node.next == None:
            node.next = new_node
            new_node.previous = node
        elif node.previous == None and node.data != None and node.next != None:
            self.add(new_node, node.next)
        elif node.previous != None and node.next != None:
            self.add(new_node, node.next)
        # Last node
        elif node.previous != None and node.next == None:  
            node.next = new_node
            new_node.previous = node


    def display(self, node: Node = None):

        if node == None:
            node = self.node

        if node.previous == None and node.data == None and node.next == None:
            DoubleLinkedList.result += 'Double Linked List is empty'
            return DoubleLinkedList.result
        elif node.previous == None and node.data != None and node.next == None:
            DoubleLinkedList.result += '{}'.format(node.data)
            return DoubleLinkedList.result        
        elif node.data != None and node.next != None:
            DoubleLinkedList.result += '{} -> '.format(node.data)
            self.display(node.next)
            return DoubleLinkedList.result
        elif node.previous != None and node.data != None and node.next == None:
            DoubleLinkedList.result += '{} -> '.format(node.data)            
            return DoubleLinkedList.result
        

dll = DoubleLinkedList()

# import pdb;
# pdb.set_trace()

dll.add(Node(data="data1"))
dll.add(Node(data="data2"))
dll.add(Node(data="data3"))
dll.add(Node(data="data4"))
dll.add(Node(data="data5"))
dll.add(Node(data="data6"))
dll.add(Node(data="data7"))
dll.add(Node(data="data8"))

print(dll.display())
