'''
两个数组的交集 II
给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]

判断那一边数比较大，采用小的那个数组中的值去大的数组中判断存不存在，存在 将其变成已经被访问过的状态，以免重复访问

力扣中存在一种思路，先排序，后采用双指针的方法

emmm 对于py而言，两种效果都不是很好，本来还期待着第二种能够一鸣惊人，是我想多了
'''

def test(nums1,nums2):
        n,m = len(nums1),len(nums2)
        ans = []
        if n > m :
            for i in nums2:
                if i in nums1:
                    nums1[nums1.index(i)] = -1
                    ans.append(i)
            return ans
        elif m > n:
            for i in nums1:
                if i in nums2:
                    nums2[nums2.index(i)] = -1
                    ans.append(i)
            return ans
        else:
            for i in nums1:
                if i in nums2:
                    nums1[nums1.index(i)] = -1
                    ans.append(i)
            return ans

def test2(nums1,nums2):
          nums1.sort()
          nums2.sort()
          i,j = 0,0
          ans = []
          while i < len(nums1) and j < len(nums2):
                    if nums1[i] > nums2[j]:
                              j += 1
                    elif nums1[i] < nums2[j] :
                              i += 1
                    else:
                              ans .append(nums1[i])
                              i += 1
                              j += 1
          print(ans)

nums1 = [1,2,2,1]
nums2 = [2,2]
test2(nums1,nums2)
