class bStack:

    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity

    def push(self,item):
        if len(self.stack) > self.capacity:
            raise Exception("Stack is full")

        self.stack.insert(0,item)

    def pop(self):
        return self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def show(self):
        print(self.stack)

    def getter(self):
        return self.stack

    def empty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)

    def isFull(self):
        return len(self.stack) == self.capacity

    def __str__(self):
        return " ".join(self.stack)

if __name__ == '__main__':
    s = bStack(2)
    s.push('a')
    s.push('b')
    s.show()
    print(s.__str__())
    s.push('c')