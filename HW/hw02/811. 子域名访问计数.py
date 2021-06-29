class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        """
            这题考察的有三个点：1）意识到要用HashTable的映射来解题；2）熟练掌握str和dict之间的转化；3)了解collections里可用的包
        """
        ans = {}    # Or ans = collections.Counter()
        for text in cpdomains:
            count, domain = text.split(' ') # "9001 discuss.leetcode.com" => "9001" and " discuss.leetcode.com"
            count = int(count)  # "9001" => 9001
            fragments = domain.split('.')   # "discuss.leetcode.com" => ['discuss', 'leetcode', 'com']
            for i in range(len(fragments)): # ['discuss', 'leetcode', 'com'] => {'discuss.leetcode.com': 9001, 'leetcode.com': 9001, 'com': 9001})
                key = '.'.join(fragments[i:])
                if key not in ans:
                    ans[key]=count
                else:
                    ans[key]+=count
                # ans[key] += count ==> Use this if you declared ans with collections.defaultdict(int)
        print(ans)
        return [f"{value} {key}" for key, value in ans.items()]

# 复杂度分析
# 时间复杂度：O(N)，其中 N 是数组 cpdomains 的长度，这里假设 cpdomains 中每个元素的长度都是常数级别的。
# 空间复杂度：O(N)，用于存储哈希映射。
