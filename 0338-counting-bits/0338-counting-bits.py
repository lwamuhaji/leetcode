class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(n+1):
            count = 0
            while i:
                if i % 2:
                    count += 1
                i //= 2
            answer.append(count)
        return answer