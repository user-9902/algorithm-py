NUMS1 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five',
         'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

NUMS2 = ['Twenty', 'Thirty', 'Forty', 'Fifty',
         'Sixty', 'Seventy', 'Eighty', 'Ninety']
NUMS3 = ['Hundred', 'Thousand', 'Million', 'Billion']


class Solution:
    def numberToWords(self, num: int) -> str:

        def dfs(n):
            if n <= 19:
                return NUMS1[n]

            if n < 100:
                res = NUMS2[(n // 10) - 2]
                n %= 10
                if n:
                    res += ' ' + dfs(n)
                return res

            if n < 1000:
                res = NUMS1[n // 100] + ' Hundred'
                n %= 100
                if n:
                    res += NUMS1[n // 100] + dfs(n)
                return res + ' ' + dfs(n)
            if n < 1000_000:
                return
            if n < 1000_000_000:
                return

        return dfs(num)


a = Solution().numberToWords(101)
print(a)
