class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original is None:
            return None
        
        if target == original:
            return cloned
        
        if original.left:
            result = self.getTargetCopy(original.left, cloned.left, target)
            
            if result:
                return result
        
        if original.right:
            result = self.getTargetCopy(original.right, cloned.right, target)
            
            if result:
                return result
        
        return None
        
