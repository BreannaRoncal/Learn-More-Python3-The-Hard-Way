#Similar to SingleLinkedList

class StackNode(object):
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


class Stack(object):
    def __init__(self):
        self.top = None

    #counts the number of elements in the stack
    def count(self):
        current_node = self.top
        num_nodes = 0

        while current_node:
            num_nodes += 1
            current_node = current_node.next

        return num_nodes

    #push a new value to the top of the stack
    def push(self, obj):
        self.top = StackNode(obj, self.top)

    #pops the value that is currently on the top of the stack
    def pop(self):
        #if stack is empty
        if self.top == None:
            return None
        #if stack has one item
        elif self.top.next == None:
            current_node = self.top
            self.top = None
            return current_node.value

        #if stack has more than one item
        else:
            current_node = self.top
            next_node = self.top.next
            self.top = next_node
            return current_node.value


    #returns a reference to the first item, does not remove
    def first(self):
        return self.top != None and self.top.value or None

