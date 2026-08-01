class Solution:
    def spiral(self, mat):
        rows = len(mat) 
        cols = len(mat[0]) 
        spiral = []
        top,left,bottom,right = 0,0,rows-1,cols-1
        while top <= bottom and left <= right:
            for i in range(top,right+1):
                spiral.append(mat[top][i])
            top += 1

            for i in range(top,bottom+1):
                spiral.append(mat[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right,left-1,-1):
                    spiral.append(mat[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom,top-1,-1):
                    spiral.append(mat[i][left])
                left += 1


        return spiral

if __name__ == "__main__":
   ob = Solution()
   ans = ob.spiral([[1],[2],[3],[4],[5],[6]])
   print(ans)