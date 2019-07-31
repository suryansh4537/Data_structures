# Parenthesis is balanced or not
from stack1 import stack

def is_match(p1,p2):
    if p1 =='(' and p2==')':
        return True
    elif p1 =='[' and p2==']':
        return True
    elif p1 =='{' and p2=='}':
        return True
    else:
        return False

def is_paran_balanced(str):
    s = stack()
    is_balanced = True
    index = 0
    while index<len(str) and is_balanced:
        paren = str[index]

        if paren in '({[':
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            elif not s.is_empty():
                top = s.pop()
                if not is_match(top,paren):
                    is_balanced = False
        index += 1
    if is_balanced:
        return True
    else:
        return False
str = input()
print(is_paran_balanced(str))