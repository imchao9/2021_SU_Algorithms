[TOC]



# 第 16 课：字符串处理



## **Overview:**

- 面试一大考点
- 不复杂，但灵活多变，细节较多，容易出错
- 实际应用中也比较普遍
- 属于孰能生巧的一系列题目
- 只能多练习，尽量别挂在这上面





## **字符串基本知识**

- 遍历字符串

```python
for ch in chars:
    print(ch)
    
# with index
for i in range(len(chars)):
    print(chars[i])
```

- 字符串比较

```python
return x==y
```

- Common string methods:

Modification:

| Methods                                                      | Description                                                  | Signature |
| ------------------------------------------------------------ | ------------------------------------------------------------ | --------- |
| [capitalize()](https://www.w3schools.com/python/ref_string_capitalize.asp) | Converts the first character to upper case, e.g., “hello” ==> “Hello” |           |
| [casefold()](https://www.w3schools.com/python/ref_string_casefold.asp) | Converts string into lower case, e.g,  "HEllO".casefold() ==> “hello” |           |
| [upper()](https://www.w3schools.com/python/ref_string_upper.asp) | Converts a string into upper case                            |           |
| [lower()](https://www.w3schools.com/python/ref_string_lower.asp) | Converts a string into lower case                            |           |
| [title()](https://www.w3schools.com/python/ref_string_title.asp) | Converts the first character of each word to upper case      |           |
| [swapcase()](https://www.w3schools.com/python/ref_string_swapcase.asp) | Swaps cases, lower case becomes upper case and vice versa    |           |
|                                                              |                                                              |           |
| [strip()](https://www.w3schools.com/python/ref_string_strip.asp) | Returns a trimmed version of the string                      |           |
| [split()](https://www.w3schools.com/python/ref_string_split.asp) | Splits the string at the specified separator, and returns a list |           |
| [partition()](https://www.w3schools.com/python/ref_string_partition.asp) | Returns a tuple where the string is parted into three parts  |           |
| [replace()](https://www.w3schools.com/python/ref_string_replace.asp) | Returns a string where a specified value is replaced with a specified value |           |
| [join()](https://www.w3schools.com/python/ref_string_join.asp) | Converts the elements of an iterable into a string           |           |



Data type Checking:

| Methods                                                      | Signature                                                    | Description                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------------------------------------------- |
| [endswith()](https://www.w3schools.com/python/ref_string_endswith.asp) |                                                              | Returns true if the string ends with the specified value |
| [isalnum()](https://www.w3schools.com/python/ref_string_isalnum.asp) | Returns True if all characters in the string are alphanumeric |                                                          |
| [isalpha()](https://www.w3schools.com/python/ref_string_isalpha.asp) | Returns True if all characters in the string are in the alphabet |                                                          |
| [isascii()](https://www.w3schools.com/python/ref_string_isascii.asp) | Returns True if all characters in the string are ascii characters |                                                          |
| [isdecimal()](https://www.w3schools.com/python/ref_string_isdecimal.asp) | Returns True if all characters in the string are decimals    |                                                          |
| [isspace()](https://www.w3schools.com/python/ref_string_isspace.asp) | Returns True if all characters in the string are whitespaces |                                                          |
| [istitle()](https://www.w3schools.com/python/ref_string_istitle.asp) | Returns True if the string follows the rules of a title      |                                                          |
| [isupper()](https://www.w3schools.com/python/ref_string_isupper.asp) | Returns True if all characters in the string are upper case  |                                                          |

Searching, Identificaiton

| Methods                                                      | Signature                           | Description                                                  |
| ------------------------------------------------------------ | ----------------------------------- | ------------------------------------------------------------ |
| [count()](https://www.w3schools.com/python/ref_string_count.asp) |                                     | Returns the number of times a specified value occurs in a string, e.g., "apple".count("p") |
| [find()](https://www.w3schools.com/python/ref_string_find.asp) | *string*.find(*value, start, end*)  | Returns the position of where it was found; returns -1 if the value is not found. |
| [rfind()](https://www.w3schools.com/python/ref_string_rfind.asp) | *string*.rfind(*value, start, end*) | returns the last position of where it was found, 返回最后一个matched char， or右边开始数得最后一个 |
| [format()](https://www.w3schools.com/python/ref_string_format.asp) |                                     | Formats specified values in a string, e.g., txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)<br/>txt2 = "My name is {0}, I'm {1}".format("John",36)<br/>txt3 = "My name is {}, I'm {}".format("John",36) |



## 基础问题练习：

- [转换成小写字母](https://leetcode-cn.com/problems/to-lower-case/)（Easy）半年内出题频次：

| Amazon |
| :----: |
|   2    |

Code:

```python
class Solution(object):
    def toLowerCase2(self, s):
        """
        :type s: str
        :rtype: str
        Idea1:
            just use s.lower()
        Idea2:
            manually checking, char by char. If ch.isupper() --> convert to lower and append to result_s, otherwise, directly append to the end
        """
        return s.lower()
    def toLowerCase(self, s):
        result_s = ""
        diff = ord('a') - ord('A')
        for ch in s:
            ascii_ch = ord(ch)
            if ascii_ch <= ord("Z") and ascii_ch >= ord('A'):
                result_s += chr(ascii_ch+diff)
            else:
                result_s += ch
        return result_s
```

Summary: N/A





- [最后一个单词的长度](https://leetcode-cn.com/problems/length-of-last-word/)（Easy）半年内出题频次：

| Google |
| :----: |
|   2    |

Code:

```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split()[-1])
```

Summary: N/A





- [宝石与石头](https://leetcode-cn.com/problems/jewels-and-stones/)（Easy）半年内出题频次：

| Amazon |
| :----: |
|   4    |



Code:

```python

```



Summary:





- [字符串中的第一个唯一字符](https://leetcode-cn.com/problems/first-unique-character-in-a-string/)（Easy）半年内出题频次：

| Facebook | 思爱普 | 微软 | Amazon |
| :------: | :----: | :--: | :----: |
|    10    |   2    |  9   |   13   |

| Google | Apple |
| :----: | :---: |
|   3    |   5   |

Code:

```python
class Solution(object):
    """
        Idea：The most simple idea is to use hash table, where we count the number of occurance of each char, and return the first 1 in hashtable, if no 1, return -1. 
            - 时间复杂度：O(n)，其中 n 是字符串 s 的长度。我们需要进行两次遍历。
        Idea 都一样的，就是用不同的方法来实现罢了。这题也正好练习下python collections 里的不同的datatypes
    """
    def firstUniqChar1(self, s):
        """
        :type s: str
        :rtype: int
            With collections.Counter()
        """
        from collections import Counter
        counter = Counter(list(s))
        print(counter)
        for i, ch in enumerate(s):
            if counter[ch] == 1:
                return i
        return -1
        # for key, value in counter.items():
        #     if value = 1
            # print(key, value)


    def firstUniqChar2(self, s):
        """
            Just dict()
        """
        dic = {}
        # Count the frequence for each char
        for ch in s:
            if ch in dic:
                dic[ch] = dic[ch] + 1
            else:
                dic[ch] = 1
        # 过滤出现次数不为一的字符
        unique_chars = [k for k, v in filter(lambda kvp: kvp[1] == 1, dic.items())]
        # 遍历目标字符串，返回首个出现在unique_chars中的字符的索引
        for i, c in enumerate(s):
            if c in unique_chars:
                return i
        return -1

    def firstUniqChar3(self, s):
        """
            字典 dict() +集合 set(): with str.count('s') and set() methods
        """
        dic = {c: s.count(c) for c in set(s)}
        print(dic)
        for i, ch in enumerate(s):
            if dic[ch] == 1:
                return i
        return -1
```



Summary:

- Method1: Use collections.Counter(),  count the frequency for each ch, and return the index of first unique ch.
  - `for i, ch in enumerate(s):`

- Method 2: Use dict(), counting the frequency yourself
- Method 3: Use dict() and set()
  - `dic = {c: s.count(c) for c in set(s)}`



- [最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix/description/)（Easy）半年内出题频次：

| Facebook | 字节跳动 | 微软 | Amazon |
| :------: | :------: | :--: | :----: |
|    17    |    16    |  7   |   17   |

| 华为 | 百度 | Google | PayPal |
| :--: | :--: | :----: | :----: |
|  3   |  3   |   6    |   2    |

| 美团 | Apple |
| :--: | :---: |
|  2   |   6   |



Code:

```python

```



Summary:





#### 字符串操作

- [反转字符串](https://leetcode-cn.com/problems/reverse-string/)（Easy）半年内出题频次：

| PayPal | 字节跳动 | 微软 | Amazon |
| :----: | :------: | :--: | :----: |
|   2    |    2     |  4   |   4    |

| Cisco | Apple |
| :---: | :---: |
|   2   |   6   |



Code:

```python

```



Summary:





- [翻转字符串里的单词](https://leetcode-cn.com/problems/reverse-words-in-a-string/)（Medium）半年内出题频次：

| Facebook | 字节跳动 | 微软 | Amazon |
| :------: | :------: | :--: | :----: |
|    3     |    3     |  12  |   2    |

| 百度 | 腾讯 | Cisco | PayPal |
| :--: | :--: | :---: | :----: |
|  2   |  2   |   2   |   2    |



Code:

```python

```



Summary:





- [仅仅反转字母](https://leetcode-cn.com/problems/reverse-only-letters/)（Easy）半年内出题频次：

| 微软 | Apple |
| :--: | :---: |
|  3   |   3   |



Code:

```python

```



Summary:







