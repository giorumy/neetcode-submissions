class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> checked; //index, difference
        for(int i=0; i< nums.size(); i++){
            if (checked.contains(nums[i])){
                return {checked[nums[i]], i};
            }
            int difference = target - nums[i];
            checked[difference] = i;
        }
        return {0,0};
    }
};
