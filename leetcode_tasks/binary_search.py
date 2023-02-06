from math import sqrt
from collections import Counter

"""
# 704
Given an array of integers nums which is sorted in ascending order, and an
integer target, write a function to search target in nums. If target exists,
then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        hight = len(nums) - 1
        while hight >= low:
            middle = (hight + low) // 2
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                low = middle + 1
            elif target < nums[middle]:
                hight = middle - 1
        return -1 if target != nums[middle] else middle


sol = Solution()

res = sol.search([-1, 0, 3, 5, 9, 12], 9)
assert res == 4, res

res = sol.search([-1, 0, 3, 5, 9, 12], 2)
assert res == -1, res

res = sol.search([2, 5], 5)
assert res == 1, res

"""
# 35
Given a sorted array of distinct integers and a target value, return the index if the 
target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        first = 0
        last = len(nums) - 1
        while first < last:
            middle = (first + last) // 2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                last = middle - 1
            else:
                first = middle + 1
        if nums[first] > target:
            return first
        elif nums[last] < target:
            return last + 1
        return first


sol = Solution()

res = sol.searchInsert([1, 3, 5, 6], 5)
assert res == 2, res

res = sol.searchInsert([1, 3, 5, 6], 0)
assert res == 0, res

res = sol.searchInsert([1, 3, 5, 6], 7)
assert res == 4, res

res = sol.searchInsert([1, 3], 0)
assert res == 0, res

res = sol.searchInsert([1], 1)
assert res == 0, res

"""
MOUNTAIN ARRAY: [1, 2, 3, 4, 9, 8, 7, 6, 5]

is an array of length at least 3 with elements strictly increasing 
from starting till an index i, and then strictly decreasing from 
index i to last index.


# 852
An array arr a mountain if the following properties hold:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... 
< arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.
"""


class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        last = len(arr) - 1
        first = 0
        # middle = 1
        # while 0 < middle < len(arr) - 1:
        #     middle = (last + first) // 2
        #     if arr[middle - 1] < arr[middle] > arr[middle + 1]:
        #         return middle
        #     elif arr[middle - 1] > arr[middle] > arr[middle + 1]:  # descend
        #         last = middle - 1
        #     elif arr[middle - 1] < arr[middle] < arr[middle + 1]:  # ascend
        #         first = middle + 1
        # return first if arr[first] > arr[last] else last
        #
        # вариант 2
        '''горный массив можно проверять только по восхождению, до пика!'''
        while last > first:
            middle = (last + first) // 2
            if arr[middle] < arr[middle + 1]:
                first = middle + 1
            else:
                last = middle
        return first


sol = Solution()

res = sol.peakIndexInMountainArray([12, 13, 19, 41, 55, 69, 70, 71, 96, 72])
assert res == 8, res

res = sol.peakIndexInMountainArray([24, 69, 100, 99, 79, 78, 67, 36, 26, 19])
assert res == 2, res

res = sol.peakIndexInMountainArray([3, 9, 8, 6, 4])
assert res == 1, res

res = sol.peakIndexInMountainArray([0, 2, 1, 0])
assert res == 1, res

res = sol.peakIndexInMountainArray([0, 10, 5, 2])
assert res == 1, res

res = sol.peakIndexInMountainArray([0, 1, 0])
assert res == 1, res

res = sol.peakIndexInMountainArray([3, 4, 5, 1])
assert res == 2, res

"""
367. Valid Perfect Square
Easy
Given a positive integer num, write a function which returns True if num 
is a perfect square else False.
Follow up: Do not use any built-in library function such as sqrt
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = sqrt(num)
        # return True if n - int(n) == 0 else False
        first = 1
        last = num
        while first <= last:  # <= а не < для крайних значений или 1
            middle = (first + last) // 2
            if n == middle:
                return True
            elif n > middle:
                first = middle + 1
            else:
                last = middle - 1
        return False


sol = Solution()

res = sol.isPerfectSquare(1)
assert res is True, res

res = sol.isPerfectSquare(16)
assert res is True, res

"""
1385. Find the Distance Value Between Two Arrays
Easy

