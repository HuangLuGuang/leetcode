# -*- coding: utf-8 -*-
# @createTime    : 2019/5/31 23:44
# @author  : Huanglg
# @fileName: 整数反转.py
# @email: luguang.huang@mabotech.com
class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        res = ""
        if x[0] == "-":
            res = "-" + x[-1:0:-1]
        elif x[0] == "0" and len(x) > 1:
            res = x.replace("0", "")[::-1]
        else:
            res = x[::-1]
        res = int(res)
        if res < -2 ** 31 or res > 2 ** 31:
            res = 0
        return res
if __name__ == '__main__':
    s = Solution()
    res = s.reverse(-123)
    print(res)
