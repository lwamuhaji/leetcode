class Solution:
    def compress(self, chars: List[str]) -> int:
        prev = chars[0]
        count = 0
        chars.append('')
        write = 0
        for i, now in enumerate(chars):
            if now == prev:
                count += 1
            else:
                chars[write] = prev
                write += 1
                
                if count > 1:
                    for n in str(count):
                        chars[write] = n
                        write += 1
                
                prev = now
                count = 1
        return write