Given two integer arrays arr1 and arr2, and the integer d, return the 
distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that 
there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.
это количество элементов массива arr1 для которых не верно условие 
arr1[i]-arr2[j]| <= d со всеми элементами массива arr2
"""


class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        n = len(arr1)
        for el in arr1:
            k = 0
            first = 0
            last = len(arr2) - 1
            while first <= last:
                mid = (first + last) // 2
                if el > arr2[mid] and abs(el - arr2[mid]) > d:
                    first = mid + 1
                elif el < arr2[mid] and abs(el - arr2[mid]) > d:
                    last = mid - 1
                else:
                    k += 1
                    break
            if k:
                n -= 1
        return n


sol = Solution()

res = sol.findTheDistanceValue(arr1=[-3, 10, 2, 8, 0, 10], arr2=[-9, -1, -4, -9, -8], d=9)
assert res == 2, res

res = sol.findTheDistanceValue(arr1=[4, 5, 8], arr2=[10, 9, 1, 8], d=2)
assert res == 2, res

res = sol.findTheDistanceValue(arr1=[1, 4, 2, 3], arr2=[-4, -3, 6, 10, 20, 30], d=3)
assert res == 2, res

"""
69. Sqrt(x)
Easy

Given a non-negative integer x, return the square root of x rounded down to the 
nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

"""


class Solution:
    def mySqrt(self, x: int) -> int:
        first = 1
        last = x
        mid = x
        while first < last:
            mid = (first + last) // 2
            if mid * mid > x:
                last = mid
            elif mid * mid < x:
                if last - first == 1:
                    return mid
                first = mid
            else:
                return mid
        return mid

        # if x <= 1: return x
        # l, r = 2, x
        # while l <= r:
        #     mid = (l + r) // 2
        #     if mid * mid == x:
        #         return mid
        #     elif mid * mid < x:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        # return r


sol = Solution()

res = sol.mySqrt(2)
assert res == 1, res

res = sol.mySqrt(6)
assert res == 2, res

res = sol.mySqrt(0)
assert res == 0, res

res = sol.mySqrt(3)
assert res == 1, res

res = sol.mySqrt(8)
assert res == 2, res

"""
744. Find Smallest Letter Greater Than Target
Easy

You are given an array of characters letters that is sorted in non-decreasing 
order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than 
target. If such a character does not exist, return the first character in letters

'a' < 'b'
True
"""


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        # # если понадобится вернуть первый:
        # l_1 = letters[0]
        # # убираем дубликаты и сортируем:
        # letters = list(set(letters))
        # letters.sort()
        # # бинарный поиск:
        # first = 0
        # last = len(letters) - 1
        # while first <= last:
        #     mid = (first + last) // 2
        #     if letters[mid] > target:
        #         last = mid - 1
        #     elif letters[mid] < target:
        #         first = mid + 1
        #     # если target в списке - выходим из цикла:
        #     else:
        #         break
        # # если след за mid элем больше target - нашли, если такого нет вернем по условию
        # try:
        #     return letters[mid+1] if letters[mid] <= target else letters[mid]
        # except IndexError:
        #     return l_1

        # вариант2
        # сначала учитываем краевые случаи:
        # вернем 0-ой элем если он больше цели или если последний не больше цели:
        if target < letters[0] or target >= letters[-1]:
            return letters[0]
        left = 0
        right = len(letters) - 1
        while left <= right:
            mid = (left + right) // 2
            if target >= letters[mid]:
                left = mid + 1
            if target < letters[mid]:
                right = mid - 1
        return letters[left]


sol = Solution()

res = sol.nextGreatestLetter(["c", "f", "j"], "a")
assert res == "c", res

res = sol.nextGreatestLetter(["e", "e", "e", "e", "e", "e", "n", "n", "n", "n"], "e")
assert res == "n", res

res = sol.nextGreatestLetter(["e", "e", "g", "g"], "g")
assert res == "e", res

res = sol.nextGreatestLetter(["c", "f", "j"], "j")
assert res == "c", res

res = sol.nextGreatestLetter(["c", "f", "j"], "c")
assert res == "f", res

res = sol.nextGreatestLetter(["c", "f", "j"], "k")
assert res == "c", res

res = sol.nextGreatestLetter(["c", "f", "j"], "d")
assert res == "f", res

"""
278. First Bad Version
Easy

You are a product manager and currently leading a team to develop a new 
product. Unfortunately, the latest version of your product fails the quality 
check. Since each version is developed based on the previous version, all the 
versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first 
bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version 
is bad. Implement a function to find the first bad version. You should minimize 
the number of calls to the API.
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# class Solution:
#     def firstBadVersion(self, n: int) -> int:
#         if isBadVersion(1):
#             return 1
#         first = 0
#         last = n
#         while first <= last:
#             mid = (first + last) // 2
#             if isBadVersion(mid):
#                 last = mid - 1
#             else:
#                 first = mid + 1
#         return first


