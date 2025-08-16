class Solution:
    def merge_two_sorted_arrays(self, nums1,nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        result = []
        i,j = 0,0
        while i < n1 and j < n2:
            if nums1[i] <= nums2[j]:
                if nums1[i] not in result:
                    result.append(nums1[i])
                i += 1
            else:
                if nums2[j] not in result:
                    result.append(nums2[j])
                j += 1
        while i < n1:
            if nums1[i] not in result:
                result.append(nums1[i])
            i += 1
        while j < n2:
            if nums2[j] not in result:
                result.append(nums2[j])
            j += 1

        return result

                
                
if __name__ == "__main__":
   ob = Solution()
   ans = ob.merge_two_sorted_arrays([1,1,1],[2,2,2,2,2,2])
   print(ans)

# 1,2,3,4,6,7,8,9,10