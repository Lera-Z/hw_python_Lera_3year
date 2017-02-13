class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def empty(self):
        if self.head:
            return False
        return True

    def printList(self):
        node = self.head
        while node:
            print(node.data, end="->")
            node = node.next_node
        print()

    def push(self, data):
        node = Node(data, next_node=self.head)
        self.head = node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            node = self.head
            while node.next_node:
                node = node.next_node
            node.next_node = new_node
            
    def size(self):
        node = self.head
        length = 0
        while node:
            length += 1
            node = node.next_node
        return length
    
    def delete(self, value):
        node = self.head
        if self.head.data != value:
            while node.next_node:
                if node.next_node.data == value:
                    to_delete = node.next_node
                    node.next_node = to_delete.next_node
                    to_delete.next_node = None
                else:
                    node = node.next_node
        else:
            self.head = self.head.next_node
            
    def insert(self, index, value):  # индексы считаю с 0
        node = self.head
        c = 0
        length = self.size()
        if index == 0:  #если в начало списка
            new_node = Node(value, next_node = self.head)
            self.head = new_node
        elif index > length:
            answer = input('Задан слишком большой индекс. Хотите вставить элемент в конец связного списка? Ответьте "Да" или "Нет"')
            if answer == 'Да':
                self.append(value)
            else:
                return self
        elif index <= length and index != 0:
            while node and node.next_node and c < index-1: #случай,когда мы не задали слишком большой индекс
                c+=1
                node = node.next_node
                
            if c == index-1:
                new_node = Node(value)
                new_node.next_node = node.next_node
                node.next_node = new_node
                
    def value_n_from_end(self, n): #возвращает n-й  элемент с конца, если задано слишком большое n (больше, чем len массива), то возвращает None
        length = self.size()  # считаем с единицы номера
        k = length - n
        c = 0
        node = self.head
        if n == 0:
            return 'Невозможно вернуть нулевой элемент с конца'
        while node and c < k:
            c += 1
            node = node.next_node
        if k == c:
            return node.data




n3 = Node(3)
n2 = Node(2, next_node=n3)
n1 = Node(1, next_node=n2)
l = LinkedList(head=n1)
l.delete(1)
l.insert(0, 17)
l.insert(3, 68)
l.delete(17)
l.delete(68)
l.delete(2)
l.delete(3)
l.printList()
l.insert(0, 15)
l.delete(15)
print(l.value_n_from_end(1))
