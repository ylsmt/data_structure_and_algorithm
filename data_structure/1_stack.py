#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(items) - 1]

    def isEmpty(self):
        return self.items == []


#  括号配对
# 1. 左括号入栈，遇到右括号左括号出栈
# 2. 考虑左括号少，右括号多，出栈时判断是否为空；栈空，说明不配对
# 3. 左括号多，栈不为空

def parCheck(string):
    stack = Stack()

    for i in range(len(string)):
        if string[i] == '(':
            stack.push(string[i])

        else:
            if stack.isEmpty():
                return False
            stack.pop()

    if stack.isEmpty():
        return True

    else:
        return False


print(parCheck('(()))'))  # False
print(parCheck('((())'))  # False
print(parCheck('))'))    # False
print(parCheck('(())'))  # True
print(parCheck('(('))    # False
