
class Empty:
    pass

class CircularQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self.data = [None]*CircularQueue.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self)    :

        if self.size == 0:
            raise Empty('Queue is Empty')
        return self.data[self.front]

    def dequeue(self):
        
        if self.is_empty():
            raise Empty('Queue is Empty')
        
        answer = self.data[self.front]
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1

        return answer

    def enqueue(self, e):        

        if self.size == len(self.data):
            self.resize(2*len(self.data))
        avail = (self.front + self.size) % len(self.data)
        self.data[avail] = e
        self.size += 1       
        


    def resize(self, cap):
        old = self.data

        self.data = [None]*cap
        walk = self.front

        for k in range(self.size):
            self._data[k] = old[walk]
            walk = (walk + 1)% len(old)
        
        self.front = 0


    def read_queue(self):
        
        read_pointer = self.front

        while read_pointer < self.front + self.size:
            print(self.data[read_pointer])
            read_pointer += 1

  

cq = CircularQueue()
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
cq.enqueue(6)

cq.read_queue()

cq.dequeue()

cq.read_queue()