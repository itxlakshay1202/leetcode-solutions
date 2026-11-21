class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        """
        :type purchaseAmount: int
        :rtype: int
        """
        if purchaseAmount % 10 > 4:
            purchaseAmount += 10 - purchaseAmount % 10
        else:
            purchaseAmount -= purchaseAmount % 10

        return 100 - purchaseAmount