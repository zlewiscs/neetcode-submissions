class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> count{};

        for (char c : s) {
            count[c]++;
        }

        for (char c : t) {
            count[c]--;
            if (count[c] < 0) {
                return false;
            }
        }

        for (auto& pair : count) {
            if (pair.second != 0) {
                return false;
            }
        }

        return true;
    }
};
