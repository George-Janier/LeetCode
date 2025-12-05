class Solution {
    public boolean isPalindrome(int x) {
        String str = Integer.toString(x);
        StringBuilder res = new StringBuilder();
        res.append(str);
        res.reverse();
        if (res.toString().equals(str)) {
            return true;
        }
        return false;
    }
}