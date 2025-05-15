# Given an array of 0s and 1s, find the length of the longest subarray with equal number of 0s and 1s.
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def getAllSubArrays(self, arr):
        length = 0
        sum_map = {}
        prefix_sum_array = []
        for i in range(len(arr)):
            if arr[i] == 0:
                arr[i] = -1
        for i in range(len(arr)):
            if i == 0:
                prefix_sum_array.append(arr[i])
            else:
                prefix_sum_array.append(prefix_sum_array[i-1] + arr[i])
        
        for j in range(len(prefix_sum_array)):
            if prefix_sum_array[j] == 0:
                length = max(length,j+1)
            if prefix_sum_array[j] not in sum_map:
                sum_map[prefix_sum_array[j]] = j
            else:
                length = max(length , j - sum_map[prefix_sum_array[j]])
        return length


 
if __name__ == "__main__":
   ob = Solution()
   ans = ob.getAllSubArrays([1,0,1,0])

   print(ans)