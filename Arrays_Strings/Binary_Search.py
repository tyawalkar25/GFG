# Time Complexity - O(log N)
class Solution:
    def binarysearch(self,arr,k):
        #arr = list(dict.fromkeys(arr))
        n = len(arr)
        l,r = 0, n-1
        while(l <= r):
            m = (l+r)//2
            if (k < arr[m]):
                r = m-1
            elif (k > arr[m]):
                l = m+1
            else:
                if (m-1) < 0:
                    return m
                if (arr[m-1]) != k:
                    return m
                r = m-1
        return -1
        

if __name__ == "__main__":
    s = Solution()
    ans = s.binarysearch([1,2,3,4,5],4)
    
    print(ans)