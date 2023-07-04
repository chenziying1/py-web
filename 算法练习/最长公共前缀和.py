strs = ["a","a"]

ans = ""
n = len(strs)
limits = len(min(strs))
j = 0
a = 0
flag = False
print(strs)
if "" in strs:
          print('""')
if limits == 1:
          for i in range(n-1):
                    if strs[i][a] != strs[i+1][a]:
                              flag = True
                              break
          if flag :
                    print('""')
          
          
for a in range(limits):
          if flag :
                    break
          
          for i in range(n-1):
                    if strs[i][a] != strs[i+1][a]:
                              print(ans)
                              flag = True
                              break
                    j = i
          if flag :
                    break
          #print(strs[j][a])
          #print(ans)
          ans += strs[j][a]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        premix,count = strs[0],len(strs)
        for i in range(1,count):
            premix = self.lcp(premix,strs[i])
            if not premix:
                break
        return premix
        

    def lcp(self,str1,str2):
        index,length = 0,min(len(str1),len(str2))
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]

#提交了n次，每次都出错，不是少这里就是少哪里的
#下次一定要注意特殊格式的输入
#同时 今天的横向扫描，纵向扫描一定要学会
