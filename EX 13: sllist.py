

#Implement SingleLinkedLists

#the class for each node
class SingleLinkedListNode(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    #repr prints debugging output when called on the node
    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value} : {repr(nval)}]"


#the controller for the Single Linked List (the operations used)
class SingleLinkedList(object):
    def __init__(self):
        self.begin = None
        self.end = None

    #append new value on the end of the list
    def push(self, obj):
        new_node = SingleLinkedListNode(obj, None)
        #if single linked list is empty, then make the new_node the beginning AND end node
        if self.begin == None:
            self.begin = new_node
            self.end = self.begin
        #if the sll is NOT empty
        else:
            self.end.next = new_node
            self.end = new_node
            
            #make sure the beginning and the end are not the same node
            assert self.begin != self.end
        
        #make sure the end node points to None
        assert self.end.next == None

    #removes the last item and returns it
    def pop(self):
        if self.end == None:
            return None
        elif self.begin == None:
            return None
        elif self.begin == self.end:
            current_node = self.begin
            self.begin = self.end = None
            return current_node.value
        else:
            current_node = self.begin
            #goes through the whole sll, until it reaches the end
            while current_node.next != self.end:
                current_node = current_node.next
            #assert self.end != current_node
            node_val = current_node.next.value
            self.end = current_node
            self.end.next = None
            return node_val



    #finds a matching item and removes it from the list
    #counts how many times the item was removed
    def remove(self, obj):
        current_node = self.begin
        if current_node != None:
            if current_node.value == obj:
                self.begin = current_node.next
                current_node = None
                return 
        
        while current_node != None:
            if current_node.value == obj:
                break
            prev = current_node
            current_node = current_node.next
            

        if current_node == None:
            return 
        prev.next = current_node.next
        current_node = None



    def count(self):
        current_node = self.begin
        node_count = 0
        while current_node != None:
            current_node = current_node.next
            node_count += 1

        return node_count

        

    #debugging function that dumps the contents of the list
    def print_list(self):
        current_node = self.begin
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    #returns a reference to the first item, does not remove
    def first(self):
        return self.begin.value

    #returns a references to the last item, does not remove
    def last(self):
        return self.end.value


    #get the value at index
    def get(self, index):
        current_node = self.begin
        if current_node == None:
            return None
        i = 0
        while i <= index - 1:
            current_node = current_node.next
            i += 1
 

        if current_node == None:
            return None
        return current_node.value

