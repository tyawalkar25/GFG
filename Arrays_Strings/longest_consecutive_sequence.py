class Solution:
    def longest_consecutive_sequence(self, arr):
        max_len,count = 1,1
        n = len(arr)
        arr.sort()
        for i in range(n-1):
            j = i+1
            if (arr[i] + 1) == arr[j]:
                count += 1
                max_len = max(max_len,count)
            else:
                count = 1
            

        return max_len

if __name__ == "__main__":
   ob = Solution()
   ans = ob.longest_consecutive_sequence([1,2,3,4,5])
   print(ans)

#[9, -2, 4, -1, 5, -5, 0, -3, 2]