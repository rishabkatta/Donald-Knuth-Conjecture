'''
@author-name: Rishab Katta

This program uses python version 2
'''


import math
import Queue
import sys

class Node:
    '''
    Node Class is used to represent each node in the Tree. The Value of each node in the tree is calculated by performing
    factorial, square root and floor operations starting from 4 using BFS algorithm.
    '''

    __slots__ = 'value', 'previousvalue', 'level', 'operation', 'childs'


    def __init__(self, value, operation):
        self.operation=operation
        self.value=value
        self.level=0
        self.previousvalue=0
        self.childs={}

    def getPreviousValue(self):
        return self.previousvalue

    def setPreviousValue(self, previousValue):
        self.previousvalue = previousValue

    def getLevel(self):
        return self.level

    def setLevel(self, level):
        self.level=level

    def getOperation(self):
        return self.operation

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value=value

    def setOperation(self, operation):
        self.operation=operation

def factorial(value):
    '''
    Calculate factorial of a number if the number is less than 150.
    :param value: number to perform factorial operation on
    :return: factorial of the number
    '''
    if(value>150):
        return value
    result=1
    for i in range(1,int(value)+1):
        result=result*i

    return result


class BFS:

    __slots__ = 'root', 'target', 'path'

    def __init__(self, value, target):
        '''
        Constructor to initialize tree structure
        :param value: value to be stored in the node
        :param target: target is the value to be achieved
        '''
        self.root = Node(value, 0)
        self.target=target
        self.path=[]

    def getChildNode(self, value, op):
        '''
        gets the child node value based operation number
        :param value: value of the child node
        :param op: operation based on which value of the child node is calculated
        :return: current node
        '''

        if op is 1:
            node = Node(math.sqrt(value), op)
        elif op is 2:
            node=Node(factorial(int(value)), op)
        elif op is 3:
            node=Node(math.floor(value), op)

        node.setPreviousValue(value)
        return node

    def traverse(self):
        '''
        starts by putting root into the queue and removes it, performs 3 operations on the root and puts the children in
        the queue and performs 3 ops on each of them and so on. The child node values are stored in a dictionary childs
        to get the path once we reach the target
        '''

        que = Queue.Queue()
        que.put(self.root)

        while not que.empty():
            node = que.get()

            for i in range(1,4):
                child = self.getChildNode(node.getValue(), i)
                child.setLevel(node.getLevel()+1)

                if child.getValue() != 1:
                    node.childs[i]=child
                    que.put(child)

            if node.getValue() == self.target:
                self.printPath(self.root)
                break

        for i in range(len(self.path)-1, -1, -1):
            if(self.path[i].getOperation() is 0):
                print "4",
            elif self.path[i].getOperation() is 1:
                print "r",
            elif self.path[i].getOperation() is 2:
                print "!",
            elif self.path[i].getOperation() is 3:
                print "f",


    def printPath(self, node):
        '''
        Used to trace the path to the target from the root node. Puts the paths leading to the target from root in the
        path list.
        :param node: starts from root node
        :return: boolean
        '''

        sys.setrecursionlimit(1500)
        if node is None:
            return False
        if node.getValue() == self.target:
            self.path.append(node)
            return True
        if self.printPath(node.childs.get(1)):
            self.path.append(node)
            return True
        if self.printPath(node.childs.get(2)):
            self.path.append(node)
            return True
        if self.printPath(node.childs.get(3)):
            self.path.append(node)
            return True
        else:
            return False



def main():

    bfs=BFS(4, int(sys.argv[1]))
    bfs.traverse()

if __name__ == '__main__':
    main()




