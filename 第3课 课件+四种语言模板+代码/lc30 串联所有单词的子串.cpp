class Solution {
public:
    // 不要把所有的code都放到一个function里，要学会modularize（模块化)
    vector<int> findSubstring(string s, vector<string>& words) {
        wordsMap = countWords(words);
        int tot = words.size() * words[0].size();
        vector<int> ans;
        // 枚举开始位置，考虑所有可能的子串
        for (int start = 0; start + tot <= s.length(); start++) {
            if (isSame(s.substr(start, tot), words)) {
                ans.push_back(start);
            }
        }
        return ans;
    }

private:
    unordered_map<string, int> wordsMap;

    // 想判断一个字符串t，是否由words拼成,e.g., is "foobar" made of ["foo", "bar"]？
    // 把t分解成若干个单词，然后看跟words数组是否相同（顺序无关）
    bool isSame(string t, vector<string>& words) {
        // cout << "isSame: " << t << " and words" << endl;
        int m = words[0].length(); // 每个单词的长度
        unordered_map<string, int> tMap; // 单词出现次数
        // 把t，每m个字符分解成一个单词
        // foothe 分解为 foo, the
        for (int i = 0; i < t.length(); i += m) {
            // i开始的m个字符，组成一个单词
            tMap[t.substr(i, m)]++;
        }
        return equals(tMap, wordsMap);
    }

    // 判断两个map是否一样的方法:1) 先比较size，再看a是否是b的subset; 2) if a is subset of b and b is subset of a, then a == b
    // a.size() == b.size()
    // a里面有的b里全有，且值一样
    bool equals(unordered_map<string, int>& a, unordered_map<string, int>& b) {
        if (a.size() != b.size()) return false;
        for (auto& key_value_pair : a) {
            auto& key = key_value_pair.first;
            auto& value = key_value_pair.second;
            // 如果b里面没有，或者value不相等（次数不一样）
            if (b.find(key) == b.end() || value != b[key]) return false;
        }
        return true;
    }

    // 用题目给的单词vector，来搭建一个map，e.g., ["foo", "bar"] ==> {"foo": 1, "bar": 2}
    unordered_map<string, int> countWords(vector<string>& words) {
        unordered_map<string, int> ans;
        for (string& word : words) {
            ans[word]++;
        }
        return ans;
    }
};

//bar foo
//arf oot
//rfo oth
//...