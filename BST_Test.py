import unittest
from BST import *

class testBST(unittest.TestCase):
	def setUp(self):
		self.tree = BSTNode("fox", None)
		self.words = ["be", "xylophone", "an", "zebra", "delta", "room"]
		
	def tearDown(self):
		self.tree = None
		
	def testCheckChildrenNone(self):
		'''Test for checkChild function used on a node with no children'''
		self.assertEqual(self.tree.checkChildren(), "None")
	
	def testCheckChildrenLeft(self):
		'''Test for checkChild function used on a node with only a left child'''
		self.tree.leftChild = BSTNode("An", self.tree) #Creates a left child
		self.assertEqual(self.tree.checkChildren(), "Left")
	
	def testCheckChildrenRight(self):
		'''Test for checkChild function used on a node with only a right child'''
		self.tree.rightChild = BSTNode("Xylophone", self.tree) #Creates a right child
		self.assertEqual(self.tree.checkChildren(), "Right")
		
	def testCheckChildrenBoth(self):
		'''Test for checkChild function used on a node with two children'''
		self.tree.leftChild = BSTNode("An", self.tree) #Creates left and right child
		self.tree.rightChild = BSTNode("Xylophone", self.tree)
		self.assertEqual(self.tree.checkChildren(), "Both")
		
	def testInsertRoot(self):
		'''Test for insertNode function used to insert a root in a new tree'''
		self.root = insertNode(None, "foxtrot") #Creates a test tree with one node
		self.assertIsNone(self.root.parent)
		self.assertIsNone(self.root.leftChild)
		self.assertIsNone(self.root.rightChild)
		self.assertEqual(self.root.value, "foxtrot")
		
	def testInsertLeftChildRoot(self):
		'''Test for insertNode function used to insert a node as a left child to an
		   existing tree with only a root'''
		insertNode(self.tree, "an") #Adds a left child to the root
		self.leftChild = self.tree.leftChild #Creates a quick reference to the left child
		self.assertEqual(self.leftChild, self.tree.leftChild)
		self.assertEqual(self.leftChild.parent, self.tree)
		self.assertIsNone(self.tree.rightChild)
		
	def testInsertRightChildRoot(self):
		'''Test for insertNode function used to insert a node as a left child to an
		   existing tree with only a root'''
		insertNode(self.tree, "xylophone") #Adds a right child to the root
		self.rightChild = self.tree.rightChild #Creates a quick reference to the right child
		self.assertEqual(self.rightChild, self.tree.rightChild)
		self.assertEqual(self.rightChild.parent, self.tree)
		self.assertIsNone(self.tree.leftChild)
		
	def testInsertLeftChild(self):
		'''Test for insertNode function used to insert a node as a left child to an
		   existing tree a root and two children'''
		insertNode(self.tree, "be") #Populates first layer of the tree
		insertNode(self.tree, "xylophone")
		insertNode(self.tree, "an") #Adds a left child to the tree
		self.leftChild = self.tree.leftChild #Creates a quick reference to the left child
		self.nextChild = self.leftChild.leftChild #Creates a quick reference to the new child
		
		self.assertEqual(self.nextChild, self.leftChild.leftChild)
		self.assertEqual(self.nextChild.parent, self.leftChild)
		self.assertEqual(self.nextChild.value, "an")
		self.assertIsNone(self.leftChild.rightChild)
		
	def testInsertRightChild(self):
		'''Test for insertNode function used to insert a node as a right child to an
		   existing tree a root and two children'''
		insertNode(self.tree, "an") #Populates first layer of the tree
		insertNode(self.tree, "xylophone")
		insertNode(self.tree, "zebra") #Adds a left child to the tree
		self.rightChild = self.tree.rightChild #Creates a quick reference to the left child
		self.nextChild = self.rightChild.rightChild #Creates a quick reference to the new child
		
		self.assertEqual(self.nextChild, self.rightChild.rightChild)
		self.assertEqual(self.nextChild.parent, self.rightChild)
		self.assertEqual(self.nextChild.value, "zebra")
		self.assertIsNone(self.rightChild.leftChild)
		
	def testSearchRoot(self):
		'''Test for binaryTreeSearch when word is the root of the tree'''
		for word in self.words:
			insertNode(self.tree, word)
		print("\n") #Clear formatting for test results
		self.assertEqual(binaryTreeSearch("fox", self.tree), "Yes")
		
	def testSearchLeft(self):
		'''Test for binaryTreeSearch when word is on the left side of the tree'''
		for word in self.words:
			insertNode(self.tree, word)
		print("\n") #Clear formatting for test results
		self.assertEqual(binaryTreeSearch("an", self.tree), "Yes")
		
	def testSearchRight(self):
		'''Test for binaryTreeSearch when word is on the right side of the tree'''
		for word in self.words:
			insertNode(self.tree, word)
		print("\n") #Clear formatting for test results
		self.assertEqual(binaryTreeSearch("zebra", self.tree), "Yes")
		
	def testSearchNotIn(self):
		'''Test for binaryTreeSearch when word is not in tree'''
		for word in self.words:
			insertNode(self.tree, word)
		print("\n") #Clear formatting for test results
		self.assertEqual(binaryTreeSearch("gumball", self.tree), "No")
		
	def testTreeFromFileSingle(self):
		'''Test for the treeFromFile function reading a single word from a file'''
		fileName = "Test_Text/SingleWord.txt"
		self.treeFile = treeFromFile(fileName)
		self.assertEqual(self.treeFile.value, "word")
		self.assertIsNone(self.treeFile.parent)
		self.assertIsNone(self.treeFile.leftChild)
		self.assertIsNone(self.treeFile.rightChild)
		
	def testTreeFromFileOneLine(self):
		'''Test for the treeFromFile function reading from text one line in a file'''
		fileName = "Test_Text/MultiWord1.txt"
		self.treeFile = treeFromFile(fileName)
		self.copyLeft = self.treeFile.leftChild
		self.copyRight = self.treeFile.rightChild
		
		self.assertEqual(self.treeFile.value, "meh")
		self.assertIsNone(self.treeFile.parent)
		self.assertEqual(self.treeFile.leftChild, self.copyLeft)
		self.assertEqual(self.treeFile.rightChild, self.copyRight)
		
		self.assertEqual(self.copyLeft.value, "charmander")
		self.assertEqual(self.copyLeft.parent, self.treeFile)
		self.assertIsNone(self.copyLeft.leftChild)
		self.assertIsNone(self.copyLeft.rightChild)
		
		self.assertEqual(self.copyRight.value, "tile")
		self.assertEqual(self.copyRight.parent, self.treeFile)
		self.assertIsNone(self.copyRight.leftChild)
		self.assertIsNone(self.copyRight.rightChild)
		
	def testTreeFromFileMultiLine(self):
		'''Test for the treeFromFile function reading words from multiple lines in
		   a file'''
		fileName = "Test_Text/MultiWord2.txt"
		self.treeFile = treeFromFile(fileName)
		self.left = self.treeFile.leftChild
		self.right = self.treeFile.rightChild
		self.leftLeft = self.left.leftChild
		self.leftRight = self.left.rightChild
		self.rightLeft = self.right.leftChild
		
		self.assertEqual(self.treeFile.value, "meh")
		self.assertIsNone(self.treeFile.parent)
		self.assertEqual(self.treeFile.leftChild, self.left)
		self.assertEqual(self.treeFile.rightChild, self.right)
		
		self.assertEqual(self.left.value, "bulbasaur")
		self.assertEqual(self.left.parent, self.treeFile)
		
		self.assertEqual(self.leftLeft.value, "abra")
		self.assertEqual(self.leftLeft.parent, self.left)
		self.assertIsNone(self.leftLeft.leftChild)
		self.assertIsNone(self.leftLeft.rightChild)
		
		self.assertEqual(self.leftRight.value, "don")
		self.assertEqual(self.leftRight.parent, self.left)
		self.assertIsNone(self.leftRight.leftChild)
		self.assertIsNone(self.leftRight.rightChild)
		
		self.assertEqual(self.right.value, "tile")
		self.assertEqual(self.right.parent, self.treeFile)
		
		self.assertEqual(self.rightLeft.value, "squirtle")
		self.assertEqual(self.rightLeft.parent, self.right)
		self.assertIsNone(self.rightLeft.leftChild)
		self.assertIsNone(self.rightLeft.rightChild)
		
	def testTreeFromFileOneLineDups(self):
		'''Test for the treeFromFile function reading from text one line in a file
		   but with duplicates in the file'''
		fileName = "Test_Text/MultiWord3.txt"
		self.treeFile = treeFromFile(fileName)
		self.copyLeft = self.treeFile.leftChild
		self.copyRight = self.treeFile.rightChild
		
		self.assertEqual(self.treeFile.value, "meh")
		self.assertIsNone(self.treeFile.parent)
		self.assertEqual(self.treeFile.leftChild, self.copyLeft)
		self.assertEqual(self.treeFile.rightChild, self.copyRight)
		
		self.assertEqual(self.copyLeft.value, "charmander")
		self.assertEqual(self.copyLeft.parent, self.treeFile)
		self.assertIsNone(self.copyLeft.leftChild)
		self.assertIsNone(self.copyLeft.rightChild)
		
		self.assertEqual(self.copyRight.value, "tile")
		self.assertEqual(self.copyRight.parent, self.treeFile)
		self.assertIsNone(self.copyRight.leftChild)
		self.assertIsNone(self.copyRight.rightChild)
		
	def testTreeFromFileMultiLineDups(self):
		'''Test for the treeFromFile function reading words from multiple lines in
		   a file with duplicates'''
		fileName = "Test_Text/MultiWord4.txt"
		self.treeFile = treeFromFile(fileName)
		self.left = self.treeFile.leftChild
		self.right = self.treeFile.rightChild
		self.leftLeft = self.left.leftChild
		self.leftRight = self.left.rightChild
		self.rightLeft = self.right.leftChild
		
		self.assertEqual(self.treeFile.value, "meh")
		self.assertIsNone(self.treeFile.parent)
		self.assertEqual(self.treeFile.leftChild, self.left)
		self.assertEqual(self.treeFile.rightChild, self.right)
		
		self.assertEqual(self.left.value, "bulbasaur")
		self.assertEqual(self.left.parent, self.treeFile)
		
		self.assertEqual(self.leftLeft.value, "abra")
		self.assertEqual(self.leftLeft.parent, self.left)
		self.assertIsNone(self.leftLeft.leftChild)
		self.assertIsNone(self.leftLeft.rightChild)
		
		self.assertEqual(self.leftRight.value, "don")
		self.assertEqual(self.leftRight.parent, self.left)
		self.assertIsNone(self.leftRight.leftChild)
		self.assertIsNone(self.leftRight.rightChild)
		
		self.assertEqual(self.right.value, "tile")
		self.assertEqual(self.right.parent, self.treeFile)
		
		self.assertEqual(self.rightLeft.value, "squirtle")
		self.assertEqual(self.rightLeft.parent, self.right)
		self.assertIsNone(self.rightLeft.leftChild)
		self.assertIsNone(self.rightLeft.rightChild)
		
	def testPreOrderRoot(self):
		'''Test for preOrder function when the tree is only a root'''
		self.assertEqual(preOrder(self.tree), "fox, ")
		
	def testPreOrderLeft(self):
		'''Test for preOrder function when the tree is only a root and a left child'''
		insertNode(self.tree, "Axe")
		self.assertEqual(preOrder(self.tree), "fox, axe, ")
		
	def testPreOrderRight(self):
		'''Test for preOrder function when the tree is only a root and a right child'''
		insertNode(self.tree, "Yukata")
		self.assertEqual(preOrder(self.tree), "fox, yukata, ")
		
	def testPreOrderBoth(self):
		'''Test for preOrder function when the tree is only a root and both children'''
		insertNode(self.tree, "Axe")
		insertNode(self.tree, "Yukata")
		self.assertEqual(preOrder(self.tree), "fox, axe, yukata, ")
		
	def testPreOrderSubTrees(self):
		'''Test for preOrder function when the tree is a root and subtrees'''
		for word in self.words:
			insertNode(self.tree, word)
		self.assertEqual(preOrder(self.tree), "fox, be, an, delta, xylophone, room, zebra, ")
		

if __name__ == "__main__":
	unittest.main()
	
	