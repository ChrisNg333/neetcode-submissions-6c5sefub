class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(ar, L, M, R):
            left_part = ar[L:M+1]
            right_part = ar[M+1:R+1]

            i ,j = 0, 0 #ptr for each array 
            c = L   # ptr for current position

            while i < len(left_part) and j < len(right_part):
                if left_part[i] <= right_part[j]:
                    ar[c] = left_part[i]
                    i += 1
                else:   
                    ar[c] = right_part[j]
                    j += 1
                c += 1
            
            while i < len(left_part):
                ar[c] = left_part[i]
                i += 1
                c += 1
                
            while j < len(right_part):
                ar[c] = right_part[j]
                j += 1
                c += 1
            


        def mergeSort(ar, l , r):
            if l == r:
                return ar       #no more element to divide

            m = (l + r) // 2
            mergeSort(ar, l,m)
            mergeSort(ar, m+1,r)
            merge(ar,l, m, r)

            return ar

        return mergeSort(nums, 0, len(nums) - 1)




