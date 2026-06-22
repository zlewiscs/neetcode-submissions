class Solution {
public:

    string encode(vector<string>& strs) {
        string results{};
        for (auto &str : strs) {
            results += to_string(str.length()) + '#' + str;
        }

        return results;
    }

    vector<string> decode(string s) {
        vector<string> results{};

        int i = 0;
        while (i < s.size()) {
            int j = i;
            int len = 0;
            while(s[j] != '#') {
                len = len * 10 + int(s[j] - '0');
                j += 1;
            }

            i = j + 1;
            j = i + len;

            results.push_back(s.substr(i, len));
            i = j;
        }

        return results;
    }
};
