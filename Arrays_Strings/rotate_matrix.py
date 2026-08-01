class Solution:
    def rotate(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        result = [[0] * rows for _ in range(cols)]
        #print(result)
        for i in range(rows):
            for j in range(cols):
                result[i][j] = mat[rows-1-j][i]
        mat = result
        for i in range(rows):
            for j in range(rows):
                print(mat[i][j], end  = " ")
            print()
                
          
        return ""

if __name__ == "__main__":
   ob = Solution()
   ans = ob.rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
   print(ans)