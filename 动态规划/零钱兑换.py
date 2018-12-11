'''
此题python提交会显示超时，但是用java不会出现超时（同样的代码）
'''
import datetime
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        opt = []
        for i in range(amount+1):
            opt.append(amount+1)
        opt[0] = 0
        for coin in coins:
            for i in range(coin,amount+1):
                opt[i] = min(opt[i-coin]+1,opt[i])
        if opt[amount] == amount+1:
            return -1
        else:
            return opt[amount]



if __name__ == '__main__':
    start = datetime.datetime.now()
    solution = Solution()
    coins = [146,66,355,93,255,152,225,244,168,205]
    amount = 8069
    result = solution.coinChange(coins,amount)
    end = datetime.datetime.now()
    print(result)
    print('程序运行时间为：', end - start)