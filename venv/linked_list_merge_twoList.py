# Swap and Delete
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

    def delete_list(self,item):
        cur_node = self.head
        if cur_node and cur_node.data == item:
            self.head = cur_node.next
            cur_node = None
            return
        prev_node = None
        while cur_node and cur_node.data != item:
            prev_node = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        else:
            prev_node.next = cur_node.next
            cur_node = None

    def delete_node_atPos(self,pos):
        cur_node = self.head
        if pos is 0:
            self.head = cur_node.next
            cur_node = None
            return
        prev_node = None
        count = 1
        cur_node = self.head.next
        while cur_node and count!=pos:
            count+=1
            prev_node = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        else:
            prev_node.next = cur_node.next
            cur_node = None

    def swap_nodes(self, e1, e2):
        if e1 == e2:
            return
        prev1 = None
        cur1 = self.head
        while cur1 and cur1.data!=e1:
            prev1 = cur1
            cur1 = cur1.next

        prev2 = None
        cur2  = self.head
        while cur2 and cur2.data!=e2:
            prev2 = cur2
            cur2 = cur2.next

        if not cur1 or not cur2:
            return

        if prev1:
            prev1.next = cur2
        else:
            self.head = cur2
        if prev2:
            prev2.next = cur1
        else:
            self.head = cur1
        cur1.next,cur2.next = cur2.next,cur1.next

    def reverse_list(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def reverse_recursive(self):

        def _reverse_recursive(cur,prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur,prev)
        self.head = _reverse_recursive(cur = self.head, prev= None)

    def merge_twoSortedList(self,list_2):
        p = self.head
        q = list_2.head
        s = None
        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next=q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head # because head is set at s above and it will be same 


lnd = linked_list()
lnd2 = linked_list()
lnd.append('1')
lnd.append('3')
lnd.append('7')
lnd.append('9')
lnd.append('10')

lnd2.append('2')
lnd2.append('4')
lnd2.append('5')
lnd2.append('6')
lnd2.append('8')

lnd.merge_twoSortedList(lnd2)

# lnd.print_list()
lnd.reverse_recursive()
lnd.print_list()
# # print("===============")
# lnd.insert_asFirstNode('v')
# lnd.insert_inMiddle('C',lnd.head.next.next)
# # lnd.print_list()
# # print("=======================")
# lnd.delete_node_atPos(5)
# lnd.swap_nodes('C','v')
# lnd.print_list()






