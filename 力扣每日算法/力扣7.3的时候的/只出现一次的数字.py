'''
只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

输入: [2,2,1]
输出: 1

输入: [4,1,2,1,2]
输出: 4

1.用字典来保存数组里面的数及数的次数

2.根据力扣题解还有两种思路
          异或运算  异或运算，相异为真，相同为假，所以 a^a = 0 ;0^a = a
                    因为异或运算 满足交换律 a^b^a = a^a^b = b 所以数组经过异或运算，单独的值就剩下了
          位运算 异或运算的另一种解释
'''
def test(nums):
          ans = {}
          for i in nums:
                    if i not in ans:
                              ans[i] = 1
                    else:
                              ans[i] += 1
          for i,j in ans.items():
                    if j == 1:
                              return i

def test2(nums):
          ans = 0
          for i in nums:
                    ans = ans ^ i
          return ans

nums = [2,2,1]
print(test2(nums))


