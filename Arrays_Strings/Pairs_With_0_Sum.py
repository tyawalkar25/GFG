class Solution:
    def getPairs(self,arr):
        x = []
        n = len(arr)
        arr = sorted(arr)
        l,r = 0,n-1
        while l < r:
            sum = arr[l] + arr[r]
            if sum < 0:
                l = l+1
            elif sum > 0:
                r = r-1
            else:
                pair = [arr[l],arr[r]]
                x.append(pair)
                l = l+1
                r = r-1
                while l< r and arr[l] == arr[l-1]:
                    l = l+1
                while l< r and arr[r] == arr[r+1]:
                    r = r-1
        return x

if __name__ == "__main__":
    s = Solution()
    ans = s.getPairs([-8 ,-10, -10, -10, 10, 6, 1, 10])
    
    print(ans)