This repository contains the files for this element of my coursework copied directly
from my repository inside of my module's GitHub organisation

To see the original version with the full history of commits please follow this link:
https://github.coventry.ac.uk/210CT-1819OCTJAN/Binary-Search-Tree

# Binary-Search-Tree

210CT Coursework Submission for Questions 1 and 2
Below are the functions and classes listed under their relevant question number
Most work is split into files meaning Question 1 is answered mostly using BST.py and Question 2 is mostly answered using BST_Delete.py, however both use at least some code from the other file so it is not a clear split between the questions.

Question 1:
Classes:
  - BSTNode
      - __init__(value, parent)
      - checkChildren()

Functions:
  - insertNode(tree, item, parent = None)
  - treeFromFile(fileName)
  - binaryTreeSearch(target, tree)
  - searchNoPrint(target, tree)
  - preOrder(tree)


Question 2:
Classes:
  - BSTNode
      - __init__(value, parent)
      - checkChildren()
      
Functions:
  - searchNoPrint(target, tree)
  - delete(target, tree)
  - deleteNode(node)
  - deleteRoot(root)