"""
34. Find First and Last Position of Element in Sorted Array
Medium

Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]
        new_arr = []
        if nums[0] == target:
            new_arr.append(0)
        first = 0
        last = len(nums) - 1
        while first <= last:
            mid = (first + last) // 2
            if nums[mid] < target:
                first = mid + 1
            elif nums[mid] > target:
                last = mid - 1
            else:
                if not new_arr:
                    last = mid - 1
                    first = last
                    if nums[first] < target:
                        new_arr.append(mid)
                        first = mid + 1
                        last = len(nums) - 1
                else:
                    if nums[-1] == target:
                        new_arr.append(len(nums) - 1)
                        return new_arr
                    else:
                        last = mid + 1
                        first = last
                        if nums[last] > target:
                            new_arr.append(mid)
        return [-1, -1] if not new_arr else [new_arr[0], new_arr[-1]]


sol = Solution()

res = sol.searchRange([1, 2, 3, 3, 3, 3, 4, 5, 9], 3)
assert res == [2, 5], res

res = sol.searchRange([5, 7, 7, 8, 8, 10], 8)
assert res == [3, 4], res

res = sol.searchRange([5, 7, 7, 8, 8, 10], 6)
assert res == [-1, -1], res

res = sol.searchRange([], 0)
assert res == [-1, -1], res

"""
441. Arranging Coins
Easy

You have n coins and you want to build a staircase with these coins. 
The staircase consists of k rows where the ith row has exactly i coins. 
The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

Input: n = 5, Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        # var 1 is runtime error
        # start = 1
        # last = n
        # row = 0
        # while start <= last:
        #     row = (start + last) // 2
        #     if sum(range(row + 1)) > n:
        #         last = row - 1
        #     elif sum(range(row + 1)) < n:
        #         start = row + 1
        #     else:
        #         return row
        # return last

        # var 2:
        """
        row 1 include 1 coin instead      => k=1
        row 2 include 3 coin instead 4    => k=1,5
        row 3 include 6 coin instead 9    => k=2
        row 4 include 10 coin instead 16  => k=2,5

        """

        start = 1
        last = n
        row = 0
        while start <= last:
            row = (start + last) // 2
            if row * (row * 0.5 + 0.5) > n:
                last = row - 1
            elif row * (row * 0.5 + 0.5) < n:
                start = row + 1
            else:
                return row
        return last


sol = Solution()

res = sol.arrangeCoins(4)
assert res == 2, res

res = sol.arrangeCoins(2)
assert res == 1, res

res = sol.arrangeCoins(8)
assert res == 3, res

res = sol.arrangeCoins(1)
assert res == 1, res

res = sol.arrangeCoins(7)
assert res == 3, res

"""
1539. Kth Missing Positive Number
Easy

Given an array arr of positive integers sorted in a strictly 
increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

 
Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. 
The 5th missing positive integer is 9.
"""


class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        # arr1 = set(range(arr[-1] + 1 + k))
        # arr2 = set(arr)
        # num = list(arr1.difference(arr2))
        # num.sort()
        # return num[k]

        # var 2:
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) // 2
            if arr[m] - 1 - m < k:
                l = m + 1
            else:
                r = m
        return l + k


sol = Solution()

res = sol.findKthPositive([1, 2, 3, 4], 2)
assert res == 6, res

res = sol.findKthPositive([2, 3, 4, 7, 11], 5)
assert res == 9, res

"""
167. Two Sum II - Input Array Is Sorted
Medium

Given a 1-indexed array of integers numbers that is already sorted in 
non-decreasing order, find two numbers such that they add up to a specific 
target number. Let these two numbers be numbers[index1] and numbers[index2] 
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as 
an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may 
not use the same element twice.

Your solution must use only constant extra space.

 
Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        first = 0
        last = len(numbers) - 1
        while first < last:
            summ = numbers[first] + numbers[last]
            if summ > target:
                last -= 1
            elif summ < target:
                first += 1
            else:
                return [first + 1, last + 1]


sol = Solution()

res = sol.twoSum([3, 24, 50, 79, 88, 150, 345], 200)
assert res == [3, 6], res

res = sol.twoSum([2, 7, 11, 15], 9)
assert res == [1, 2], res

res = sol.twoSum([5, 25, 75], 100)
assert res == [2, 3], res

res = sol.twoSum([-3, 3, 4, 90], 0)
assert res == [1, 2], res

res = sol.twoSum([2, 3, 4], 6)
assert res == [1, 3], res

"""
1351. Count Negative Numbers in a Sorted Matrix
Easy

