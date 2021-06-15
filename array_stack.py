class ArrayStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def pop(self):

        if self.is_empty():
            raise Empty('Stack is empty')

        return self._data.pop()

    def display(self):
        print(self._data)


class Empty(Exception):
    pass


AS = ArrayStack()
AS.push(1)
# AS.push(2)
# AS.push(3)
# AS.push(4)
# AS.push(5)

AS.pop()
AS.pop()

AS.display()
