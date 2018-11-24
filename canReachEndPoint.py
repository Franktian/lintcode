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

    def reachEndpointBFS(map):
        queue = [[0, 0]]
        m = len(map)
        n = len(map[0])
        distance =[[m * n for x in range(n)] for y in range(m)]
        distance[0][0] = 0

        dirs = ((-1, 0),(0, 1), (0, -1),(1, 0))
        while queue:
            i, j = queue.pop(0)

            if map[i][j] == 9:
                return distance[i][j]

            map[i][j] = 2
            for x, y in dirs:
                row = i + x
                col = j + y

                if 0 <= row < m and 0 <= col < n and map[row][col] != 0 and map[row][col] != 2:
                    queue.append([row, col])
                    distance[row][col] = distance[i][j] + 1
        return -1
