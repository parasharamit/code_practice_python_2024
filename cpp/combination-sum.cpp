#include <bits/stdc++.h>

using namespace std;

void backtrack_util(vector<int> &candidates, vector<vector<int>> &res_arr, vector<int> tmp_arr, int idx, int target_sum)
{
    //base condition:
    if (target_sum==0) {
        res_arr.push_back(tmp_arr);
        return;
    } 
    else if (target_sum<0 || idx>=candidates.size()) 
        return;
    

    for (int i=idx; i<candidates.size(); i++) {
        if ((target_sum - candidates[i]) >= 0){
            
            tmp_arr.push_back(candidates[i]);
            
            backtrack_util(candidates, res_arr, tmp_arr, i, target_sum-candidates[i]);

            tmp_arr.pop_back();

        } 
    }

}

vector<vector<int>> combination_sum(vector<int> candidates, int target_sum)
{
    vector<vector<int>> res_arr;

    if (candidates.empty())
        return {};
    
    backtrack_util(candidates, res_arr, {}, 0, target_sum);

    return res_arr;


}

int main()
{
    vector<int> candidates;
    int target_sum;

    candidates = {2, 3, 6, 7};
    target_sum = 7;

    candidates = {8,7,4,3};
    target_sum = 11;

    vector<vector<int>> res_arr = combination_sum(candidates, target_sum);

    for (auto v : res_arr) {
        for (int c: v)
            cout<<c<<", ";
        cout<<endl;
    }
    
    return 0;
}