# Given an array of 0s, 1s and 2s, sort the array in a single traversal.
# Time Complexity: O(n) 
# Space Complexity: O(1)
# Approach: Use three pointers to keep track of the current position of 0s, 1s and 2s.
class Solution:
    def sort012(self,arr):
        n = len(arr)
        start,current,end = 0, 0, n-1
        while current <= end:
            if arr[current] == 2:
                arr[current],arr[end] = arr[end],arr[current]
                end -= 1
            elif arr[current] == 0:
                arr[start],arr[current] = arr[current],arr[start]
                start += 1
                current += 1
            else:
                current += 1

        return arr



if __name__ == "__main__":
    ob = Solution()
    ans = ob.sort012([2,2,2,2,1,0,1,0,1,0])
    print(ans)