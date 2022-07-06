
class node:
    def __init__(self, data = None):
        self.data = data # points to last node
        self.next = None # points to next node

class linked_list:
    def __init__(self): # list length 0, not accessable by user
        self.head = node() # not a data node

    def append(self, data):
        new_node = node(data) # sets data into node
        cur = self.head
        while cur.next != None: # if there is still next node, move along
            cur = cur.next
        cur. next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total # gives length of linked list

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data) # looks at and adds data to list
        print(elems) # prints the list of data viewed


my_list = linked_list

my_list.display()

my_list.append(55)

my_list.append("ffff")