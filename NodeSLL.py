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

class LinkedList:
    def __init__(self):
        self.head_node = None
    
    def get_head_node(self):
        return self.head_node

    def add_node(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def remove_node(self, value_to_remove):
        # if node we want to remove is the head node
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            new_head = current_node.get_next_node()
            self.head_node = new_head
        # if node we want to remove is the 2nd node
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
        # if node we want to remove is any other node besides the 1st and 2nd
                else:
                    current_node = next_node
    
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + " -> "
        # if the value of the current node is none
            current_node = current_node.get_next_node()
        return string_list



ord_to_lax = LinkedList()
ord_to_lax.add_node("Go to Chicago Ohare Int Airport")
ord_to_lax.add_node("mexico")
print(ord_to_lax.stringify_list())