Given a m x n matrix grid which is sorted in non-increasing order both 
row-wise and column-wise, return the number of negative numbers in grid.

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

"""


class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        def binary(arr):
            first = 0
            last = len(arr) - 1
            while first <= last:
                m = (first + last) // 2

                try:
                    num_idx = arr[m][-1]
                except TypeError:
                    num_idx = arr[m]

                if num_idx < 0:
                    last = m - 1
                else:
                    first = m + 1
            return first

        count = 0
        if grid[-1][-1] >= 0:
            return 0
        elif grid[0][-1] < 0:
            i = 0
        else:
            i = binary(grid)  # № подмассива с -
        for lst_idx in range(i, len(grid)):
            count += len(grid[lst_idx]) - binary(grid[lst_idx])
        return count


sol = Solution()

res = sol.countNegatives([[3, 2], [-3, -3], [-3, -3], [-3, -3]])
assert res == 6, res

res = sol.countNegatives([[5, 1, 0], [-5, -5, -5]])
assert res == 3, res

res = sol.countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]])
assert res == 8, res

"""
1608. Special Array With X Elements Greater Than or Equal X
Easy

You are given an array nums of non-negative integers. nums is considered 
special if there exists a number x such that there are exactly x numbers 
in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven 
that if nums is special, the value for x is unique.

Example 1:

Input: nums = [3,5]
Output: 2
Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

порядок решения:
сортируем массив, принимаем за х середину, как только элем под индексом х
становится меньше чем кол-во элементов от него до конца - нашли
если число больше чем кол-во, то продолжаем искать.
если х = кол-ву элементов после него, значит условие не выполнено возвращаем -1
(х не может быть больше кол-ва элементов
и кол-во элементов не может быть больше х)
если все ок - возвращаем разницу
"""


class Solution:
    def specialArray(self, nums: list[int]) -> int:
        l = len(nums) - 1
        f = 0
        nums.sort()
        while f < l:
            x = (f + l) // 2
            if nums[x] < len(nums) - x:
                if nums[x] == len(nums) - 1 - x:  # 3, 6, 6, 7 если x = 3 то кол-во = 4, если х=4 то кол-во = 3
                    return -1
                f = x + 1
            else:
                l = x
        return len(nums) - f if len(nums) - f <= nums[f] else -1


sol = Solution()

res = sol.specialArray([3, 3, 3])
assert res == 3, res

res = sol.specialArray([3, 6, 7, 7, 0])
assert res == -1, res

res = sol.specialArray([0, 4, 3, 0, 4])
assert res == 3, res

res = sol.specialArray([3, 5])
assert res == 2, res

"""
74. Search a 2D Matrix
Medium

Write an efficient algorithm that searches for a value target in an m x n 
integer matrix matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the 
    previous row.

"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def bin_search(arr):
            f = 0
            l = len(arr) - 1
            while f < l:
                m = (f + l) // 2

                try:
                    a = arr[m][0]
                except TypeError:
                    a = arr[m]

                if a >= target:
                    l = m
                elif a < target:
                    f = m + 1
            return f

        idx_1 = bin_search(matrix)
        if matrix[idx_1][0] > target:
            idx_1 -= 1
        cur_arr = matrix[idx_1]
        idx_2 = bin_search(cur_arr)

        if matrix[idx_1][idx_2] == target:
            return True
        else:
            return False


sol = Solution()

res = sol.searchMatrix([[1], [3]], 1)
assert res is True, res

res = sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 11)
assert res is True, res

res = sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 7)
assert res is True, res

res = sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
assert res is True, res

"""
1337. The K Weakest Rows in a Matrix
Easy

You are given an m x n binary matrix mat of 1's (representing soldiers) 
and 0's (representing civilians). The soldiers are positioned in front of 
the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

    The number of soldiers in row i is less than the number of soldiers in row j.
    Both rows have the same number of soldiers and i < j.

Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.
"""


class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        dic = dict()
        i = 0
        for row in mat:
            f = 0
            l = len(row) - 1
            while f <= l:
                m = (f + l) // 2
                if row[m] == 1:
                    f = m + 1
                else:
                    l = m - 1
            dic[i] = f
            i += 1
        dic = sorted(dic.items(), key=lambda x: x[1])
        return [dic[i][0] for i in range(k)]


