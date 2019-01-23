# Binary Search Tree
# 210CT Coursework
# Question 2

def searchNoPrint(target, tree):
	'''Searches an existing Binary Search Tree for a value
	   
	   Takes the target value and the target tree as arguments'''
	if isinstance(target, str): #Turns strings to lower case for consistency
		target = target.lower()
	
	if target == tree.value: #Checks if the current value matches the target
		return tree
	
	elif target < tree.value: #Moves down the left of the tree if the target is smaller than the current node
		
		if tree.leftChild == None: #Checks if the next node is empty meaning the target was not found
			return None
		else:
			return searchNoPrint(target, tree.leftChild)
	
	else: #Moves down the right of the tree if the target is larger than the current node
		if tree.rightChild == None: #Checks if the next node is empty meaning the target was not found
			return None
		else:
			return searchNoPrint(target, tree.rightChild)
		

def delete(target, tree):
	'''Deletes a node from the binary search tree by determining if it is a
	   regular node or a root and calling the appropriate deletion function
	   
	   Takes the target value of node to be deleted and the tree as arguments'''
	try:
		node = searchNoPrint(target, tree)

		if node == None:
			raise ValueError("Target does not exist inside of tree, removal failed")

		else:
			if node.parent == None: #Check if the node is the root
				deleteRoot(tree)
				return "Root"
			else:
				deleteNode(node)
				return "Node"
	except ValueError:
		print("Node does not exist within the given tree, removal unnecessary")
		return None
		
		
def deleteNode(node):
	'''Deletes a node from the binary search tree
	   
	   Takes the target node to be deleted as an argument'''
	child = node.checkChildren()
	
	if child == "None": #If the node has no children (Is a leaf)
		parent = node.parent #Traverse back up to the parent
		
		if node == parent.leftChild: #Delete the leftChild if it is the target
			parent.leftChild = None
		
		else: #Delete the rightChild if it is the target
			parent.rightChild = None
	
	elif child == "Left": #If the node only has a left child
		parent = node.parent #Traverse back up to the parent
		newNode = node.leftChild

		if node == parent.leftChild: #Delete the leftChild if it is the target
			parent.leftChild = newNode
			newNode.parent = parent
		
		else: #Delete the rightChild if it is the target
			parent.rightChild = newNode
			newNode.parent = parent
	
	elif child == "Right": #If the node only has a right child
		parent = node.parent #Traverse back up to the parent
		newNode = node.rightChild
		
		if node == parent.leftChild: #Delete the leftChild if it is the target
			parent.leftChild = newNode
			newNode.parent = parent
		
		else: #Delete the rightChild if it is the target
			parent.rightChild = newNode
			newNode.parent = parent
			
	else: #If the node has two children
		holder = node.rightChild
		
		if holder.checkChildren == "None": #If right subtree has only one node
			node.value = holder.value
			node.rightChild = None
		
		else: #If right subtree has more than one node
			while holder.leftChild != None: #Loop to cycle through node to find minimum of right subtree
				holder = holder.leftChild
			node.value = holder.value
			parent = holder.parent
			
			if holder == parent.leftChild: #Delete the minimum leaf of the right subtree if it was a left child
				if holder.rightChild == None:
					parent.leftChild = None
				else:
					parent.leftChild = holder.rightChild
			
			else: #Delete the minimum leaf of the right subtree if it was the right child
				if holder.rightChild == None:
					parent.rightChild = None
				else:
					parent.rightChild = holder.rightChild

				
def deleteRoot(root):
	'''Deletes the root from a binary search tree
	   
	   Only takes the tree as an argument'''
	child = root.checkChildren()
	
	if child == "None": #Leaves an empty tree if it was only the root in the tree
		root.value = None
		root.frequency = 0
	
	elif child == "Left": #Root only has a left child
		leftChild = root.leftChild
		root.value = leftChild.value
		root.leftChild = None
		root.parent = None
	
	elif child == "Right": #Root only has a right child
		rightChild = root.rightChild
		root.value = rightChild.value
		root.rightChild = None
		root.parent = None
	
	else: #Root has both left and right children
		rootCopy = root #Holds a copy of the root
		holder = root.rightChild #Holds a copy of the root's right child
		
		if holder.checkChildren == "None": #If right subtree has only one node
			root.value = holder.value
			root.rightChild = None
		
		else:
			while holder.leftChild != None: #Loop to cycle through node to find minimum of right subtree
				holder = holder.leftChild
			root.value = holder.value
			parent = holder.parent
			
			if holder == parent.leftChild: #Delete the minimum leaf of the right subtree if it was a left child
				parent.leftChild = None
			
			else: #Delete the minimum leaf of the right subtree if it was the right child
				parent.rightChild = None