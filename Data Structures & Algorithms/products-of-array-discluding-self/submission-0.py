class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        product = 1
        non_0 = 0
        first_0 = False
        for num in nums:
            non_0 = num * non_0
            if num == 0 and not first_0:
                non_0 = product
                first_0 = True
            product = num * product

        def safe_div(a,b):
            if b != 0:
                return a // b
            return non_0

        return [safe_div(product, nums[i]) for i in range(len(nums))]