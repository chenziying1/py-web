# -*- coding: utf-8 -*-
# time:2022/11/23 14:31
# file 整数反转.py
# outhor:czy
# email:1060324818@qq.com

'''
整数反转
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围[−231,231 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。
示例 1:
输入：x = 123
输出：321
'''

#自己最开始的代码，没有运行成功，还浪费了大量时间，是我们一开始就想歪了，想用整数转字符串，正确的解法应该是用
class Solution:
    def reverse(self, x: int, ans=None) -> int:
        n = str(x)
        if len(str(x)) > 1 and "-" in str(x) and n[-1] != "0":
            ans = int("-"+n[1:][::-1])
            if ans < 2147483647:
                return ans
            else:
                return 0
        elif len(str(x)) > 1 and "-" in str(x) and n[-1] == "0":
            return int("-"+n[1:-1][::-1])
            if ans < 2147483647:
                return ans
            else:
                return 0
        elif len(str(x)) > 1 and n[-1] != "0":
            return int(n[::-1])
            if ans < 2147483647:
                return ans
            else:
                return 0
        elif len(str(x)) > 1 and n[-1] == "0":
            return int(n[:-1][::-1])
            if ans < 2147483647:
                return ans
            else:
                return 0
        else:
            if ans < 2147483647:
                return ans
            else:
                return 0



#参考别人代码写出来的，负数采用字符串，不为零且大于0就正常数字反转
def s_reverse(x):
    res = 0
    if x < 0:
        x_rev = str(x)[1:]
        x_rev = x_rev[::-1]
        if -2 ** 31 <= int('-' + x_rev) <= 2 ** 31 - 1:
            return int('-' + x_rev)
        return 0
    while (x != 0):
        t = x % 10
        newres = res * 10 + t
        if ((newres - t)) / 10 != res:
            return 0
        res = newres
        x = x // 10
    if -2 ** 31 <= res <= 2 ** 31 - 1:
        return res
    return 0

ans = s_reverse(3)
print(ans)

