# Given an array of integers and a target sum, find the length of the longest subarray that sums to the target
# Time Complexity: O(n), Space Complexity: O(n)
class Solution:
    def getAllSubArrays(self, arr,target):
        prefix_sum_array = []
        length = 0
        sum_map = {}
        for i in range(len(arr)):
            if i == 0:
                prefix_sum_array.append(arr[i])
            else:
                prefix_sum_array.append(prefix_sum_array[i-1] + arr[i])
        for j in range(len(prefix_sum_array)): 
            prev_sum = prefix_sum_array[j] - target
            if prev_sum not in sum_map:
                sum_map[prefix_sum_array[j]] = j
            else:
                sum_map[prefix_sum_array[j]] = j
                length = max(length, (j - sum_map[prev_sum]))
                
        return length



 
if __name__ == "__main__":
   ob = Solution()
   ans = ob.getAllSubArrays([1,6],6)
   print(ans)

# expected output: 5
# prefix_sum_array = [5, 11, 6, 1, 4, 9, 12, 10, 10, 10]