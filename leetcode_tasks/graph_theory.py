import math
from collections import deque
from queue import Queue

"""
733. Flood Fill
Easy

An image is represented by an m x n integer grid image where image[i][j]
represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform
a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels
connected 4-directionally to the starting pixel of the same color as
the starting pixel, plus any pixels connected 4-directionally to those
pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Example 1:
Input: image = [[1,1,1],
                [1,1,0],
                [1,0,1]],
                sr = 1, sc = 1, color = 2

Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1)
(i.e., the red pixel), all pixels connected by a path of the same color as
the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally
connected to the starting pixel.
"""


class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        R, C = len(image), len(image[0])
        start_color = image[sr][sc]
        if start_color == color:
            return image

        def dfs(r, c):
            if image[r][c] == start_color:
                image[r][c] = color
                if r >= 1: dfs(r - 1, c)
                if r + 1 < R: dfs(r + 1, c)
                if c >= 1: dfs(r, c - 1)
                if c + 1 < C: dfs(r, c + 1)

        dfs(sr, sc)
        return image

        # checked = []
        # start_color = image[sr][sc]
        # lst = []
        # if color == start_color:
        #     return image
        #
        # def find_neighbor(tup):
        #     sr, sc = tup
        #
        #     if sc > 0 and image[sr][sc - 1] == start_color:
        #         image[sr][sc - 1] = color
        #         lst.append((sr, sc - 1))
        #     if sc < len(image[sr]) - 1 and image[sr][sc + 1] == start_color:
        #         image[sr][sc + 1] = color
        #         lst.append((sr, sc + 1))
        #     if sr > 0 and image[sr - 1][sc] == start_color:
        #         image[sr - 1][sc] = color
        #         lst.append((sr - 1, sc))
        #     if sr < len(image) - 1 and image[sr + 1][sc] == start_color:
        #         image[sr + 1][sc] = color
        #         lst.append((sr + 1, sc))
        #
        #     image[sr][sc] = color
        #     checked.append((sr, sc))
        #     return lst
        #
        # find_neighbor((sr, sc))
        # for el in lst:
        #     if el not in checked:
        #         find_neighbor(el)
        # return image


sol = Solution()

res = sol.floodFill([[0, 0, 0], [0, 0, 0]], 1, 0, 2)
assert res == [[2, 2, 2], [2, 2, 2]], res

res = sol.floodFill(image=[[0, 0, 0], [0, 0, 0]], sr=0, sc=0, color=0)
assert res == [[0, 0, 0], [0, 0, 0]], res

res = sol.floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2)
assert res == [[2, 2, 2], [2, 2, 0], [2, 0, 1]], res

"""
200. Number of Islands
Medium

Given an m x n 2D binary grid grid which represents a map of '1's 
(land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent
 lands horizontally or vertically. You may assume all four edges of 
 the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

or
[
["1","1","0","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","1"]
]
"""


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        row_last = len(grid) - 1
        col_last = len(grid[0]) - 1
        count = 0

        def dfs(r, c):
            if grid[r][c] == '1':
                grid[r][c] = 'ok'  # заменим уже пройденные, а то по времени не пролезть
                if c > 0:
                    dfs(r, c - 1)
                if c < col_last:
                    dfs(r, c + 1)
                if r > 0:
                    dfs(r - 1, c)
                if r < row_last:
                    dfs(r + 1, c)
            return

        for i in range(row_last + 1):
            for j in range(col_last + 1):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count


sol = Solution()
res = sol.numIslands(
    [["1", "1", "1", "1", "0"],
     ["1", "1", "0", "1", "0"],
     ["1", "1", "0", "0", "0"],
     ["0", "0", "0", "0", "0"]])
assert res == 1, res

res = sol.numIslands(
    [["1", "1", "0", "0", "0"],
     ["1", "1", "0", "0", "0"],
     ["0", "0", "1", "0", "0"],
     ["0", "0", "0", "1", "1"]])
assert res == 3, res

