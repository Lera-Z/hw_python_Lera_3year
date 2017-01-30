class Stack:
    def __init__(self):
        self.arr = []
    def push(self, item):
        self.arr.insert(0, item)
    def pop(self):
        if not self.isEmpty():
            elem = self.arr.pop(0)
            return elem
    def isEmpty(self):
        if len(self.arr) == 0:
            return True
        else:
            return False
    def peek(self):
        return self.arr[0]
        

# class Queue:
#     def __init__(self):
#         self.arr = []
#     def enqueue(self, i):
#         self.arr.append(i)
#     def dequeue(self):
#         elem = self.arr.pop(0)
#         return elem


# c = Stack()
# c.push(1)
# c.push(4)
# c.push(10)
# print(c.arr)
# c.pop()
# c.pop()
# c.pop()
# print(c.isEmpty())

class MyQueue:
    def __init__(self):
        self.add = Stack()
        self.main = Stack()
    def enqueue(self, i):
        self.add.push(i)

    def dequeue(self):
        while not self.add.isEmpty():
            up_elem = self.add.pop()
            self.main.push(up_elem)
        fst_elem = self.main.pop()
        while not self.main.isEmpty():
            up = self.main.pop()
            self.add.push(up)
        return fst_elem
    def peek(self):
         return self.add.arr[len(self.add.arr)-1]
    def isEmpty(self):
         if len(self.add.arr) == 0:
             return True
         else:
             return False



r = MyQueue()
r.enqueue(5)
r.enqueue(7)
r.enqueue(8)
r.enqueue(34)


r.dequeue()
r.dequeue()
r.dequeue()
r.dequeue()
r.enqueue(9)
r.enqueue(3)
r.enqueue(8)
#print(r.IsEmpty())
print(r.peek())