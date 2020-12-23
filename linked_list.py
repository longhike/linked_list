class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.root = Node()
    
    def append(self, data):
        new_node = Node(data)
        current = self.root
        while current.next != None:
            current = current.next
        current.next = new_node

    def length(self):
        result = 0
        current = self.root
        while current.next != None:
            result += 1
            current = current.next
        return(result)

    def getByIndex(self, idx):
        if idx >= self.length():
            return "Invalid: cannot search for index not in list"
        else:
            iteration = 0
            current = self.root
            while True:
                current = current.next
                if iteration == idx:
                    return(current.data)
                iteration += 1

    def printList(self):
        this_list = []
        current = self.root
        while current.next != None:
            current = current.next
            this_list.append(current.data)
        return(this_list)

list_example = LinkedList()

list_example.append("first")
list_example.append("second")
print(list_example.printList())
print(list_example.length())
print(list_example.getByIndex(1))
