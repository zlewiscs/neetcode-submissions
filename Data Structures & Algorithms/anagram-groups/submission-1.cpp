class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        unordered_map<string, vector<string>> result_map{};

        for (auto &str : strs) {
            vector<int> letter_count(26, 0);

            for (auto &c : str) {
                letter_count[c - 'a'] += 1;
            }

            string key{};

            for (auto &digit : letter_count) {
                key += "#" + to_string(digit);
            }

            result_map[key].push_back(str);
        }

        vector<vector<string>> res{};
        
        for (auto &pair : result_map) {
            res.push_back(pair.second);
        }

        return res;
    }
};
