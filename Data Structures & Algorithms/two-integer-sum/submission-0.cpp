class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> num_index_pair{};

        for(int i = 0; i < nums.size(); i++) {
            if (num_index_pair.find(target - nums[i]) != num_index_pair.end()) {
                return vector<int>{num_index_pair[target-nums[i]], i};
            } else {
                num_index_pair[nums[i]] = i;
            }
        }

        return vector<int>{};
    }
};
