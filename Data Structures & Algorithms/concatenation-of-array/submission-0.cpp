class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int k = nums.size();
        vector<int> ans;
        for (int i = 0; i < k * 2; i++) {
            ans.push_back(nums[i % k]);
        }

        return ans;
    }
};