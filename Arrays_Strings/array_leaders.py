class Solution:
    def getArrayLeaders(self,arr):
        leader = []
        max = arr[-1]
        for i in arr[::-1]:
            if i >= max:
                max = i
                leader.append(i)
        
        return leader[::-1]

if __name__ == "__main__":
    s = Solution()
    ans = s.getArrayLeaders([30, 10, 10, 5])
    
    print(ans)