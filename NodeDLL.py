class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def get_prev_node(self):
        return self.prev_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def add_to_head(self, new_value):
        new_node = Node(new_value)
        current_head = self.head_node
        # if there are nodes already
        if current_head != None:
            new_node.set_next_node(current_head)
            current_head.set_prev_node(new_node)
        
        self.head_node = new_node
        # if there is nothing else in the list
        if self.tail_node == None:
            self.tail_node = new_node

    def add_to_tail(self, new_value):
        new_node = Node(new_value)
        current_tail = self.tail_node
        # if there are nodes already
        if current_tail != None:
            new_node.set_prev_node(current_tail)
            current_tail.set_next_node(new_node)

        self.tail_node = new_node
        # if there is nothing else in the list
        if self.head_node == None:
            self.head_node = new_node

    def remove_head(self):
        head_to_remove = self.head_node

        if self.head_node == None:
            return None
        
        new_head = head_to_remove.get_next_node()
        self.head_node = new_head

        if new_head != None:
            new_head.set_prev_node(None)

        if new_head == self.tail_node:
            self.remove_tail()

    def remove_tail(self):
        tail_to_remove = self.tail_node

        if self.tail_node == None:
            return None
        
        new_tail = tail_to_remove.get_prev_node()
        self.tail_node = new_tail

        if new_tail != None:
            new_tail.set_next_node(None)

        if new_tail == self.head_node:
            self.remove_head()
    
    def remove_by_value(self, value_to_remove):
        node_to_remove = None
        current_node = self.head_node

        while current_node != None:
            if current_node.get_value() == value_to_remove:
                node_to_remove = current_node
                break
            
            current_node = current_node.get_next_node()

        if node_to_remove == None:
            return None
        
        if node_to_remove == self.head_node:
            self.remove_head()
        elif node_to_remove == self.tail_node:
            self.remove_tail()
        else:
            next_node = node_to_remove.get_next_node()
            prev_node = node_to_remove.get_prev_node()
            prev_node.set_next_node(next_node)
            next_node.set_prev_node(prev_node)
        
        return node_to_remove

    def stringify_list(self):
        string_list = ""
        current_node = self.head_node
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + " -> "
            current_node = current_node.get_next_node()
        return string_list




        


ll = DoublyLinkedList()

ll.add_to_head("Hello")
ll.remove_head()

print(ll.stringify_list())
