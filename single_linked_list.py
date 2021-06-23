class Node:    

    def __init__(self, data, next = None):
        self.data = data
        self.next = next        

class LinkedList:

    result: any = ''

    def __init__(self):
        self.node = Node(None)  
    
    def add(self, new_node: Node, node: Node = None):
        
        # For first iteration
        if node == None:
            node = self.node

        # First Node
        if node.data == None and node.next == None:
            node.data = new_node.data
            node.next = None        
        # Intermediate node
        elif node.next != None:
            self.add(new_node, node.next)
        # Last Node
        else:            
            node.next = new_node

    
    def display(self, node: Node = None):
        
        if node == None:
            node = self.node
        
        if node.next != None:
            LinkedList.result += ("{} -> ".format(node.data))
            self.display(node.next)
        else:
            LinkedList.result += ("{} -> ".format(node.data))
                
        return LinkedList.result
        
ll = LinkedList()
ll.add(Node("data1"))
ll.add(Node("data2"))
ll.add(Node("data3"))
ll.add(Node("data4"))
ll.add(Node("data5"))
ll.add(Node("data6"))

print(ll.display(None))
