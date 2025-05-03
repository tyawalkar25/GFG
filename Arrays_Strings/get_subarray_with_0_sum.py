# Given an array of integers, find all the subarrays with a sum of 0.
# Time Complexity: O(n^2), Space Complexity: O(n)
class Solution:
    def getAllSubArrays(self, arr):
        prefix_sum_array = []
        subarrays = []
        hashmap = {}
        n = len(arr)
        for i in range(n):
            if i == 0:
                prefix_sum_array.append(arr[i])
            else:
                prefix_sum_array.append(prefix_sum_array[i-1] + arr[i])
        for i in range(n):
            if prefix_sum_array[i] not in hashmap:
                hashmap[prefix_sum_array[i]] = [i]
            else:
                hashmap[prefix_sum_array[i]].append(i)
        for key,value in hashmap.items():
            if len(value) > 1 or key == 0:
                if key == 0:
                    for k in range(len(value)):
                        subarrays.append(arr[0:value[k]+1])
                    
                    for j in range(len(value)-1):
                        for k in range(j+1,len(value)):
                            subarrays.append(arr[value[j]+1:value[k]+1])
                else:
                    for j in range(len(value)-1):
                        for k in range(j+1,len(value)):
                            subarrays.append(arr[value[j]+1:value[k]+1])
                    

        return subarrays
                
        



 
if __name__ == "__main__":
   ob = Solution()
   ans = ob.getAllSubArrays([4,-4,8,0,7,-7])
   print(ans)

# prefix sum arrar : [4,0,8,8,15,8]
