class node:
    def __init__(self, data):
        self.next = None
        self.data = data

class linked_list:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
    def append(self,data):
        new_node = node(data)
        if self.head == None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_asFirstNode(self,data):
        new_node =  node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_inMiddle(self,data,prev_node):
        if not prev_node:
            print("No previous node is available enter correct node!!!!!!")
            return

        new_node = node(data)

        new_node.next = prev_node.next
        prev_node.next  = new_node




lnd = linked_list()
lnd.append('A')
lnd.append('B')
# lnd.append('C')
lnd.append('D')
lnd.append('E')
# lnd.print_list()
# print("===============")
lnd.insert_asFirstNode('v')
lnd.insert_inMiddle('C',lnd.head.next.next)
lnd.print_list()
print(l)






