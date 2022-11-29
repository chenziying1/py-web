'''
给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]

输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释: 
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]

提示：

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

解:
三种情况
k小于数组全长 相当于将数组从后数k个数接到前面去
k大于数组全长 相当于将数据从后数n-k个数接到前面去
k等于数组全长 不变

'''

def test(nums,k):
          n = len(nums)
          if n > k:
                    temp1 = nums[n-k:]
                    temp2 = nums[:n-k]
                    nums2 = temp1+temp2
                    for i in range(len(nums2)):
                              nums[i] = nums2[i]
          elif n < k:
                    temp1 = nums[n-(k-n):]
                    temp2 = nums[:n-(k-n)]
                    nums2 = temp1+temp2
                    for i in range(len(nums2)):
                              nums[i] = nums2[i]
          return nums

nums = [1,2,3,4]
ans = test(nums,2)
print(ans)
          
