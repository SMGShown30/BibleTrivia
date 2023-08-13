class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node

class Stack:
    def __init__(self, max_size=5):
        self.head = None
        self.max_size = max_size
        self.size = 0

    def push(self, value):
        if self.has_space():
            item_to_add = Node(value)
            item_to_add.set_next_node(self.head)
            self.head = item_to_add
            print("Adding " + str(item_to_add.get_value()) + " to the top of the stack")
            self.size += 1
        else:
            print("Sorry there is no more room")

    def pop(self):
        if not self.is_empty():
            top = self.head
            self.head = top.get_next_node()
            self.size -= 1
            print("Removing " + str(top.get_value()) + " from the stack")
        else:
            print("There is nothing in the stack")

    def peek(self):
        if not self.is_empty():
            print(str(self.head.get_value()) + " is at the top")
        else:
            print("There is nothing here to see")

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def has_space(self):
        if self.max_size > self.size:
            return True
        else: 
            return False

        

stack = Stack(6)

stack.push("Michael")
stack.push("Michelle")

stack.pop()
stack.peek()