"""
695. Max Area of Island
Medium

You are given an m x n binary matrix grid. An island is a group of 1's 
(representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""


class Solution:
    def maxAreaOfIsland(self, grid: list[list[str]]) -> int:
        # var1: рекурсивный подход:
        # row_last = len(grid) - 1
        # col_last = len(grid[0]) - 1
        # max_count = 0
        #
        # def dfs(r, c):
        #     num = 0
        #     if grid[r][c] == 1:
        #         grid[r][c] = 11  # заменим уже пройденные, а то по времени не пролезть
        #         num = 1
        #         if c > 0:
        #             num += dfs(r, c - 1)
        #         if c < col_last:
        #             num += dfs(r, c + 1)
        #         if r > 0:
        #             num += dfs(r - 1, c)
        #         if r < row_last:
        #             num += dfs(r + 1, c)
        #     return num
        #
        # for i in range(row_last + 1):
        #     for j in range(col_last + 1):
        #         if grid[i][j] == 1:
        #             count = dfs(i, j)
        #             if max_count < count:
        #                 max_count = count
        # return max_count

        # var2: итеративный подход, здесь мы не зависим от переполнения стека из-за рекурсий:
        seen = set()
        ans = 0
        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):
                if val and (r0, c0) not in seen:
                    shape = 0
                    stack = [(r0, c0)]
                    seen.add((r0, c0))
                    while stack:
                        r, c = stack.pop()
                        shape += 1
                        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                    and grid[nr][nc] and (nr, nc) not in seen):
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    ans = max(ans, shape)
        return ans


sol = Solution()
res = sol.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                           [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                           [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]])
assert res == 6, res

"""
1254. Number of Closed Islands
Medium

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a 
maximal 4-directionally connected group of 0s and a closed island is an 
island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

Example 1:

