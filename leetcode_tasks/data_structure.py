from collections import Counter, defaultdict

"""
53. Maximum Subarray
Medium

Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # суть решения в том что храним максимальную сумму подмассива max_sum
        # и сравниваем ее с параллельно вычисляемой текущей суммой cur_sum
        # если текущее значение cur_sum больше максимального max_sum - обновляем max_sum
        # в cur_sum сохр текущее вычисление, оно то увеличивается то уменьшается.
        # если к cur_sum прибавили nums[i] и получилось все равно меньше чем nums[i]
        # то отбрасываем пред значение cur_sum(те элементы не войдут в subarray with the largest sum)
        # и делаем cur_sum = nums[i] (будем считать сумму от элемента nums[i])
        max_sum, cur_sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            cur_sum += nums[i]
            if cur_sum < nums[i]:
                # then not include item in subarray
                cur_sum = nums[i]
            if max_sum < cur_sum:
                # max_sum is maximum of cur_sum values
                max_sum = cur_sum
        return max_sum


sol = Solution()

res = sol.maxSubArray([-1])
assert res == -1, res

res = sol.maxSubArray([4, -1, 2, -1])
assert res == 5, res

res = sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
assert res == 6, res

"""
1. Two Sum
Easy

Given an array of integers nums and an integer target, return indices of 
the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you 
may not use the same element twice.

You can return the answer in any order.
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic_nums = {}
        # создали словарь чтобы бегать по нему
        # вместо списка - экономить время
        # иначе было бы O(n2)
        for i in range(len(nums)):
            if target - nums[i] in dic_nums:  # O(1)
                return [dic_nums[target - nums[i]], i]
            else:
                dic_nums[nums[i]] = i


sol = Solution()

res = sol.twoSum([3, 3], 6)
assert res == [0, 1], res

res = sol.twoSum([3, 2, 4], 6)
assert res == [1, 2], res

res = sol.twoSum([2, 7, 11, 15], 9)
assert res == [0, 1], res

