#Double Linked Lists
#have a beginner, end, and previous pointer so the operations (i.e. push and pop) are easier

"""
    With a prev pointer you now have to handle more conditions in each operation:
    1. Are there zero elements? Then self.begin and self.end need to be None.
    2. If there is one element, then self.begin and self.end have to be equal (point at same
    node).
    3. The first element must always have a prev that is None.
    4. The last element must always have a next that is None.

    Check for invariants
"""

class DoubleLinkedListNode(object):
    def __init__(self, value, prev=None, next_node=None):
        self.prev = prev
        self.value = value
        self.next = next_node
    
class DoubleLinkedList(object):
    def __init__(self):
        self.begin = None
        self.end = None

    #counts the number of elements in the list
    def count(self):
        current_node = self.begin
        num_nodes = 0
        while current_node:
            num_nodes += 1
            current_node = current_node.next
        return num_nodes

    #checks the begin, end, and prev 
    def _invariant(self):
        if self.begin == None:
            assert self.end == None
        else:
            assert self.begin.prev == None
            assert self.end.next == None

    #add a new node to the end
    def push(self, obj):
        #if list is empty
        if self.end == None:
            self.begin = DoubleLinkedListNode(obj)
            self.end = self.begin
        
        #if list only has at least one item
        else:
            new_node = DoubleLinkedListNode(obj, self.end)
            self.end.next = new_node
            self.end = new_node

    #remove the last node and return it   
    def pop(self):
        #if list is empty
        if self.end == None:
            return None

        #if list only has one item
        elif self.begin == self.end:
            current_node = self.begin
            self.begin = self.end = None
            return current_node.value

        #if list has at least one item
        else:
            current_node = self.end
            self.end = current_node.prev
            self.end.next = None


            return current_node.value
    
    #remove needs a helper function 
    #take a node and detach it from the begining, end, 
    #or middle of the list
    def detach_node(self, node):
        #if the node is at the begining
        if self.begin == node:
            current_node = self.begin

            #check if there is only one node
            if self.begin == self.end:
                self.begin = self.end = None
            else:
                self.begin = current_node.next
                self.begin.prev = None

        #if the node is at the end
        elif self.end == node:
            self.pop()

        #if the node is in the middle
        else:
            #node.prev.next = node.next
            next_node = node.next
            prev_node = node.prev
            prev_node.next = next_node
            self.next.prev = prev_node

    #finds a matching item and removes it from the list
    def remove(self, obj):
        current_node = self.begin

        #keep track of the index
        node_count = 0

        while current_node:
            if current_node.value == obj:
                self.detach_node(current_node)
                return node_count
            else:
                node_count += 1
                current_node = current_node.next

    #get the value at the index
    def get(self, index):
        current_node = self.begin
        i = 0

        while current_node:
            if i == index:
                return current_node.value
            else:
                i += 1
                current_node = current_node.next
        return None

    #returns a reference to the first item, does not remove
    def first(self):
        return self.begin and self.begin.value or None

    #returns a referenve to the last item, does not remove
    def last(self):
        return self.end and self.end.value or None
        
        

    
