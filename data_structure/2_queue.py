#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# 循环出队、入队；到标记点出队；判断队列是否只剩1个元素


def hotPotato(namelist, num):
    queue = Queue()

    for i in namelist:
        queue.enqueue(i)

    print(queue.items)
    while queue.size() > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())
            print(queue.items)

        d = queue.dequeue()
        print('dequeue----------', d)
    return queue.dequeue()

# while for 组合


print(hotPotato('abcdefg', 7))
