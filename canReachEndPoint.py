class Solution:
    """
    @param map: the map
    @return: can you reach the endpoint
    """
    def reachEndpoint(self, map):
        # Write your code here
        
        return self.bfs(map, 0, 0)

    def bfs(self, map, i, j):
        if i < 0 or i >= len(map) or j < 0 or j >= len(map[0]) or map[i][j] == 0 or map[i][j] == 2:
            return False
        
        if map[i][j] == 9:
            return True

        map[i][j] = 2

        return self.bfs(map, i + 1, j) or \
               self.bfs(map, i - 1, j) or \
               self.bfs(map, i, j + 1) or \
               self.bfs(map, i, j - 1)