class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> hash_table{};

        for (auto &num : nums) {
            if (hash_table.find(num) != hash_table.end()) {
                return true;
            }

            hash_table.insert(num);
        }

        return false;
    }
};