class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] fpAr = new int[n];
        fpAr[0] = 1;
        int[] bpAr = new int[n];
        bpAr[n-1] = 1;
        int[] ans = new int[n];
        int fp = 1;
        for(int i = 0; i<n-1; i++){
            fp = fp * nums[i];
            fpAr[i+1] = fp;
        }
        int bp = 1;
        for(int j = n-1; j>=1; j--){
            bp = bp * nums[j];
            bpAr[j-1] = bp;
        }
        for(int i=0; i<n; i++){
            ans[i]=fpAr[i]*bpAr[i];
        }
        System.out.println(Arrays.toString(fpAr));
        System.out.println(Arrays.toString(bpAr));
        return ans;

    }
}