sol = Solution()

res = sol.kWeakestRows([[1, 1, 0, 0, 0],
                        [1, 1, 1, 1, 0],
                        [1, 0, 0, 0, 0],
                        [1, 1, 0, 0, 0],
                        [1, 1, 1, 1, 1]], 3)
assert res == [2, 0, 3], res

"""
1346. Check If N and Its Double Exist
Easy

Given an array arr of integers, check if there exist two indices i and j such that :

    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]

"""


class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        arr.sort()
        dic = {i: arr[i] for i in range(len(arr))}
        for k, v in dic.items():
            f = 0
            l = len(dic) - 1
            while f <= l:
                m = (f + l) // 2
                if dic[m] < 2 * v:
                    f = m + 1
                elif dic[m] > 2 * v:
                    l = m - 1
                else:
                    if m != k:
                        return True
                    else:
                        f = m + 1
        return False
        # d = {}
        # for val in arr:
        #     if d.get(val * 2, 0) or d.get(val // 2, 0):
        #         return True
        #     d[val] = 1
        # return False


sol = Solution()

res = sol.checkIfExist([-2, 0, 10, -19, 4, 6, -8])  # [-19, -8, -2, 0, 4, 6, 10]
assert res is False, res

res = sol.checkIfExist([10, 2, 5, 3])  # 2, 3, 5, 10
assert res is True, res

res = sol.checkIfExist([-10, 12, -20, -8, 15])  # -20, -10, -8, 12, 15, 17
assert res is True, res

res = sol.checkIfExist([2, 3, 3, 0, 0])  # 0, 0, 2, 3, 3
assert res is True, res

res = sol.checkIfExist([10, 2])
assert res is False, res

"""
350. Intersection of Two Arrays II
Easy

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays 
and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

"""


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1 = dict(Counter(nums1))
        nums2 = dict(Counter(nums2))
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        lst2 = list(nums2.keys())
        lst2.sort()
        lst = []
        for k, v in nums1.items():
            f = 0
            l = len(nums2) - 1
            while f <= l:
                m = (f + l) // 2
                if lst2[m] == k:
                    lst.extend([k for i in range(min(nums2[k], nums1[k]))])
                    f = m + 1
                elif lst2[m] < k:
                    f = m + 1
                else:
                    l = m - 1
        return lst

        # var2 - two counters:
        # nums1.sort()
        # nums2.sort()
        #
        # ans = []
        # i = j = 0
        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] < nums2[j]:
        #         i += 1
        #     elif nums1[i] > nums2[j]:
        #         j += 1
        #     else:
        #         ans.append(nums1[i])
        #         i += 1
        #         j += 1
        # return ans


sol = Solution()

res = sol.intersect([4, 9, 5], nums2=[9, 4, 9, 8, 4])
assert res == [4, 9], res

"""
633. Sum of Square Numbers
Medium
Given a non-negative integer c, decide whether there're two 
integers a and b such that a2 + b2 = c.

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

"""


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        j = int(sqrt(c))
        for i in range(j + 1):
            if i ** 2 + j ** 2 == c:
                return True
            elif i ** 2 + j ** 2 < c:
                i += 1
            else:
                j -= 1
        return False


sol = Solution()

res = sol.judgeSquareSum(5)
assert res is True, res

"""
1855. Maximum Distance Between a Pair of Values
Medium

You are given two non-increasing 0-indexed integer arrays nums1 and nums2.

A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j < nums2.length, 
is valid if both i <= j and nums1[i] <= nums2[j]. The distance of the pair is j - i.

Return the maximum distance of any valid pair (i, j). If there are no valid pairs, return 0.

An array arr is non-increasing if arr[i-1] >= arr[i] for every 1 <= i < arr.length.
"""


class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        max_dist, dist = 0, 0
        i, j = len(nums1) - 1, len(nums2) - 1
        for i in range(min(i, j) + 1):
            if nums1[i] <= nums2[i]:
                if nums1[i] <= nums2[j]:
                    dist = j - i
                else:
                    f, l = i, j
                    while f <= l:
                        m = (f + l) // 2
                        if nums1[i] > nums2[m]:
                            l = m - 1
                        else:
                            f = m + 1
                            dist = m - i
            if max_dist < dist:
                max_dist = dist
        return max_dist

        # var 2:
        # i = j = res = 0
        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] > nums2[j]:
        #         i += 1
        #     else:
        #         res = max(res, j - i)
        #         j += 1
        # return res


