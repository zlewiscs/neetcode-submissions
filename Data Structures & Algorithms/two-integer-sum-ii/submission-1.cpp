class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i = 0;
        int j = numbers.size() - 1;

        while (i < j) {
            int temp_sum = numbers[i] + numbers[j];
            if (temp_sum == target) {
                return {i + 1, j + 1};
            }

            if (temp_sum < target) {
                i += 1;
            } else {
                j -= 1;
            }
        }

        return {};
    }
};
