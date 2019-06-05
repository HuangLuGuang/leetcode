# -*- coding: utf-8 -*-
# @createTime    : 2019/6/5 23:01
# @author  : Huanglg
# @fileName: 7_最长公共前缀.py
# @email: luguang.huang@mabotech.com
class Solution:
    """
    法一：使用zip函数
    @param: strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        # write your code here
        if strs is None or len(strs) == 0:
            return ''
        for i in range(len(strs)):
            strs[i] = list(strs[i])
        tmp = zip(*strs)
        res = ''
        for i in tmp:
            if len(set(i)) == 1:
                res += i[0]
            else:
                break
        return res

    """
    两两比较
    @param: strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix1(self, strs):
        # write your code here
        if strs is None or len(strs) == 0:
            return ''
        res = strs[0]
        for i in range(1, len(strs)):
            tmp = res
            res = ''
            for j in range(min(len(strs[i]),len(tmp))):
                if tmp[j] == strs[i][j]:
                    res += tmp[j]
                else:
                    break
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.longestCommonPrefix(["aca","cba"])
    print(res)
