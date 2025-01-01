import sys
import io
from collections import deque


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def main(rootNode):
    currentLevel = deque()
    nextLevel = deque()
    currentLevel.append(rootNode)
    string = ""
    levelPrint(string, currentLevel,nextLevel) 

def levelPrint(levelString, currentLevel, nextLevel):
    if (len(currentLevel) > 0):
        currentNode = currentLevel.popleft()
        if currentNode.left != None:
            nextLevel.append(currentNode.left)
        if currentNode.right != None:
            nextLevel.append(currentNode.right)
        levelString += str(currentNode.value)
        if len(currentLevel) > 0:
            levelString += ", "
            levelPrint(levelString, currentLevel,nextLevel)
        else:
            print(levelString)
            levelString = ""
            currentLevel.extend(nextLevel)
            nextLevel.clear()
            levelPrint(levelString, currentLevel, nextLevel)
    else:
        return

def buildNode(value):
    if value is not None:
        print("The Current Node is '" + str(value) + "'")
        left = input("Enter Left Node Value: ")
        if len(left) == 0:
            left = None
        right = input("Enter Right Node Value: ")
        if len(right) == 0:
            right = None
        print("--------------")
        if left != None and right != None:
            return Node(value, buildNode(int(left)), buildNode(int(right)))
        elif left == None and right != None:
            return Node(value, None, buildNode(int(right)))
        elif left != None and right == None:
            return Node(value, buildNode(int(left)), None)
        else:
            return Node(value, None, None)

if __name__ == "__main__":
  RootValue = int(input("Enter Root Value: "))
  main(buildNode(RootValue))