class Solution:
    def rearrange(self, arr):
        pos,neg = [],[]
        pos_index,neg_index,i = 0,0,0
        for n in arr:
            if n >= 0:
                pos.append(n)
            else:
                neg.append(n)
        while pos_index < len(pos) and neg_index < len(neg):
            if i % 2 == 0:
                arr[i] = pos[pos_index]
                pos_index += 1
            else:
                arr[i] = neg[neg_index]
                neg_index += 1
            i += 1
        while pos_index < len(pos):
            arr[i] = pos[pos_index]
            pos_index += 1
            i += 1
        while neg_index < len(neg):
            arr[i] = neg[neg_index]
            neg_index += 1
            i += 1
        return arr
        

if __name__ == "__main__":
   ob = Solution()
   ans = ob.rearrange([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8])
   print(ans)

#[9, -2, 4, -1, 5, -5, 0, -3, 2]