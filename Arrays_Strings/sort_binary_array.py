# sort a binarty array in place in linear time
# Time complexity: O(n)
# Space complexity: O(1)
# Approach: use two pointers, one from the start and one from the end of the array.
class Solution:
    def sortBinaryArray(self, arr):
        n = len(arr)
        i,j = 0,n-1
        while i < j:
            if arr[i] == 1 and arr[j] == 0:
                arr[i],arr[j] = arr[j],arr[i]
                i += 1
                j -= 1
            elif arr[i] == 0:
                i += 1
            else:
                j -= 1
        return arr        



 
if __name__ == "__main__":
   ob = Solution()
   ans = ob.sortBinaryArray([1,0,0,0,1])
   print(ans)