"""
88. Merge Sorted Array
Easy

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored 
inside the array nums1. To accommodate this, nums1 has a length of m + n, where the 
first m elements denote the elements that should be merged, and the last n elements 
are set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
"""


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int):
        # суть в том что бы одновременно пройти два массива(два указателя)
        # и либо сразу вставлять значения на свои места в nums1,
        # либо просто вставить в nums1 а потом отсортировать полученный массив

        # вариант 1:
        # by use two pointers and sorting:
        # k = 0
        # for i in range(m, len(nums1)):
        #     if nums1[i] == 0 and k <= n:
        #         nums1[i] = nums2[k]
        #         k += 1

        # вариант 2 но сортировка такая же:
        # nums1[m:] = nums2[:n]  так короче и быстрее
        #  In slow languages like python, offloading the heavy lifting
        #  to an underlying module written in a low level language like
        #  C will often be faster
        # nums1.sort()

        # вариант 3:
        # сравнение значений в конце массивов и подстановка соответствующих(одновременно):
        # [1, 2, 3, 0, 0] [2, 5] m=3, n=2
        while n > 0 and m > 0:
            # находим больший элемент и отправляем его в конец массива:
            if nums1[m - 1] < nums2[n - 1]:
                nums1[n + m - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[n + m - 1] = nums1[m - 1]
                m -= 1
        # если m=0 а n=1 то делаем копию списка от 0 до n:
        if n > 0:
            nums1[:n] = nums2[:n]  # в отличие от nums1 = nums2 создаст объект(копию)
            # а не ссылку на тот же объект
            # nums1 = nums2
            # print(id(nums1))
            # print(id(nums2))
        return nums1


sol = Solution()
res = sol.merge(nums1=[0], m=0, nums2=[1], n=1)
assert res == [1], res

res = sol.merge([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3)
assert res == [-1, 0, 0, 1, 2, 2, 3, 3, 3], res

res = sol.merge(nums1=[1, 2, 3, 0, 0], m=3, nums2=[2, 5], n=2)
assert res == [1, 2, 2, 3, 5], res

res = sol.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
assert res == [1, 2, 2, 3, 5, 6], res

"""
350. Intersection of Two Arrays II
Easy

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both 
arrays and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

!!! Нужно не пересечение массивов выдать а просто собрать массив с общими элементами где порядок не важен !!!
"""


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # nums1 = dict(Counter(nums1))
        # nums2 = dict(Counter(nums2))
        # if len(nums2) < len(nums1):
        #     nums1, nums2 = nums2, nums1
        # lst2 = list(nums2.keys())
        # lst2.sort()
        # lst = []
        # for k, v in nums1.items():
        #     f = 0
        #     l = len(nums2) - 1
        #     while f <= l:
        #         m = (f + l) // 2
        #         if lst2[m] == k:
        #             lst.extend([k for i in range(min(nums2[k], nums1[k]))])
        #             f = m + 1
        #         elif lst2[m] < k:
        #             f = m + 1
        #         else:
        #             l = m - 1
        # return lst

        # var2 - two counters:
        """
        суть:
        идем по обоим массивам сначала сравнивая элементы.
        если у первого массива элемент больше то увеличиваем счетчик второго
        если теперь у второго больше - увеличиваем счетчик первого
        если наконец равны - добавляем в конечный список и т д.
        """
        nums1.sort()
        nums2.sort()

        ans = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1
        return ans


sol = Solution()

res = sol.intersect([4, 9, 5, 1], nums2=[9, 4, 5, 9, 8, 4, 1])
# assert res == [9, 4, 5, 1], res
# assert res == [4, 9, 5, 1], res


"""
121. Best Time to Buy and Sell Stock
Easy

You are given an array prices where prices[i] is the price of a given 
tock on the ith day.
You want to maximize your profit by choosing a single day to buy one 
stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If 
you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_p = 0
        min_p = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min_p:
                min_p = prices[i]
            elif prices[i] > max_p:
                max_p = prices[i]
        return max_p - min_p if max_p else 0


# sol = Solution()
# res = sol.maxProfit([7, 6, 4, 3, 1])
# assert res == 0, res
#
# res = sol.maxProfit([7, 1, 5, 3, 6, 4])
# assert res == 5, res

"""
566. Reshape the Matrix
Easy

In MATLAB, there is a handy function called reshape which can reshape
an m x n matrix into a new one with a different size r x c keeping 
its original data.
You are given an m x n matrix mat and two integers r and c representing 
the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original 
matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output 
the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:
Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
"""


class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        # если кол-во items останется тем же в новой форме матрицы, то меняем:
        if m * n == r * c:
            mat_2 = []
            lst = []
            col = 0
            for i in range(m):
                for j in range(n):
                    lst.append(mat[i][j])
                    col += 1  # число колонок n,c разное, поэтому добавляем счетчик на новые колонки
                    # при этом кол-во строк считать не нужно п ч мы проверили общее кол-во в начале.
                    # если заданное условием кол-во колонок заполнилось, переходим к след строке:
                    if col == c:
                        mat_2.append(lst)
                        lst = []
                        col = 0
            return mat_2
        else:
            return mat

        # # var 2:
        # # распаковываем матрицу в список:
        # nums = sum(mat, [])  # extend list
        # if len(nums) != r * c:
        #     return mat
        # tuples = [*zip(*([iter(nums)] * c))]  # в зип передается кол-во итераторов равное кол-ву колонок
        # # распаковка итератора [*iter(nums)]
        # mat2 = [*map(list, tuples)]  # превратили кортежи в списки и распаковали генератор в список
        # return mat2

        # var 3:
        # if r * c != len(mat) * len(mat[0]):
        #     return mat
        # else:
        #     # распаковываем матрицу в список:
        #     lst = [y for x in mat for y in x]
        #     # [число для строки в матрице для числа в строке]
        #     return [lst[i * c: ((i + 1) * c)] for i in range(r)]
        #     # берем срезы lst[1*3: 1+1*3] => lst[3:6], lst[6:9] и т д
        #     # и заполняем ими матрицу


sol = Solution()

res = sol.matrixReshape([[1, 2], [3, 4], [5, 6]], 2, 3)
assert res == [[1, 2, 3], [4, 5, 6]], res

"""
118. Pascal's Triangle
Easy

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers 
directly above it as shown:
   [[1],
   [1,1],
  [1,2,1],
 [1,3,3,1],
[1,4,6,4,1]]

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
"""


# append быстрее тк не создает нового списка в отличие от конкатенации!!
# [1, 1, 0] + [0, 1, 1] => [1, 1, 0, 0, 1, 1]

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]
        for i in range(1, numRows):
            temp1 = res[-1] + [0]  # [1, 1] + [0] = [1, 1, 0]
            temp2 = [0] + res[-1]  # [0] + [1, 1] = [0, 1, 1]
            res.append([temp1[i] + temp2[i] for i in range(len(temp1))])
            # res.append(list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])))  # [1, 0] + [0, 1] => [1, 1]
        return res[:numRows]

        # так мне более понятно:
        # lst = [1]
        # mat = [lst]
        # for i in range(1, numRows):
        #     part1 = lst + [0]
        #     part2 = [0] + lst
        #     lst = [part1[i] + part2[i] for i in range(len(part1))]
        #     mat.append(lst)
        # return mat


sol = Solution()

res = sol.generate(5)
assert res == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]], res

"""
36. Valid Sudoku
Medium

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells 
need to be validated according to the following rules:
    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the 
    digits 1-9 without repetition.

Note:
    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left 
corner being modified to 8. Since there are two 8's in the top left 
3x3 sub-box, it is invalid.
"""


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # решила верно и логически. но очень долго думала
        # нужно постараться до конца довести решение в голове
        # потом записывать, а мне не хватает внимания и я начинаю писать код
        # в надежде что по ходу прояснится но начинаю плутать
        # несложное вычисление квадратов зяняло много времени
        # маленькие подзадачки может стоит и подсмотреть и потратить это время на действительно важное
        #     m = len(board)
        #     n = len(board[0])
        #     dic = {}
        #     for r in range(m):
        #         for c in range(n):
        #             num = board[r][c]
        #             if num != '.':
        #                 q = self.find_square_num(r, c)
        #                 st = {f'r{r}', f'c{c}', f'q{q}'}
        #                 if num in dic:
        #                     if not dic[num].isdisjoint(st):
        #                         return False
        #                     dic[num] = dic[num].union(st)
        #                 else:
        #                     dic[num] = st
        #     return True
        #
        # def find_square_num(self, row, col):
        #     # вычисляет квадрато одним номером 0 - 8
        #     ans = (row//3)*3 + col//3
        #     return ans

        # вар 2(не мой):
        # return 1 == max(Counter(x
        #                         for i, row in enumerate(board)
        #                         for j, c in enumerate(row)
        #                         if c != '.'
        #                         for x in ((c, i), (j, c), (i / 3, j / 3, c))
        #                         ).values() + [1])

        # вар 3(для понимания, не мой):
        # для определения квадратов:
        # 0 // 3 = 0
        # 1 // 3 = 0
        # 2 // 3 = 0 - для обычных строк 0,1,2 строка квадратов будет 0
        # 3 // 3 = 1
        # 4 // 3 = 1
        # 5 // 3 = 1 - для обычных строк 3,4,5 строка квадратов будет 1
        # 6 // 3 = 2
        # 7 // 3 = 2
        # 8 // 3 = 2 - для обычных строк 6,7,8 строка квадратов будет 3
        """
        [[[0,1,2], [0,1,2], [0,1,2]],  - строка квадратов 0
        [[0,1,2], [0,1,2], [0,1,2]],   - строка квадратов 1
        [[0,1,2], [0,1,2], [0,1,2]]]   - строка квадратов 2
        """
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]

        for x in range(9):
            for y in range(9):
                cell_value = board[x][y]
                if cell_value == ".":
                    continue
                if cell_value in rows[x] or cell_value in columns[y] or cell_value in squares[x // 3][y // 3]:
                    # числа записываем в список множеств, индекс (множество) определяется
                    # номером строки или столбца или квадрата
                    # т е в rows[x] собирается все из строки х
                    # квадрат обозначен по x и y т е строка 0 с квадратами 0,1,2 строка 1 с квадратами 0,1,2
                    # квадраты это список из списков(х 3строки, у 3строки)
                    return False

                rows[x].add(cell_value)
                columns[y].add(cell_value)
                squares[x // 3][y // 3].add(cell_value)

        return True


sol = Solution()
res = sol.isValidSudoku([[".", ".", "4", ".", ".", ".", "6", "3", "."],
                         [".", ".", ".", ".", ".", ".", ".", ".", "."],
                         ["5", ".", ".", ".", ".", ".", ".", "9", "."],
                         [".", ".", ".", "5", "6", ".", ".", ".", "."],
                         ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
                         [".", ".", ".", "7", ".", ".", ".", ".", "."],
                         [".", ".", ".", "5", ".", ".", ".", ".", "."],
                         [".", ".", ".", ".", ".", ".", ".", ".", "."],
                         [".", ".", ".", ".", ".", ".", ".", ".", "."]])
assert res is False, res

res = sol.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
assert res is True, res

res = sol.isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."]
                            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
assert res is False, res

"""
387. First Unique Character in a String
Easy

Given a string s, find the first non-repeating character in it 
and return its index. If it does not exist, return -1.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # var 1: just dict
        # dct = {}
        # k = 0
        # for letter in s:
        #     if letter not in dct:
        #         dct[letter] = 1
        #     else:
        #         dct[letter] += 1
        # for el in s:
        #     if dct[el] == 1:
        #         return k
        #     k += 1
        # return -1

        # var 2 Counter from collections:
        # dct = Counter(s)
        # i = 0
        # for el in s:
        #     if dct[el] == 1:
        #         return i
        #     i += 1
        # return -1

        # var 3 built-ins count and index:
        """
        очень быстрый благодаря встроенным count и index
        (это С ф-ии кот вызывает Python) гораздо быстрее словаря
        буквы итерируем не из строки(она мб огромной) а из алфавита

        !!!
        """
        # index_set = set()
        # for l in 'abcdefghijklmnopqrstuvwxyz':
        #     if s.count(l) == 1:
        #         index_set.add(s.index(l))
        import string
        letters = string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
        index_set = {s.index(l) for l in letters if s.count(l) == 1}  # еще круче
        return min(index_set) if index_set else -1


sol = Solution()
res = sol.firstUniqChar("loveleetcode")
assert res == 2, res

res = sol.firstUniqChar("leetcode")
assert res == 0, res

"""
383. Ransom Note
Easy

Given two strings ransomNote and magazine, return true if ransomNote 
can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # вар 1 мое:  - очень долго
        # dic_mag = Counter(magazine)
        # dic_rans = Counter(ransomNote)
        # for l in dic_rans:
        #     if l in dic_mag.keys() and dic_rans[l] <= dic_mag[l]:
        #         continue
        #     else:
        #         return False
        # return True

        # var 2: очень быстрый
        # rans = Counter(ransomNote)
        # mag = Counter(magazine)
        # c = rans - mag
        # # если ничего не осталось значит в подстроке
        # # было только то что и в родительской:
        # return not c
        # return not Counter(ransomNote) - Counter(magazine)

        # var 3 set + count - это еще быстрее
        set_rans = set(ransomNote)
        for l in set_rans:  # чтобы не проверять повторно одну букву
            if ransomNote.count(l) > magazine.count(l):
                return False
        return True


sol = Solution()
res = sol.canConstruct("aa", "aab")
assert res is True, res

res = sol.canConstruct("ab", "aa")
assert res is False, res

"""
242. Valid Anagram
Easy

Given two strings s and t, return true if t is an 
anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the 
letters of a different word or phrase, typically using all 
the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? 
How would you adapt your solution to such a case?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_set = set(s)
        # t_set = set(t)
        # all_set = s_set.union(t_set)
        # for letter in all_set:
        #     if s.count(letter) != t.count(letter):
        #         return False
        # return True  # решение похоже на предыдущее но нужно исп сортировку

        # var 2: sort
        # s_sort = sorted(s)
        # t_sort = sorted(t)
        # s_sort, t_sort = list(map(sorted, [s, t]))  # так даже дольше
        # for s_letter, t_letter in zip(s_sort, t_sort):
        #     if s_letter != t_letter:
        #         return False
        # return True

        # var 3: sort only:
        # return sorted(t) == sorted(s)
        # или тоже в одну строку: return Counter(s) == Counter(t)

        # var 4: sort and dict
        if len(s) != len(t):
            return False
        ddct = defaultdict(int)  # словарь {любой ключ: 0}
        for c in s:  # считываем из s и добавляем
            ddct[c] += 1
        for c in t:  # считываем из t и вычитаем
            ddct[c] -= 1
        return all(el == 0 for el in ddct.values())  # генератор проверяет если вычли больше чем положили и наоборот
        # all() принимает итерабл а значит примет и итератор(генератор)


sol = Solution()
res = sol.isAnagram("^ир", "ри^")
assert res is True, res

res = sol.isAnagram("anagram", "nagaram")
assert res is True, res

res = sol.isAnagram("rat", "car")
assert res is False, res

"""
141. Linked List Cycle
Easy

Given head, the head of a linked list, determine if the 
linked list has a cycle in it.

There is a cycle in a linked list if there is some node in 
the list that can be reached again by continuously following 
the next pointer. Internally, pos is used to denote the index 
of the node that tail's next pointer is connected to. Note that 
pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, 
return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the 
tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the 
tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val}'


def list_to_linked(lst):
    """
    создает связный список из обычного
    """
    if not lst:
        return None
    it_lst = iter(lst)  # создали итератор
    head = ListNode(next(it_lst))  # создали первый узел со значением val
    nodes = [head]  # сначала в списке узлов только один
    for node in nodes:
        new = next(it_lst, None)  # итерируем дальше - берем следующий - ищем next узла
        if new is not None:  # если есть
            node.next = ListNode(new)  # он тоже класса ListNode
            nodes.append(node.next)  # добавляем в цикл находу
    return head


class Solution:
    def hasCycle(self, head: [ListNode]) -> bool:
        # set_nodes = set()
        # while head:
        #     print(id(head))
        #     if head in set_nodes:
        #         return True
        #     set_nodes.add(head)
        #     print(id(head))
        #     head = head.next
        # return False

        # var2 using tortoise and hare alg:
        fast = head
        slow = head  # начинаем одновременно
        while fast and fast.next:  # тк fast быстрее - проверяем его
            slow = slow.next  # движежние на 1
            fast = fast.next.next  # движение через 1
            if slow == fast:  # если встретятся - цикл есть
                return True
        return False


# sol = Solution()
# res = sol.hasCycle(list_to_linked([3, 2, 0, -4, 2, 0, -4])) тут разные объекты создались - не работает
# assert res is True, res


"""
21. Merge Two Sorted Lists
Easy

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by
splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        new = list1 if list1 else list2
        if list1 and list2:
            if list2.val > list1.val:
                list1 = list1.next
            else:
                new = list2
                list2 = list2.next
            new.next = self.mergeTwoLists(list1, list2)
        return new


# sol = Solution()
# res = sol.mergeTwoLists(list_to_linked([1, 2, 4]), list_to_linked([1, 3, 4]))
# # assert res == list_to_linked([1, 1, 2, 3, 4, 4]), res
# print(id(res))
# while res:
#     print(res.val)
#     res = res.next
#
# res2 = list_to_linked([1, 1, 2, 3, 4, 4])
# print(id(res2))
# while res2:
#     print(res2.val)
#     res2 = res2.next

"""
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: [ListNode], val: int) -> [ListNode]:
        # var 1:
        # dummy = ListNode(-1, head)
        # prev = dummy
        # while head:
        #     if head.val != val:
        #         prev = head  # продвинулся вперед
        #     else:
        #         prev.next = head.next
        #     head = head.next
        # return dummy.next

        # var 2(мой!!!):
        if head:  # на случай если []
            head.next = self.removeElements(head.next, val)  # определяем next
            if head.val == val:
                return head.next
            return head
        return None

        # var 3:
        # if not head:
        #     return None
        # head.next = self.removeElements(head.next, val)
        # return head.next if head.val == val else head


sol = Solution()
# res = sol.removeElements(list_to_linked([]), 1)
# assert res == list_to_linked([]), res
#
# res = sol.removeElements(list_to_linked([2, 2, 2]), 2)
# assert res == list_to_linked([]), res

# res = sol.removeElements(list_to_linked([1, 2, 4]), 2)
# assert res == list_to_linked([1, 4]), res


"""
206. Reverse Linked List
Easy

Given the head of a singly linked list, reverse the list, 
and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively 
or recursively. Could you implement both?
"""


class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        if not head or not head.next:
            return head
        r_head = self.reverseList(head.next)  # 1, 2, 3, 4, None
        head.next.next = head
        head.next = None
        return r_head


# sol = Solution()
# res = sol.reverseList(list_to_linked([1, 2, 3, 4]))
# print(res)
# assert res == list_to_linked([4, 3, 2, 1]), res

"""
83. Remove Duplicates from Sorted List
Easy

Given the head of a sorted linked list, delete all duplicates 
such that each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:
    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: [ListNode]) -> [ListNode]:
        # вели доп переменную чтобы итерироваться по списку не меняя его
        temp = head
        while temp:  # пока не закончился список
            while temp.next and temp.next.val == temp.val:
                temp.next = temp.next.next
            temp = temp.next  # взяли cur чтобы в этом месте не обрезать head
            # т к temp хранит новый узел в момент времени
            print(f'head = {head}', f'cur = {temp}', sep=', ')
        return head


# sol = Solution()
# res = sol.deleteDuplicates(list_to_linked([1, 1, 2, 3, 3]))
# print(res)
# assert res == list_to_linked([1, 2, 3]), res


"""
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # var 1 (mine)
        # stack = []
        # for l in s:
        #     if l in '{([':  # сначала смотрим открывающие скобки, добавляем их в стэк
        #         stack.append(l)
        #     else:
        #         if stack:  # если стэк не пустой, смотрим закрывающие скобки
        #             ll = stack[-1]
        #             if ll == '{' and l == '}' or ll == '(' and l == ')' or ll == '[' and l == ']':
        #                 stack.pop()
        #             else:
        #                 return False
        #         else:
        #             return False
        # return False if stack else True

        # var 2(not mine)
        stack = []
        brackets_dic = {  # храним все возможные скобки в словаре
            '{': '}',
            '(': ')',
            '[': ']'
        }
        for el in s:
            if el in brackets_dic:  # если открывающая - сохраняем в стек ее пару
                stack.append(brackets_dic[el])
            else:
                if stack and stack[-1] == el:  # если закрывающая, то она уже должна быть в стеке
                    stack.pop()
                else:
                    return False
        return False if stack else True  # если стек не опустел

        # closeToOpen = {
        #     ']': '[',
        #     '}': '{',
        #     ')': '('
        # }
        # for char in s:
        #     if char in closeToOpen:  # все скобки держим в словаре
        #         if stack and stack[-1] == closeToOpen[char]:
        #             stack.pop()  # закрывающую скобку удаляем из стэка
        #         else:
        #             return False
        #     else:
        #         stack.append(char)  # если открывающая скобка - добавляем в стэк
        #
        # return True if not stack else False


sol = Solution()
# res = sol.isValid("]")
# assert res is False, res

# res = sol.isValid("[")
# assert res is False, res

res = sol.isValid("{[]}")
assert res is True, res

res = sol.isValid("()[]{}")
assert res is True, res

"""
232. Implement Queue using Stacks
Easy

Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal
queue (push, peek, pop, and empty).

Implement the MyQueue class:
    void push(int x) Pushes element x to the back of the queue.
    int pop() Removes the element from the front of the queue and returns it.
    int peek() Returns the element at the front of the queue.
    boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
You must use only standard operations of a stack, which means only push 
to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively.
You may simulate a stack using a list or deque (double-ended queue) as 
long as you use only a stack's standard operations.
"""


class MyQueue:
    def __init__(self):
        self.stack_1 = []  # O(1)
        self.stack_2 = []

    def push(self, x: int) -> None:  # O(1)
        self.stack_1.append(x)
        return None

    def pop(self) -> int:
        # var1
        # first = self.stack_1[0]  # O(1)
        # self.stack_1 = self.stack_1[1:]  # O(n)
        # return first

        # var2
        """
        перелил из одного стека в другой
        взял верхнее значение
        прелил обратно
        """
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())
        el = self.stack_2.pop()
        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())
        return el

    def peek(self) -> int:  # O(1)
        return self.stack_1[0]

    def empty(self) -> bool:  # O(1)
        return False if self.stack_1 else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(2)
# param_4 = obj.empty()
# print(obj.empty())

# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


"""
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'({self.val})'


def binarytree_from_list(lst):
    """
    create nested nodes from list
    """
    nodes = iter(lst)
    root_val = next(nodes)  # this is nodes[0]
    if root_val is None:
        return False
    root_node = TreeNode(root_val)
    all_nodes = [root_node]  # add nodes to iterate trough them later

    for node in all_nodes:
        val_left = next(nodes, None)
        if val_left:  # if it leaf
            node.left = TreeNode(val_left)
            all_nodes.append(node.left)

        val_right = next(nodes, None)
        if val_right:  # if it leaf
            node.right = TreeNode(val_right)
            all_nodes.append(node.right)
    return root_node


root = [1, None, 2, 3]

"""
144. Binary Tree Preorder Traversal
Easy

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]
"""
class Solution:
    def preorderTraversal(self, root: [TreeNode]) -> list[int]:
        """var 1, iteratively"""
        res = []  # исп для результата
        # исп стэк будем имитировать рекурсивные вызовы
        # кладем в стэк корневой узел:
        stack = [root]
        while stack:
            curr_node = stack.pop()  # извлекаем из стека верхний нод(корень, левый, правый)
            if curr_node:
                res.append(curr_node.val)
                # берем сначала правый чтобы потом достать из стека и записать в res левый:
                stack.append(curr_node.right)
                stack.append(curr_node.left)
        return res
    """
    суть решения в том что в стек попадает сначала сам узел а потом и его дети
     - это есть прямой обход дерева в глубину
    шаги:
    для итеративного способа:
    положили корневой узел в стек
    удалили узел из стека
    добавили в стек его правого ребенка
    добавили в стек его левого ребенка
    повторяем все пока стек не опустеет
    
    итеративный отличается от рекурсивного использованием стека
    для имитации рекурсивных вызовов.
    
    блин, мой затык оказался в том что я собиралась пройти именно dfs 
    сначала по всем левым детям потом вернуться пройти по потомкам правого итд
    оказалась какая-то смесь dfs и bfs...
    """

    """var 2, recursively"""
    # def preorderTraversal(self, root: [TreeNode]) -> list[int]:
    #     res = []
    #
    #     def dfs(node):
    #         if node:
    #             res.append(node.val)
    #             dfs(node.left)  # здесь доберется до None и потом пойдет ниже(вверх по дереву)
    #             dfs(node.right)
    #         return  # а возвращать ничего не надо тк мы пишем в res
    #
    #     dfs(root)  # вызываем от корневого узла
    #     return res


sol = Solution()

root = [1, 2, 3, 4, None, 5]
root = binarytree_from_list(root)
res = sol.preorderTraversal(root)
assert res == [1, 2, 4, 3, 5], res

root = [1, None, 2, 3]
root = binarytree_from_list(root)
res = sol.preorderTraversal(root)
assert res == [1, 2, 3], res


"""
94. Binary Tree Inorder Traversal
Easy

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """in-order traversal: левый, корень, правый"""

    """var1 recursively"""
    # def inorderTraversal(self, root: [TreeNode]) -> list[int]:
    #     res = []
    #     def dfs_inorder(root):
    #         if root:
    #             dfs_inorder(root.left)  # падаем
    #             res.append(root.val)  # пишем в res
    #             dfs_inorder(root.right)  # падаем
    #         return  # ничего, все записано в res
    #
    #     dfs_inorder(root)
    #     return res  # конечный результ

    """var2 iteratively"""
    def inorderTraversal(self, root: [TreeNode]) -> list[int]:
        res, stack = [], []

        while True:
            # кладем в стек всех левых детей левых родителей
            while root:
                stack.append(root)
                root = root.left  # движение по левым потомкам

            # перед pop() проверяем не пуст ли стек:
            if not stack:
                return res

            curr = stack.pop()
            res.append(curr.val)
            root = curr.right  # зашли в правого(чтобы обойти всех его левых)


        # # this following "while True" block keeps running until "return"
        # while True:
        #     # goes all the way to left end's None, append every step onto "stack"
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #
        #     # if stack has nothing left, then return result
        #     if not stack:
        #         return res
        #
        #     # take the last step out, append its value to result
        #     node = stack.pop()
        #     res.append(node.val)
        #     # moves to right before going all the way to left end's None again
        #     root = node.right


sol = Solution()
"""
     1
  2    3
4  N  5  N
"""
root = [1, 2, 3, 4, None, 5]
root = binarytree_from_list(root)
res = sol.inorderTraversal(root)
assert res == [4, 2, 1, 5, 3], res


