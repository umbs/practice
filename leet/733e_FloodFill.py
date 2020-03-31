class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def dfs(r, c):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != oldColor:
                return
            
            image[r][c] = newColor
            for (x,y) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                dfs(r+x, c+y)

        oldColor = image[sr][sc]
        if image[sr][sc] != newColor:
            dfs(sr, sc)
        
        return image
