class Solution:
    def minDist(self, arr,x,y):
        if x in arr and y in arr:
            ind_x = [i for i,a in enumerate(arr) if a == x]
            ind_y = [i for i,a in enumerate(arr) if a == y]
        else:
            return -1
        ind = [(i,j) for i in ind_x for j in ind_y]
        #return ind
        return min([abs(t[1] - t[0]) for t in ind])

        

if __name__ == "__main__":
   ob = Solution()
   ans = ob.minDist([10, 20, 30, 40, 50],10,50)
   print(ans)

   