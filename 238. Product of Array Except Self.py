class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right_prod = 1
        indeces = 0
        lent = len(nums)
        for i in range(lent):
            if nums[i] == 0:
                indeces += 1
            else:
                right_prod *= int(nums[i])
            
        left_prod = 1
        prod = []
        
        for i in range(lent):
            if nums[i] ==0 :
                indeces -= 1
                
            if indeces > 0:
                right = 0
                product = left_prod * right
                if nums[i] != 0:
                    right_prod = right_prod//nums[i]
            else :
                if nums[i] != 0:
                    right_prod = right_prod//nums[i]
                product = left_prod * right_prod
            left_prod = left_prod * nums[i]
            prod.append(int(product))
        return prod