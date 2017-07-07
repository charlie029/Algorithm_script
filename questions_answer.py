# -*- coding: utf-8 -*-
"""
Created on Wed Jun 01 15:40:11 2016

@author: djl358
"""
# question same tree
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p==None and q==None:
            return True
        elif p==None and q!=None:
            return False
        elif q!=None and p==None:
            return False
        elif p.val != q.val:
            return False
        else:
            print p.val            
        # the return a and b structure runs a first and then b
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
a = TreeNode(1)
a.left = TreeNode(2)
a.left.left = TreeNode(3)
a.right = TreeNode(4)
a.right.left = TreeNode(5)

b = TreeNode(1)
b.left = TreeNode(2)
b.left.left = TreeNode(3)
b.right = TreeNode(4)
b.right.left = TreeNode(5)

temp = Solution()
temp.isSameTree(a, b)


# question valid anagram
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = list(s)
        t_list = list(t)
        if len(s_list) == len(t_list):
            s_ls = sorted(s_list)
            t_ls = sorted(t_list)
            if s_ls == t_ls:
                return True
            else:
                return False
        else:
            return False

s = 'hello'
t = 'hello'
temp = Solution()
temp.isAnagram(s, t)

# 171. Excel Sheet Column Number
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_list = list(s)
        l = len(s_list)
        tsum = 0
        i = 0
        for item in s_list:
            tsum += (ord(item)-64)*26**(l-1-i)
            i += 1
        return tsum
s = 'ABCDEFD'
temp = Solution()
temp.titleToNumber(s)

# 217. Contains Duplicate
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        else:           
            nums_s = list(set(nums))
            if len(nums)==len(nums_s):
                return True
            else:
                return False
        
# 461. Hamming Distance
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_b = bin(x).replace('0b','')
        y_b = bin(y).replace('0b','')
        if len(x_b) <= len(y_b):
            x_b = x_b.zfill(len(y_b))
        else:
            y_b = y_b.zfill(len(x_b))
        
        return sum(x1 != y1 for x1, y1 in zip(x_b, y_b))
        
temp = Solution()
temp.hammingDistance(1,6)

# 500. Keyboard Row
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        list1 = list('qwertyuiop')
        list2 = list('asdfghjkl')
        list3 = list('zxcvbnm')
        rslt = list()
        for word in words:
            i = 0
            while i <= len(word)-2:
                if (word[i].lower() in list1) and (word[i+1].lower() not in list1):
                    break 
                elif (word[i].lower() in list2) and (word[i+1].lower() not in list2):
                    break
                elif (word[i].lower() in list3) and (word[i+1].lower() not in list3):
                    break
                else:
                    i+=1
            if i==len(word)-1:
                rslt.append(word)
        return rslt
temp = Solution()
temp.findWords(["Aasdfghjkl","Qwertyuiop","zZxcvbnm"])

# 476. Number Complement

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        rslt = str()
        for x in bin(num)[2:]:
            y = 1 - int(x)
            rslt = ''.join((rslt,str(y)))
        print(bin(num), rslt)
        return int(rslt,2)
temp = Solution()
temp.findComplement(5)
        
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        rslt = list()
        for inum in findNums:
            i = nums.index(inum)+1
            rslt.append(-1)
            while i < len(nums):
                #print(inum, nums)
                if inum < nums[i]:
                    rslt[-1] = nums[i]
                    break
                i += 1
                
        return rslt
temp = Solution()
temp.nextGreaterElement([4,1,2],[1,3,4,2])
temp.nextGreaterElement([2,4],[1,2,3,4])
temp.nextGreaterElement([4,1,2,5],[1,3,4,2,5])


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x = 0
        y = 0
        rslt = 0
        for ls in grid:
            y = 0
            for itm in ls:
                if itm == 1:
                    if x == 0:
                        add_1 = 0
                    else:
                        add_1 = grid[x-1][y] 
                    if y == 0:
                        add_2 = 0
                    else:
                        add_2 = grid[x][y-1]
                    if x == len(grid)-1:
                        add_3 = 0
                    else:
                        add_3 = grid[x+1][y]
                    if y == len(grid[0])-1:
                        add_4 = 0
                    else:
                        add_4 = grid[x][y+1] 
                    
                    totl = 4-(add_1+add_2+add_3+add_4)
                    print(totl)
                    rslt += totl
                y += 1
            x += 1
        return rslt

temp = Solution()
temp.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
temp.islandPerimeter([[0,0,1,0,0],[1,1,1,1,0],[0,0,1,0,0],[1,1,1,0,0]])
                        
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split(' ')
        r_s = str()
        for itm in s_list:
            r_s += ' {}'.format(itm[::-1])
        
        return r_s.strip()
temp = Solution()
temp.reverseWords("Let's take LeetCode contest")
                  
                  
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rslt = list()
        for num in range(n):
            num += 1
            if num%3 == 0 and num%5 == 0:
                rslt.append('FizzBuzz')
            elif num%3 == 0:
                rslt.append('Fizz')
            elif num%5 == 0:
                rslt.append('Buzz')
            else:
                rslt.append(str(num))
        return rslt
temp = Solution()
temp.fizzBuzz(15)

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        length = 0
        nums = [0] + nums + [0]
        while i < len(nums)-1:
            diff = nums[i]-nums[i+1]
            if diff == -1:
                ind_strt = i
            elif diff == 1:
                ind_end = i
                temp = ind_end-ind_strt
                length = max(temp, length)
            i += 1
        return length
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        temp = 0
        length = 0
        for num in nums:
            if num == 1:
                temp += 1
                length = max(length, temp)
            elif num == 0:
                temp = 0
        return length
temp = Solution()
temp.findMaxConsecutiveOnes([1,1,0,1,1,1])

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while 0<=len(nums):
            print('b', nums, len(nums))
            a = nums.pop(0)
            print('a',nums,a, len(nums))
#            if len(nums)==1:
#                return nums
            if a not in nums:
                return a
            nums.remove(a)
            print('c', nums)
temp = Solution()
temp.singleNumber([2,3,3,0,1,1,2])
temp.singleNumber([2,2,1])
temp.singleNumber([2,2,3,3,4])


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # For each number i in nums,
        # we mark the number that i points as negative.
        # Then we filter the list, get all the indexes
        # who points to a positive number
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])
            print(index, nums)

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
temp = Solution()
temp.findDisappearedNumbers([4,3,2,7,8,2,3,1])


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        zlen = 0
        while i <= len(nums)-1:
            if nums[i] != 0:
                nums[i], nums[i-zlen] = 0, nums[i]
            else:
                zlen += 1
            i += 1
        return None

temp = Solution()
a = [0, 1, 0, 3, 12]
temp.moveZeroes(a)
temp.moveZeroes([0, 0, 0, 3, 0, 12])

class Solution(object):
    def wordBreak(self, s, wordDict, memo={}):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not s:
            return []
        if s in worDict:
            return s
        for item in wordDict:
            if s.startswith(item):
                leftover = s[len(item):]
                reslt += ' '.format(item)
                self.wordBreak(leftover, wordDict)

s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]                
temp = Solution()
print(temp.wordBreak(s, wordDict))
                
