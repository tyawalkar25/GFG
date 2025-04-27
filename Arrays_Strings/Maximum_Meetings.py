class Solution:
    def maximumMeetings(self, a,b):
        x = sorted([(i,j) for i,j in zip(a,b)],key=lambda x: x[1])
        #print(x)
        end = x[0][1]
        count = 1
        for i in range(1,len(x)):
            if x[i][0] > end:
                count += 1
                end = x[i][1]
        return count
        
        


if __name__ == "__main__":
   ob = Solution()
   ans = ob.maximumMeetings([1, 3, 0, 5, 8, 5],[2, 4, 6, 7, 9, 9])
   print(ans)