Input:  grid = [[1,1,1,1,1,1,1,0],
                [1,0,0,0,0,1,1,0],
                [1,0,1,0,1,1,1,0],
                [1,0,0,0,0,1,0,1],
                [1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
"""


class Solution:
    def closedIsland(self, grid: list[list[int:]]) -> int:
        # var1: рекурсивный подход:
        # row_last = len(grid) - 1
        # col_last = len(grid[0]) - 1
        # count = 0
        #
        # def dfs(r, c):
        #     num = 0
        #     if grid[r][c] == 0:
        #         if r == 0 or r == row_last or c == 0 or c == col_last:
        #             num = 1  # if meet boundary at least once
        #         else:
        #             grid[r][c] = 'ok'
        #             if c > 0:
        #                 num += dfs(r, c - 1)
        #             if c < col_last:
        #                 num += dfs(r, c + 1)
        #             if r > 0:
        #                 num += dfs(r - 1, c)
        #             if r < row_last:
        #                 num += dfs(r + 1, c)
        #     return num
        #
        # for i in range(row_last + 1):
        #     for j in range(col_last + 1):
        #         if grid[i][j] == 0:
        #             res = dfs(i, j)
        #             if not res:
        #                 count += 1
        # return count

        # var2: итеративный подход, здесь мы не зависим от переполнения стека из-за рекурсий:
        seen = set()
        count = 0
        for r1 in range(len(grid)):
            for c1 in range(len(grid[0])):
                at_boundary = 0
                if grid[r1][c1] == 0 and (r1, c1) not in seen:
                    stack = [(r1, c1)]
                    seen.add((r1, c1))
                    num = 0
                    while stack:
                        r, c = stack.pop()
                        for nr, nc in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                            if (nr, nc) not in seen:
                                if nr in (-1, len(grid)) or nc in (-1, len(grid[0])):
                                    at_boundary = 1  # note if come to boundary
                                else:
                                    if grid[nr][nc] == 0:
                                        stack.append((nr, nc))
                                        seen.add((nr, nc))
                                    num = 1
                    if num and not at_boundary:
                        count += 1
        return count


sol = Solution()

res = sol.closedIsland(
    [[0, 1, 1, 1, 0],
     [1, 0, 1, 0, 1],
     [1, 0, 1, 1, 1],
     [1, 1, 1, 0, 1],
     [0, 1, 0, 1, 0]])
assert res == 3, res

res = sol.closedIsland(
    [[0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0],
     [0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0],
     [0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
     [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1],
     [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
     [0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
     [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
     [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1],
     [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
     [1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0]])
assert res == 14, res

res = sol.closedIsland(
    [[0, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 1, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 1, 0, 1],
     [0, 1, 0, 0, 0, 1, 0, 1],
     [1, 0, 0, 1, 0, 1, 0, 1],
     [1, 1, 1, 1, 0, 0, 1, 1],
     [1, 0, 0, 0, 0, 0, 1, 1],
     [0, 1, 1, 1, 1, 1, 1, 1]])
assert res == 1, res

res = sol.closedIsland(
    [[1, 1, 1, 1, 1, 1, 1, 0],
     [1, 0, 0, 0, 0, 1, 1, 0],
     [1, 0, 1, 0, 1, 1, 1, 0],
     [1, 0, 0, 0, 0, 1, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 0]])
assert res == 2, res

"""
1020. Number of Enclaves
Medium

You are given an m x n binary matrix grid, where 0 represents 
a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent 
(4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off 
the boundary of the grid in any number of moves.
"""


class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        # var2: итеративный подход
        count = 0
        seen = set()
        for r1 in range(len(grid)):
            for c1 in range(len(grid[0])):
                if grid[r1][c1] == 1 and (r1, c1) not in seen:
                    stack = [(r1, c1)]
                    seen.add((r1, c1))
                    at_boundary = 0
                    num = 1
                    while stack:
                        r, c = stack.pop()
                        for nr, nc in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                            if (nr, nc) not in seen:
                                if nr in (-1, len(grid)) or nc in (-1, len(grid[0])):
                                    at_boundary = 1
                                else:
                                    if grid[nr][nc] == 1:
                                        stack.append((nr, nc))
                                        seen.add((nr, nc))
                                        num += 1
                    if num and not at_boundary:
                        count += num
                    else:
                        num = 0
        return count


sol = Solution()

res = sol.numEnclaves(
    [[0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1], [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0],
     [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1], [0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
     [0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
     [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1]]

)
assert res == 7, res

res = sol.numEnclaves(
    [[0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
     [1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
     [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
     [0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
     [0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
     [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
     [0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
     [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
     [1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 0, 0, 0, 1]]
)
assert res == 3, res

res = sol.numEnclaves(
    [[0, 0, 0, 0],
     [1, 0, 1, 0],
     [0, 1, 1, 0],
     [0, 0, 0, 0]])
assert res == 3, res

res = sol.numEnclaves(
    [[0, 1, 1, 0],
     [0, 0, 1, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 0]])
assert res == 0, res

"""
1905. Count Sub Islands
Medium

You are given two m x n binary matrices grid1 and grid2 containing only 0's 
(representing water) and 1's (representing land). An island is a group of 1's 
connected 4-directionally (horizontal or vertical). Any cells outside of the 
grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 
that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

Example 1:

Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], 
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid 
on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. 
There are three sub-islands.
"""


class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        # var2: итеративный подход
        seen = set()
        amount = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1 and (i, j) not in seen:
                    stack = [(i, j)]
                    seen.add((i, j))
                    count_one = 0
                    wrong = 0

                    while stack:
                        r, c = stack.pop()
                        if grid1[r][c] == 0:
                            wrong += 1
                        for (nr, nc) in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                            if nr not in (-1, len(grid2)) and nc not in (-1, len(grid2[0])):
                                if (nr, nc) not in seen:
                                    if grid2[nr][nc] == 1:
                                        stack.append((nr, nc))
                                        seen.add((nr, nc))
                                        if grid1[nr][nc] == 0:
                                            wrong += 1
                    count_one += 1
                    if not wrong:
                        amount += count_one
        return amount


sol = Solution()

res = sol.countSubIslands(grid1=[[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]],
                          grid2=[[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]])
assert res == 3, res

"""
1162. As Far from Land as Possible
Medium

Given an n x n grid containing only values 0 and 1, where 0 
represents water and 1 represents land, find a water cell such 
that its distance to the nearest land cell is maximized, and 
return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance 
between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

Example 1:

Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.

Example 2:
"""


class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dist = 0
        deq = deque((i, j) for i in range(n) for j in range(n) if grid[i][j] == 1)  # list of lands
        if len(deq) == 0 or len(deq) == n * n:  # no land or no water
            return -1

        while deq:
            for _ in range(len(deq)):  # check one level per cycle (bfs)
                r, c = deq.popleft()
                for (nr, nc) in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:  # index is not out of range
                        deq.append((nr, nc))  # add to deq to check in next cycle
                        grid[nr][nc] = 1  # 1 means is checked
            dist += 1
        return dist - 1


# One way is to think of the matrix as a graph.
# At the first level we have all the cells that are land.
# The next level consists of water cells that are reachable
# at a distance of 1. The level next to that is reachable
# at a distance of 2 and so on.

# first level:  [(0, 0), (0, 2), (2, 0), (2, 2)]
# second level: [(1, 0), (0, 1), (1, 2), (2, 1)]
# third level:  [(1, 1)]


sol = Solution()

res = sol.maxDistance([[1, 0, 1],
                       [0, 0, 0],
                       [1, 0, 1]])
assert res == 2, res

res = sol.maxDistance([[1, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]])
assert res == 4, res

"""
417. Pacific Atlantic Water Flow
Medium

There is an m x n rectangular island that borders both the Pacific 
Ocean and Atlantic Ocean. The Pacific Ocean touches the island's 
left and top edges, and the Atlantic Ocean touches the island's 
right and bottom edges.

The island is partitioned into a grid of square cells. You are given 
an m x n integer matrix heights where heights[r][c] represents the 
height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to 
neighboring cells directly north, south, east, and west if the 
neighboring cell's height is less than or equal to the current 
cell's height. Water can flow from any cell adjacent to an ocean 
into the ocean.

Return a 2D list of grid coordinates result where 
result[i] = [ri, ci] denotes that rain water can flow from 
cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:

Input: heights = 
[[1,2,2,3,5],
 [3,2,3,4,4],
 [2,4,5,3,1],
 [6,7,1,4,5],
 [5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

"""


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        len_matrix = len(heights)
        len_row = len(heights[0])

        def dfs(r, c):
            flow_path.add((r, c))
            for (nr, nc) in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                if 0 <= nr < len_matrix and 0 <= nc < len_row and \
                        heights[r][c] <= heights[nr][nc] and (nr, nc) not in flow_path:
                    flow_path.add((nr, nc))
                    dfs(nr, nc)

        pacific_border = set((i, 0) for i in range(len_matrix))
        border2 = set((0, i) for i in range(len_row))
        pacific_border.update(border2)
        flow_path = set()
        for (r, c) in pacific_border:
            dfs(r, c)
        pacific_path = flow_path

        atlantic_border = set((i, len_row - 1) for i in range(len_matrix))
        border2 = set((len_matrix - 1, i) for i in range(len_row))
        atlantic_border.update(border2)
        flow_path = set()
        for (r, c) in atlantic_border:
            dfs(r, c)
        atlantic_path = flow_path

        common = list(pacific_path.intersection(atlantic_path))
        return common


sol = Solution()

# res = sol.pacificAtlantic([[1, 1], [1, 1], [1, 1]])
# assert res == [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)], res
#
# res = sol.pacificAtlantic([[1, 2, 2, 3, 5],
#                            [3, 2, 3, 4, 4],
#                            [2, 4, 5, 3, 1],
#                            [6, 7, 1, 4, 5],
#                            [5, 1, 1, 2, 4]])
# assert res == [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]], res


"""
"""


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid) - 1
        seen = set()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, -1), (-1, 1), (1, 1))

        if grid[0][0] == 0:
            deq = deque()
            deq.append((0, 0))
            count = 0
        else:
            return -1

        def bfs(r, c):
            # for (nr, nc) in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1), (r + 1, c - 1), (r + 1, c + 1), (
            # r - 1, c - 1), (r - 1, c + 1):
            for (dr, dc) in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr <= n and 0 <= nc <= n and grid[nr][nc] == 0 and (nr, nc) not in seen:
                    deq.append((nr, nc))
                    seen.add((nr, nc))

        while deq:
            count += 1
            for _ in range(len(deq)):
                r, c = deq.popleft()
                seen.add((r, c))

                if r == n and c == n:
                    return count
                else:
                    bfs(r, c)
        return -1


sol = Solution()

res = sol.shortestPathBinaryMatrix([[0, 1], [1, 1]])
assert res == -1, res

res = sol.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]])
assert res == 4, res

res = sol.shortestPathBinaryMatrix([[0, 1], [1, 0]])
assert res == 2, res

res = sol.shortestPathBinaryMatrix([[0, 0, 0], [0, 1, 0], [0, 1, 0]])
assert res == 4, res

res = sol.shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]])
assert res == -1, res

"""
542. 01 Matrix
Medium

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
"""
"""
решение:
проходим циклом и добавляем в дек все клетки с 0
если в клетке не 0 - заменяем на -1 т о  помечая 
непроверенные.
затем берем клетки с начала дека. если там -1 то 
записываем значение родитель + 1 и добавляем в дек
идем до конца дека
так сохраняем значение в клетках(самое сложное оказалось для меня)

"""


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        direction = ((0, -1), (1, 0), (0, 1), (-1, 0))
        deq = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    deq.append((i, j))
                else:
                    mat[i][j] = -1  # not checked

        while deq:
            # тк очередь из 0 то когда в соседях находится -1(непроверенный)
            # то значит это 0+1
            # потом в очередь попадет 1 и его сосед будет 1+1=2  итд
            r, c = deq.popleft()
            for (dr, dc) in direction:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if mat[nr][nc] == -1:
                        mat[nr][nc] = mat[r][c] + 1
                        deq.append((nr, nc))
        return mat

        # v2 dinamic programming approach:
        # m, n = len(mat), len(mat[0])
        #
        # for r in range(m):
        #     for c in range(n):
        #         if mat[r][c] > 0:
        #             top = mat[r - 1][c] if r > 0 else math.inf
        #             left = mat[r][c - 1] if c > 0 else math.inf
        #             mat[r][c] = min(top, left) + 1
        #
        # for r in range(m - 1, -1, -1):
        #     for c in range(n - 1, -1, -1):
        #         if mat[r][c] > 0:
        #             bottom = mat[r + 1][c] if r < m - 1 else math.inf
        #             right = mat[r][c + 1] if c < n - 1 else math.inf
        #             mat[r][c] = min(mat[r][c], bottom + 1, right + 1)
        #
        # return mat


sol = Solution()

res = sol.updateMatrix([[0, 0, 0],
                        [0, 1, 0],
                        [1, 1, 1]])
assert res == [[0, 0, 0], [0, 1, 0], [1, 2, 1]], res

"""
934. Shortest Bridge
Medium

You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

"""


class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        # n = len(grid)
        # deq = deque()
        # directions = ((0, -1), (1, 0), (0, 1), (-1, 0))
        # count = 0
        # seen = set()
        # k = 0
        #
        # # find first cell of first island:
        # for i in range(n):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             deq.append((i, j))
        #             break
        #     if deq:
        #         break
        #
        # # find whole first island:
        # while True:
        #     try:
        #         r, c = deq[k]
        #         seen.add((r, c))
        #         for (dr, dc) in directions:
        #             nr, nc = r + dr, c + dc
        #             if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1 and (nr, nc) not in seen:
        #                 deq.append((nr, nc))
        #         k += 1
        #     except IndexError:
        #         break
        #
        # # find second island:
        # while deq:
        #     for _ in range(len(deq)):
        #         r, c = deq.popleft()
        #         seen.add((r, c))
        #         for (dr, dc) in directions:
        #             nr, nc = r + dr, c + dc
        #             if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen:
        #                 if grid[nr][nc] == 0:
        #                     deq.append((nr, nc))
        #                 else:
        #                     return count
        #     count += 1
        # return count

        # ver2 without deque:
        n = len(grid)
        deq = deque()
        directions = ((0, -1), (1, 0), (0, 1), (-1, 0))
        count = 0
        seen = set()
        k = 0
        start_cell = False

        # find first cell of first island:
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 2
                    start_cell = (i, j)
                    break
            if start_cell:
                break

        # find whole first island:
        def dfs(r, c):
            for (dr, dc) in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    dfs(nr, nc)

        def bfs(r, c):
            for (dr, dc) in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = -1
                    if grid[nr][nc] == 1:
                        return


        i, j = start_cell
        dfs(i, j)

        # find second island:
        for r in range(i, n):
            for j in range(j, n):
                bfs(i, j)


sol = Solution()

res = sol.shortestBridge(
    [[0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 0, 0]]
    )
assert res == 2, res

res = sol.shortestBridge([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]])
assert res == 1, res

res = sol.shortestBridge([[0, 1], [1, 0]])
assert res == 1, res

res = sol.shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]])
assert res == 2, res

"""
797. All Paths From Source to Target
Medium

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, 
find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit 
from node i (i.e., there is a directed edge from node i to node graph[i][j]).

Example 1:

Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Example 2:

Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

Constraints:

    n == graph.length
    2 <= n <= 15
    0 <= graph[i][j] < n
    graph[i][j] != i (i.e., there will be no self-loops).
    All the elements of graph[i] are unique.
    The input graph is guaranteed to be a DAG.
"""


class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        """bfs approach"""
        # deq = deque([[0]])
        # res = []
        # while deq:
        #     path = deq.popleft()
        #     if path[-1] == len(graph) - 1:
        #         res.append(path)
        #     else:
        #         for el in graph[path[-1]]:
        #             deq.append(path + [el])
        # return res
        '''
        path = [0], [0, 1], [0, 2], [0, 1, 3], [0, 2, 3]
        '''

        # var2:
        """dfs approach"""

        def dfs(path):
            if path[-1] == len(graph) - 1:
                res.append(path)
                return
            else:
                for el in graph[path[-1]]:
                    dfs(path + [el])

        res = []
        dfs([0])
        return res


'''
path = [0], [0, 1], [0, 1, 3]
path = [0], [0, 2], [0, 2, 3]
'''

sol = Solution()

res = sol.allPathsSourceTarget([[1, 2], [3], [3], []])
# assert res == [[0, 1, 3], [0, 2, 3]], res

"""
"""


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        # keys = [0]
        # for i in range(len(rooms)):
        #     if i > 0:
        #         if i not in keys:
        #             return False
        #     if rooms[i]:
        #         keys.extend(rooms[i])
        # return True
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]
        # At the beginning, we have a todo list "stack" of keys to use.
        # 'seen' represents at some point we have entered this room.
        while stack:  # While we have keys...
            node = stack.pop()  # get the next key 'node'
            for nei in rooms[node]:  # For every key in room # 'node'...
                if not seen[nei]:  # ... that hasn't been used yet
                    seen[nei] = True  # mark that we've entered the room
                    stack.append(nei)  # add the key to the todo list
        return all(seen)  # Return true iff we've visited every room


sol = Solution()

res = sol.canVisitAllRooms([[1, 3], [1, 4], [2, 3, 4, 1], [], [4, 3, 2]])
assert res is True, res

res = sol.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]])
assert res is False, res

"""
"""
