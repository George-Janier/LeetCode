class Solution {
    public int removeDuplicates(int[] nums) {
        int n = nums.length;
        Set<Integer> s = new HashSet<>();
        int uni = 0;
        for(int i = 0; i<n ; i++){
            if(!s.contains(nums[i])){
                s.add(nums[i]);
                nums[uni]=nums[i];
                uni++;
            }
        }
        return uni;
    }
}