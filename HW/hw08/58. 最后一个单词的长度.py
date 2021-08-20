class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


"""
Time Compleity:
执行用时：32 ms , 在所有 Python3 提交中击败了78.68%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了 68.42% 的用户
"""

class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        r = len(s)-1
        while s[r] == " ":
            r-=1
        if r<0:
            return None
        l = r
        # print(f"L: {l}, r:{r}")
        # print(f"s[l]: {s[l]}")
        while l >= 0 and s[l] != " ":
            l -= 1
        return (r-l)

"""
Time Compleity:
执行用时：28 ms , 在所有 Python3 提交中击败了91.46% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了 92.82% 的用户
"""