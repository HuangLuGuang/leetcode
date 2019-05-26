# -*- coding: utf-8 -*-
# @createTime    : 2019/5/26 11:10
# @author  : Huanglg
# @fileName: 02_买卖股票的最好时机.py
# @email: luguang.huang@mabotech.com
"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

"""

class Solution:
    def maxProfit(self, prices: list) -> int:
        res = 0
        for i in range(len(prices) - 1):
            if prices[i+1] - prices[i] > 0:
               res += prices[i+1] - prices[i]
        return res

if __name__ == '__main__':
    soultion = Solution()
    res = soultion.maxProfit([1,2,3,4,5])
    print(res)
