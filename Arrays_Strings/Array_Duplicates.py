class Solution:
    def getArrayDuplicates(self,arr):
        s = set()
        dup = []
        for i in arr:
            if i in s:
                dup.append(i)
            else:
                s.add(i)
        return list(set(dup))

if __name__ == "__main__":
    s = Solution()
    ans = s.getArrayDuplicates([2, 3, 1, 2, 3,3])
    
    print(ans)