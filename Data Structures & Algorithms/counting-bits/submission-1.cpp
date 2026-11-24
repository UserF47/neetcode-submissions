class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> res;
        for(int i = 0; i <= n; i++) {
            int x = i;
            int bit_ones = 0;
            while(x != 0) {
                bit_ones += x & 1;
                x = x >> 1;
            }
            res.push_back(bit_ones);
        }

        return res;
    }
};
