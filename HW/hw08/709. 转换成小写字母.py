class Solution1:
    def toLowerCase(self, s: str) -> str:
        return s.lower()

""" 
Time Complexity:
执行用时：32 ms, 在所有 Python3 提交中击败了 82.34% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了 27.16% 的用户
"""

class Solution2:
    def toLowerCase(self, s: str) -> str:
        """
        Method 2:
        - Using ASCII table encodding, with ord() and chr() method to convert between ascii code and character
            A-Z: 65~90
            a-z: 97~122
        - ord(A) - ord(a) = 32
        Time Complexity:
            执行用时：28 ms, 在所有 Python3 提交中击败了 93.04% 的用户
            内存消耗：15 MB, 在所有 Python3 提交中击败了 5.60% 的用户
        """
        result = "" # str is immutable type, so...
        for ch in s:
            # print(f"ch: {ch}, ord(ch): {ord(ch)}")
            if ord(ch) <= 90 and ord(ch)>=65 :
                result += chr(ord(ch) + 32)
            else:
                result += ch
        return result

class Solution:
    def toLowerCase(self, s: str) -> str:
        """
        Method 2: Use Dictionary
        """
        dic = {'A':'a', 'B':'b', 'C':'c', 'D':'d', 'E':'e', 'F':'f',
               'G':'g', 'H':'h', 'I':'i', 'J':'j', 'K':'k', 'L':'l',
               'M':'m', 'N':'n', 'O':'o','P':'p', 'Q':'q', 'R':'r',
               'S':'s', 'T':'t', 'U':'u', 'V':'v', 'W':'w', 'X':'x',
               'Y':'y', 'Z':'z'}
        result = ""
        for ch in s:
            if dic.get(ch): # .get() will return boolean if not exist
                result += dic[ch]
            else:
                result += ch
        return result

# Good reference, https://leetcode-cn.com/problems/to-lower-case/solution/709-zhuan-huan-cheng-xiao-xie-zi-mu-duo-chong-jie-/

# Method 4: Use some binary operation, if you know C/C++, refers to this blog, https://leetcode-cn.com/problems/to-lower-case/solution/ming-ming-zhi-you-26ge-zi-mu-wei-shi-yao-d2ec/