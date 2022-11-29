'''
移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。

 

示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:

输入: nums = [0]
输出: [0]

1.用两个数组将内容及顺序存储并替换掉原来的数组
2.把非0的往前挪,在最后再将多余的部分置零
3.双指针，这里可以参照双指针的思路解决，指针j是一直往后移动的，如果指向的值不等于0才对他进行操作。
  而i统计的是前面0的个数，我们可以把j-i看做另一个指针，它是指向前面第一个0的位置，然后我们让j指向的值和j-i指向的值交换
（无论在时间，内存上都具备优势）

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp1,temp2 = [],[]
        for i in range(len(nums)):
            if nums[i] == 0:
                temp1.append(0)
            else:
                temp2.append(nums[i])
        target = temp2+temp1
        for i in range(len(target)):
            nums[i] = target[i]
'''
        

def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return
        else:
            index = 0
            for i in nums:
                if i != 0:
                    nums[index] = i
                    index += 1
            while index < n:
                nums[index] = 0
                index += 1

def moveZeroes2(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return
        else:
            i = 0
            for j in range(n):
                if nums[j] == 0:
                    i += 1
                elif i != 0:
                    nums[j-i] = nums[j]
                    nums[j] = 0
