class Solution:
    def foo(self, long, short):
        return short * (len(long) // len(short)) == long
        
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            long, short = str1, str2
        else:
            long, short = str2, str1
        
        for i in range(len(short)):
            if self.foo(long, short[:len(short)-i]) and self.foo(short, short[:len(short)-i]):
                return short[:len(short)-i]
        return ""