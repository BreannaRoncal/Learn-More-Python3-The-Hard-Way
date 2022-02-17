#Similar to DoubleLinkedList

class QueueNode(object):
    def __init__(self, value, prev=None, nxt=None):
        self.value = value
        self.prev = prev
        self.next = nxt


class Queue(object):
    def __init__(self):
        self.begin = None
        self.end = None
    
    def count(self):
        current_node = self.begin
        num_nodes = 0
        
        while current_node:
            num_nodes += 1
            current_node = current_node.next
        
        return num_nodes

    #add a new item to the back of the queue
    def push(self, val):
        #if queue is empty:
        if self.end == None:
            new_node = QueueNode(val)
            self.begin = new_node
            self.end = self.begin
        #if queue has 1 item
        elif self.end == self.begin:
            new_node = QueueNode(val)
            self.begin.next = new_node
            self.end = new_node
        #if queue has more than 1 item
        else:
            new_node = QueueNode(val)
            self.end.next = new_node
            self.end = new_node
    #remove and return the first item from the queue
    def pop(self):
        #if queue is empty
        if self.end == None:
            return None
        #if queue has 1 item
        elif self.begin == self.end:
            current_node = self.begin
            self.begin = self.end = None
            return current_node.value
        #if queue has more than 1 item
        else:
            current_node = self.begin
            self.begin = current_node.next
            return current_node.value

