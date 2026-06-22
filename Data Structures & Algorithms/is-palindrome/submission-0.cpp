class Solution {
public:
    bool isPalindrome(string s) {
        int p = 0;
        int q = s.size() - 1;

        while (p < q) {
            while (p < q && !std::isalnum((unsigned char)s[p])) ++p;
            while (p < q && !std::isalnum((unsigned char)s[q])) --q;

            if (std::tolower((unsigned char)s[p]) != std::tolower((unsigned char)s[q])) return false;

            ++p;
            --q;
        }

        return true;
    }
};
