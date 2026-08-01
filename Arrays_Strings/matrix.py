class Solution:
    def get_diagonal(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        #m,n = 0,0
        h, v = [], []
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    h.append(i)
                    v.append(j)
        for i in h:
            m = 0
            while m < cols:
                mat[i][m] = 0
                m += 1
        for j in v:
            n = 0
            while n < rows:
                mat[n][j] = 0
                n += 1                    

        for i in range(rows):
            for j in range(cols):       
                print(mat[i][j], end = " ")
            print()
                
          
        return ""

if __name__ == "__main__":
   ob = Solution()
   ans = ob.get_diagonal([[0,10,8],[7,0,8],[2,1,9]])
   print(ans)