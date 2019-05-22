class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if not image or not image[0]:
            return
        n = len(image)
        m = len(image[0])
        self.dfs(image, sr, sc, n, m, newColor, image[sr][sc])
        return image
                
    def dfs(self, image, x, y, n, m, nc, initial):
        if x < 0 or y < 0 or x >= n or y >= m or image[x][y] != initial or image[x][y] == nc:
            return
        image[x][y] = nc
        self.dfs(image, x + 1, y, n, m, nc, initial)
        self.dfs(image, x - 1, y, n, m, nc, initial)
        self.dfs(image, x, y + 1, n, m, nc, initial)
        self.dfs(image, x, y - 1, n, m, nc, initial)

# s = Solution()
# print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
s1 = Solution()
print(s1.floodFill([[0,0,0],[0,1,1]], 1, 1, 1))
