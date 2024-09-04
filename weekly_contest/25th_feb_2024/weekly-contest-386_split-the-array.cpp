/*
Input: nums = [1,1,2,2,3,4]
Output: true
Explanation: One of the possible ways to split nums is nums1 = [1,2,3] and nums2 = [1,2,4]. 

Input: nums = [1,1,1,1]
Output: false
Explanation: The only possible way to split nums is nums1 = [1,1] and nums2 = [1,1]. Both nums1 and nums2 do not contain distinct elements. Therefore, we return false.
*/

#include <bits/stdc++.h>
using namespace std;


class Solution {
public:
    bool isPossibleToSplit(vector<int>& nums) {
        
    }

private:
    unordered_map<int, int> count_freq(vector<int> nums) {
        unordered_map<int, int> freq_mp;
        for (int i=0; i<nums.size(); i++) {
            freq_mp[nums[i]] = 1;
        }
    }

};


int main()
{
    vector<int> nums;
    // nums = [1,2, 3, 1]
    // nums = [2,10,2,7,8,9,7,6,6,9]
    // nums = [8,9,8,5,9,3,3,1,2,1]
    nums = {1,1,2,2,3,4};
    // nums = {}

    Solution sol_obj;
    bool result = sol_obj.isPossibleToSplit(nums);
    cout<<"result -> "<<result;
}

