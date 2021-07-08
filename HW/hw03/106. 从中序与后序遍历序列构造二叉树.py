# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
            inorder =   [9,         | 3, | 15,   20,     7], 
                        l1          mid   mid+1          r1    
                        <-leftSize->      <-- rightSize ->
            postorder = [9, 15, 7, 20        |   3  ] ==> We know the last one is root
                        l2 --- l2+leftSize --- r2-1   r2
        """
        root = self.traverse(inorder, 0, len(inorder), postorder, 0, len(postorder))
        return root

    def traverse(self, inorder, l1, r1, postorder, l2, r2):
        if l1>=r1 or l2>= r2:
            return None
        
        root = TreeNode()
        # print(f"r2: {r2}, postorder: {postorder}")
        root.val = postorder[r2-1]

        inorder_mid = l1
        while inorder[inorder_mid] != root.val:
            inorder_mid+=1
        # print(f"inorder_mid: {inorder_mid}")
        leftSize = inorder_mid - l1
        rightSize = r1 - (inorder_mid + 1)

        root.left = self.traverse(inorder, l1, l1+leftSize ,postorder, l2, l2+leftSize)
        root.right = self.traverse(inorder, inorder_mid+1, r1, postorder, l2+leftSize, r2-1 )

        return root