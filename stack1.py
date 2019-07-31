class stack():
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def top(self):
        if not self.is_empty():
            return self.items[-1]
    def lenofstack(self):
        return self.items.__len__()
    def show(self):
        return self.items
    def clear(self):
        self.items=[]

# s = stack()
# s.push(4)
# s.push(10)
# s.push(12)
# s.push(13)
# s.push(14)
# # s.pop()
#
# print(s.show())
# print(s.lenofstack())
# print(s.is_empty())
# s.clear()
# print(s.is_empty())
