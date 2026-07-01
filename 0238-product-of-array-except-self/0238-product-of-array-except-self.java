class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];
        ans[0]=1;
        int prod = 1;
        for(int i=0; i<n-1;i++){
            prod = prod * nums[i];
            ans[i+1] = prod;
        }
        int pr = 1;
        for(int j=n-1; j>0; j--){
            pr = pr * nums[j];
            ans[j-1] *= pr;
        }
        return ans;

    }
}