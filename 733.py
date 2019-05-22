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
        self.dfs(image, sr, sc, n, m, newColor)
        return image
                
    def dfs(self, image, x, y, n, m, nc):
        if x < 0 or y < 0 or x >= n or y >= m or image[x][y] == nc:
            return
        image[x][y] = nc
        self.dfs(image, x + 1, y, n, m, nc)
        self.dfs(image, x - 1, y, n, m, nc)
        self.dfs(image, x, y + 1, n, m, nc)
        self.dfs(image, x, y - 1, n, m, nc)