class Solution {
public:
    int reverse(int x) {
        int res = 0;

        while(x != 0) {
            int i = x % 10;
            x = x / 10;

            if (res > INT_MAX / 10 or res < INT_MIN / 10) return 0;

            res = res * 10 + i;
        }

        return res;

    }
};
