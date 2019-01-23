import unittest
from BST import *

class testDeleteNode(unittest.TestCase):
	def setUp(self):
		self.tree = BSTNode("fox", None)
		self.words = ["be", "xylophone", "an", "zebra", "delta", "room"]
		for word in self.words:
			insertNode(self.tree, word)
		self.root = insertNode(None, "blossom") #Creates a tree with only a root
		
	def tearDown(self):
		self.tree = None
		self.root = None
		
	def testSearchRoot(self):
		'''Test for the searchNoPrint function when the target is the root'''
		self.assertEqual(searchNoPrint("fox", self.tree), self.tree)
		
	def testSearchLeft(self):
		'''Test for the searchNoPrint function when the target is the left child'''
		self.leftChild = self.tree.leftChild
		self.assertEqual(searchNoPrint("be", self.tree), self.leftChild)
		
	def testSearchRight(self):
		'''Test for the searchNoPrint function when the target is the right child'''
		self.rightChild = self.tree.rightChild
		self.assertEqual(searchNoPrint("xylophone", self.tree), self.rightChild)
		
	def testSearchNotIn(self):
		'''Test for the searchNoPrint function when the target is not in the tree'''
		self.assertIsNone(searchNoPrint("gumball", self.tree))
		
	def testDeleteNotIn(self):
		'''Test for the delete function when the target is not in the tree'''
		print("\n") #Format test results
		self.assertIsNone(delete("flimflam", self.tree))
	
	def testDeleteRoot(self):
		'''Test for the delete function when the target is the root the tree'''
		self.assertEqual(delete("fox", self.tree), "Root")
		
	def testDeleteNode(self):
		'''Test for the delete function when the target is in the tree but is not
		   the root of the tree'''
		self.assertEqual(delete("delta", self.tree), "Node")
		
	def testDeleteRootOnly(self):
		'''Test for the deleteRoot function when only the root exists in a tree'''
		deleteRoot(self.root) #Deletes the root created
		
		self.assertIsNone(self.root.value)
		self.assertIsNone(self.root.parent)
		self.assertIsNone(self.root.leftChild)
		self.assertIsNone(self.root.rightChild)
		
	def testDeleteRootLeft(self):
		'''Test for the deleteRoot function when only the root and left child exists
		   in a tree'''
		insertNode(self.root, "all") #Gives root a left child
		self.copyNode = self.root.leftChild
		deleteRoot(self.root) #Deletes the root
		
		self.assertIsNone(self.root.parent)
		self.assertIsNone(self.root.leftChild)
		self.assertIsNone(self.root.rightChild)
		self.assertEqual(self.root.value, self.copyNode.value)
		
	def testDeleteRootRight(self):
		'''Test for the deleteRoot function when only the root and right child
		   exists in a tree'''
		insertNode(self.root, "sauce") #Gives root a right child
		self.copyNode = self.root.rightChild
		deleteRoot(self.root) #Deletes the root
		
		self.assertIsNone(self.root.parent)
		self.assertIsNone(self.root.leftChild)
		self.assertIsNone(self.root.rightChild)
		self.assertEqual(self.root.value, self.copyNode.value)
	
	def testDeleteRootChildren(self):
		'''Test for the deleteRoot function when the root, left child and right
		   child exist within a tree'''
		insertNode(self.root, "all") #Gives root a left and a right child
		insertNode(self.root, "sauce")
		self.copyNode = self.root.rightChild
		self.copyLeft = self.root.leftChild
		deleteRoot(self.root) #Deletes the root
		
		self.assertIsNone(self.root.parent)
		self.assertIsNone(self.root.rightChild)
		self.assertEqual(self.root.value, self.copyNode.value)
		self.assertEqual(self.root.leftChild, self.copyLeft)
		
	def testDeleteRootSubtrees(self):
		'''Test for the deleteRoot function when it has full subtrees'''
		self.copyLeft = self.tree.leftChild #Creates a copy of the current left child
		self.copyRight = self.tree.rightChild #Creates a copy of the current right child
		self.copyNode = self.copyRight.leftChild #Creates a copy of what will become the new root
		deleteRoot(self.tree) #Deletes the root
		
		self.assertIsNone(self.copyRight.leftChild)
		self.assertEqual(self.tree.value, self.copyNode.value)
		self.assertEqual(self.tree.leftChild, self.copyLeft)
		self.assertEqual(self.tree.rightChild, self.copyRight)
		
	def testDeleteNodeLeaf(self):
		'''Test for deleteNode to delete a node that is a leaf but not a root'''
		insertNode(self.root, "trousers")
		deleteNode(self.root.rightChild)
		self.assertIsNone(self.root.rightChild)
		
	def testDeleteNodeBranchLeft(self):
		'''Test for deleteNode to delete a branch with only a left child but
		   that is not a root'''
		insertNode(self.root, "trousers") #Populates tree
		insertNode(self.root, "idea")
		deleteNode(self.root.rightChild)
		self.newChild = self.root.rightChild
		
		self.assertIsNone(self.newChild.leftChild)
		self.assertIsNone(self.newChild.rightChild)
		self.assertEqual(self.newChild.parent, self.root)
		self.assertEqual(self.newChild.value, "idea")
		
	def testDeleteNodeBranchRight(self):
		'''Test for deleteNode to delete a branch with only a right child but
		   that is not a root'''
		insertNode(self.root, "trousers") #Populates tree
		insertNode(self.root, "under")
		deleteNode(self.root.rightChild)
		self.newChild = self.root.rightChild
		
		self.assertIsNone(self.newChild.leftChild)
		self.assertIsNone(self.newChild.rightChild)
		self.assertEqual(self.newChild.parent, self.root)
		self.assertEqual(self.newChild.value, "under")
		
	def testDeleteNodeBranchBoth(self):
		'''Test for deleteNode to delete a branch with both a left and a right
		   child but that is not a root'''
		insertNode(self.root, "trousers") #Populates tree
		insertNode(self.root, "idea")
		insertNode(self.root, "under")
		self.leftLeaf = self.root.rightChild
		self.leftLeaf = self.leftLeaf.leftChild
		deleteNode(self.root.rightChild)
		self.newChild = self.root.rightChild
		
		self.assertEqual(self.newChild.leftChild, self.leftLeaf)
		self.assertIsNone(self.newChild.rightChild)
		self.assertEqual(self.newChild.parent, self.root)
		self.assertEqual(self.newChild.value, "under")
		
	def testDeleteNodeSubTrees(self):
		'''Test for deleteNode to delete a branch with subtrees'''
		self.words2 = ["tree", "idea", "under", "cat", "jacket", "zebra", "call", "lemon"]
		for word in self.words2:
			insertNode(self.root, word)
		self.leftSub = self.root.rightChild #Creates a reference to the left subtree
		self.leftSub = self.leftSub.leftChild
		self.leftSubLeft = self.leftSub.leftChild #Creates references to second layer of left subtree
		self.leftSubRight = self.leftSub.rightChild
		self.rightLeaf = self.root.rightChild #Creates a reference to the right leaf
		self.rightLeaf = self.rightLeaf.rightChild
		self.rightLeaf = self.rightLeaf.rightChild
		deleteNode(self.root.rightChild)
		self.newChild = self.root.rightChild
		self.newChildLeft = self.newChild.leftChild
		
		self.assertEqual(self.newChild.leftChild, self.leftSub)
		self.assertEqual(self.newChild.rightChild, self.rightLeaf)
		self.assertEqual(self.newChild.parent, self.root)
		self.assertEqual(self.newChild.value, "under")
		self.assertEqual(self.newChildLeft.leftChild, self.leftSubLeft)
		self.assertEqual(self.newChildLeft.rightChild, self.leftSubRight)
		

if __name__ == "__main__":
	unittest.main()