sol = Solution()

res = sol.maxDistance([30, 29, 28, 27], [30, 29, 28, 27])
assert res == 0, res

res = sol.maxDistance([9819, 9508, 7398, 7347, 6337, 5756, 5493, 5446, 5123, 3215, 1597, 774, 368, 313],
                      [9933, 9813, 9770, 9697, 9514, 9490, 9441, 9439, 8939, 8754, 8665, 8560])
assert res == 9, res

res = sol.maxDistance([30, 29, 19, 5], [25, 25, 25, 25, 25])
assert res == 2, res

res = sol.maxDistance([2, 2, 2], [10, 10, 1])
assert res == 1, res

res = sol.maxDistance(nums1=[55, 30, 5, 4, 2], nums2=[100, 20, 10, 10, 5])
assert res == 2, res

"""
33. Search in Rotated Sorted Array
Medium

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown 
pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], 
nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For 
example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the 
index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        f = 0
        l = len(nums) - 1
        while f <= l:
            m = (f + l) // 2
            if nums[m] == target:
                return m

            elif nums[m] >= target:  # m > tar
                if nums[f] > target:
                    if nums[f] > nums[m]:
                        l = m - 1
                    else:
                        f = m + 1
                else:
                    l = m - 1

            else:  # m < tar
                if nums[l] >= target:
                    f = m + 1
                else:
                    if nums[f] < nums[m]:
                        f = m + 1
                    else:
                        l = m - 1
        return -1

        # start, end = 0, len(nums) - 1
        #
        # while start <= end:
        #     mid = start + (end - start) // 2
        #
        #     if nums[mid] == target:
        #         return mid
        #
        #     elif nums[mid] >= nums[start]:  # [3, 4, 5, 6, 1, 2]
        #         if nums[mid] >= target >= nums[start]:
        #             end = mid - 1
        #         else:
        #             start = mid + 1
        #     else:
        #         if nums[mid] <= target <= nums[end]:
        #             start = mid + 1
        #         else:
        #             end = mid - 1
        # return -1


sol = Solution()

res = sol.search([5, 1, 2, 3, 4], 1)
assert res == 1, res

res = sol.search([6, 7, 1, 2, 3, 4, 5], 6)
assert res == 0, res

res = sol.search([4, 5, 6, 7, 8, 1, 2, 3], 8)
assert res == 4, res

res = sol.search([5, 1, 3], 5)
assert res == 0, res

res = sol.search([3, 4, 5, 6, 1, 2], 2)
assert res == 5, res

res = sol.search([3, 5, 1], 1)
assert res == 2, res

res = sol.search([3, 5, 1], 5)
assert res == 1, res

res = sol.search([3, 5, 1], 3)
assert res == 0, res

res = sol.search([4, 5, 6, 7, 0, 1, 2], 0)
assert res == 4, res

res = sol.search([1, 3], 3)
assert res == 1, res

res = sol.search([3, 1], 3)
assert res == 0, res

res = sol.search([1, 3], 1)
assert res == 0, res

res = sol.search([3, 1], 1)
assert res == 1, res

res = sol.search([1], 0)
assert res == -1, res

res = sol.search([4, 5, 6, 7, 0, 1, 2], 3)
assert res == -1, res

"""
153. Find Minimum in Rotated Sorted Array
Medium

Suppose an array of length n sorted in ascending order is rotated between 
1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results 
in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum 
element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

"""


# class Solution:
#     def findMin(self, nums: list[int]) -> int:
#         f = 0
#         l = len(nums) - 1
#         m = (f + l) >> 1
#         while f < l:
#             if nums[m] >= nums[0]:
#                 f = m + 1
#             else:
#                 l = m
#             m = (f + l) >> 1
#         return min(nums[0], nums[l])
#
#
# sol = Solution()
#
# res = sol.findMin([4, 5, 6, 7, 0, 1, 2])
# assert res == 0, res


class Solution:
    def findMin(self, nums: list[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        else:
            f = 0
            l = len(nums) - 1
            while f < l:
                m = (f + l) // 2
                if nums[m] > nums[l]:
                    f = m + 1
                else:
                    l = m
            return nums[f]


sol = Solution()

res = sol.findMin([1, 2, 3, 4, 5])
assert res == 1, res

res = sol.findMin([2, 1])
assert res == 1, res

res = sol.findMin([3, 1, 2])
assert res == 1, res

res = sol.findMin([3, 4, 5, 1, 2])
assert res == 1, res
