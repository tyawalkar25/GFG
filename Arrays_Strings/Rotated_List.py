class Solution:
    def rotateCount(self,l):
        low,high = 0, len(l)-1
        while low <= high:
            mid = (low+high)//2
            if (l[mid-1] < l[mid] ):
                low = mid+1
            elif (l[mid-1] > l[mid]):
                return mid
        return 0

if __name__ == "__main__":
    s = Solution()
    ans = s.rotateCount([1,2,3])

    print(ans)

    [1,2,3]
    [3,1,2]
    [2,3,1]