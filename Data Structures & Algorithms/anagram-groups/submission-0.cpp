class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        unordered_map<std::string, vector<string>> res_map{};

        for (auto &str : strs) {
            vector<int> letter_freq(26, 0);

            for(char c : str) {
                letter_freq[c - 'a'] += 1;
            }

            string key{};

            for(int cnt : letter_freq) {
                key += '#' + to_string(cnt);
            }

            res_map[key].push_back(str);
        }

        vector<vector<string>> results{};

        for (auto &pair : res_map) {
            results.push_back(pair.second);
        }

        return results;
    }
};
