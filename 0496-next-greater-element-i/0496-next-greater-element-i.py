class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        st = []
        res = [-1] * len(nums2)

        for i, e in enumerate(nums2):
            while st and nums2[st[-1]] < e:
                res[st.pop()] = e
            st.append(i)

        ans = []
        for x in nums1:
            for j, n in enumerate(nums2):
                if x == n:
                    ans.append(res[j])
                    break

        return ans