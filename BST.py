# Binary Search Tree
# 210CT Coursework
# Question 1
import string
from BSTDelete import *
	
class BSTNode():
	'''Binary Search Tree Node
	   This class is the basis for each node within the binary search tree structure
	   it is able to hold value for the node and a parent node and two child nodes
	   to create the data structure
	   
	   It requires a value immediately as empty nodes serve no purpose in a binary
	   search tree structure'''
	def __init__(self, value, parent):
		self.parent = parent #Parent node to traverse back up the tree
		self.leftChild = None #Holds the left child node
		self.rightChild = None #Holds the right child node
		self.value = value #Holds the value of the current node
		self.frequency = 1 #Holds the frequency of a value occuring in the data
		
	def checkChildren(self):
		if self.leftChild == None and self.rightChild == None: #No children
			return "None"
		elif (self.leftChild == None or self.rightChild == None) and not (self.leftChild == None and self.rightChild == None): #One child
			if self.leftChild != None and self.rightChild == None:
				return "Left"
			else:
				return "Right"
		else: #Two children
			return "Both"
	
	
def insertNode(tree, item, parent = None):
	'''Takes the variable that stores the root of the tree and inserts a new node
	   or creates the root as a node if it is empty
	   
	   Requires the tree and the item to be inserted, parent is used only when the
	   function is called recursively to inform the next node what its parent node
	   is'''
	if isinstance(item, str): #Turns strings to lower case for consistency
		item = item.lower()
	
	if tree == None: #If the tree is empty a root is created
		tree = BSTNode(item, parent)
		return tree
	else:
		if item < tree.value: #Creates the left child
			if tree.leftChild == None:
				tree.leftChild = BSTNode(item, tree) #For when there is no child for that node
			else:
				insertNode(tree.leftChild, item, tree) #Continues down the tree if a child node already exists
		
		else: #Creates the right child
			if tree.rightChild == None:
				tree.rightChild = BSTNode(item, tree) #For when there is no child for that node
			else:
				insertNode(tree.rightChild, item, tree) #Continues down the tree if a child node already exists


def treeFromFile(fileName):
	'''Reads the contents of a file and stores them inside of a Binary Search Tree structure
	   Takes the filename of the target file as an argument in string form'''
	try:
		words = list()
		file = open(fileName, 'r') #Opens the file ready to be read

		if file.mode == 'r': #Tests the file was opened in the correct mode
			line = file.read() #Assigns contents to a variable
		else:
			raise ValueError("File could not be read\nReason: File not in read mode")
		words = line.split()
	except ValueError:
		print("File could not be opened correctly. Please check input file and try again")
		return 1
	
	file.close() #Closes the file		
	
	currentNodes = list() #Creates a list to store words that have already been added to the tree
	count = 0
	for word in words: #Create tree
		word = str(word)
		if word[-1:] in string.punctuation:
			word = word[:-1]
		
		if word.upper() in currentNodes:
			existingNode = searchNoPrint(word.lower(), tree)
			existingNode.frequency += 1
			continue
		else:
			if count == 0: #Uses counter to know when to create the root of the tree
				tree = insertNode(None, word.lower())
				currentNodes.append(word.upper()) #Adds word to currentNodes to prevent duplication
				count += 1			
			else:
				insertNode(tree, word.lower())
				currentNodes.append(word.upper()) #Adds word to currentNodes to prevent duplication
	return tree
		
	
def binaryTreeSearch(target, tree):
	'''Searches an existing Binary Search Tree for a value and prints the path
	   regardless of whether the target is found
	   
	   Takes the target value and the target tree as arguments'''
	if isinstance(target, str): #Turns strings to lower case for consistency
		target = target.lower()
		
	if target == tree.value: #Checks if the current value matches the target
		print(tree.value)
		return "Yes"
	
	elif target < tree.value: #Moves down the left of the tree if the target is smaller than the current node
		print(tree.value)
		if tree.leftChild == None: #Checks if the next node is empty meaning the target was not found
			return "No"
		else:
			return binaryTreeSearch(target, tree.leftChild)
	
	else: #Moves down the right of the tree if the target is larger than the current node
		print(tree.value)
		if tree.rightChild == None: #Checks if the next node is empty meaning the target was not found
			return "No"
		else:
			return binaryTreeSearch(target, tree.rightChild)
			
			
def preOrder(tree):
	'''Prints out the tree in pre-order
	   Requires the tree to be passed as an argument'''
	preOrderStr = str(tree.value) + ", "
	if tree.leftChild != None: #Recursive call through the left side of the tree
		preOrderStr += str(preOrder(tree.leftChild))
	if tree.rightChild != None: #Recursive call through the right side of the tree
		preOrderStr += str(preOrder(tree.rightChild))
	return preOrderStr

		
if __name__ == "__main__":
	#tree = treeFromFile("Paragraph.txt")
	#if tree == 1:
	#	print("File error encountered, aborting program...")
	#else:
	#	print(binaryTreeSearch("quo", tree))
	#	printPreOrder(tree)
	
	nums = [6, 2, 10, 1, 3, 4]
	count = 0
	for num in nums:
		if count == 0:
			tree = insertNode(None, num)
			count += 1
		else:
			insertNode(tree, num)
	
	print(preOrder(tree))
	print("-----------------------")
	delete(2, tree)
	print(preOrder(tree))
	print("-----------------------")
	#binaryTreeSearch(3, tree)