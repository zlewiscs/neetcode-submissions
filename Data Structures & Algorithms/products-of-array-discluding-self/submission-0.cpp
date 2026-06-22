class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> results(nums.size(), 1);

        // compute prefix
        int pre = 1;
        for (int i = 0; i < nums.size(); i++) {
            results[i] = pre;
            pre = pre * nums[i];
        }

        // compute suffix
        int suf = 1;
        for (int i = nums.size() - 1; i >= 0; i--) {
            results[i] = suf * results[i];
            suf = suf * nums[i];
        }

        return results;
    }
};
