class Solution:
    def rotate(self,arr,k):
        n = len(arr)-1
        while k > 0:
            arr.insert(0,arr[n])
            k -= 1
            arr.pop()
        return arr


if __name__ == "__main__":
    s = Solution()
    ans = s.rotate([1,2,3,4,5],3)

    print(ans)