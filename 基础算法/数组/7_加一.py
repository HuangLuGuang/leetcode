# -*- coding: utf-8 -*-
# @createTime    : 2019/5/28 15:30
# @author  : Huanglg
# @fileName: 7_加一.py
# @email: luguang.huang@mabotech.com
class Solution:
    def plusOne(self, digits: list) -> list:
        s = ""
        for i in digits:
            s += str(i)
        num = int(s) + 1
        res = []
        res.extend(str(num))
        for i in range(len(res)):
            res[i] = int(res[i])
        return res

if __name__ == '__main__':
    s = Solution()
    res = s.plusOne([9, 9, 9])
    print(res)
