class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq_map{};

        for (auto &num : nums) {
            freq_map[num] += 1;
        }

        vector<vector<int>> ordered_freq_array(nums.size() + 1);

        for (auto &pair : freq_map) {
            ordered_freq_array[pair.second].push_back(pair.first);
        }

        vector<int> results{};
        results.reserve(k);

        for(int i = nums.size(); i > 0; i--) {
            for(int num: ordered_freq_array[i]) {
                results.push_back(num);
            }

            if (results.size() == k) {
                return results;
            }
        }

        return results;
        
    }
};
