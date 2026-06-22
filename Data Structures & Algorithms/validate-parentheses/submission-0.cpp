class Solution {
public:
    bool isValid(string s) {
        std::stack<char> bracket_stack;
        std::unordered_map<char, char> bracket_pairs;
        bracket_pairs[')'] = '(';
        bracket_pairs[']'] = '[';
        bracket_pairs['}'] = '{';
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(' or s[i] == '[' or s[i] == '{') {
                bracket_stack.push(s[i]);
            } else if (s[i] == '}' or s[i] == ']' or s[i] == ')') {
                if (!bracket_stack.empty() && bracket_pairs[s[i]] == bracket_stack.top()) {
                    bracket_stack.pop();
                } else {
                    return false;
                }
            } else {
                return false;
            }
        }

        if (bracket_stack.size() == 0) {
            return true;
        }

        return false;
    }
};
