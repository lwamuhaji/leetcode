class Solution:
    memo = {}
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1
        
        sheet = [_ for _ in range(n+1)]
        sheet[0] = 0
        sheet[1] = 1
        sheet[2] = 1
        
        for i in range(3, n+1):
            sheet[i] = sheet[i-3]+sheet[i-2]+sheet[i-1]
        return sheet[n]
    
    def tribonacci2(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1
        
        if k := self.memo.get(n):
            return k
        
        self.memo[n] = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
        return self.memo[n]