# -*- coding: utf-8 -*-
# time:2022/11/24 16:19
# file 字符串转换整数 (atoi).py
# outhor:czy
# email:1060324818@qq.com

'''
字符串转换整数 (atoi)
请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。
函数 myAtoi(string s) 的算法如下：
读入字符串并丢弃无用的前导空格
检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被固定为 −231 ，大于 231 − 1 的整数应该被固定为 231 − 1 。
返回整数作为最终结果。
注意：
本题中的空白字符只包括空格字符 ' ' 。
除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。
示例 1：
输入：s = "42"
输出：42
解释：加粗的字符串为已经读入的字符，插入符号是当前读取的字符。
第 1 步："42"（当前没有读入字符，因为没有前导空格）
         ^
第 2 步："42"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
         ^
第 3 步："42"（读入 "42"）
           ^
解析得到整数 42 。
由于 "42" 在范围 [-231, 231 - 1] 内，最终结果为 42 。
'''

#自己写的代码
class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "" or s == '+' or s == '-':
            return 0

        for i in range(len(s)):
            if s[i] != " ":
                s = s[i:]
                break
        if s[0] == '+' and (s[1] > '9' or s[1] < '0'):
            return 0
        if s[0] == '+':
            s = s[1:]

        ans, fushu = "", False
        for i in range(len(s)):
            if s[i] == "-":
                if i != 0:
                    break
                else:
                    fushu = True
            if s[i] <= '9' and s[i] >= '0':
                ans += s[i]
            else:
                break

        if ans == "":
            return 0

        if fushu:
            ans = int("-" + ans)
            if int(ans) <= 2 ** 31 - 1 and int(ans) >= -2 ** 31:
                return int(ans)
            else:
                return -2 ** 31
        else:
            if int(ans) <= 2 ** 31 - 1 and int(ans) >= -2 ** 31:
                return int(ans)
            else:
                return -2 ** 31

#仿照别人写出来的代码
class Solution:
    def myAtoi(self, s: str) -> int:
        chars = s
        lens = len(chars)
        index = 0

        while (index < lens and chars[index] == " "):
            index += 1
        if index >= lens:
            return 0

        sign = 1
        if chars[index] == '-' or chars[index] == '+':
            if chars[index] == '-':
                sign = -1
            index += 1

        result = 0
        temp = 0

        while (index < lens):
            num = ord(chars[index]) - ord('0')
            if (num > 9 or num < 0):
                break
            temp = result
            result = result * 10 + num

            if result > 2 ** 31 - 1 or result < -2 ** 31:
                if sign > 0:
                    return 2 ** 31 - 1
                else:
                    return -2 ** 31
            index += 1

        return result * sign