import bisect

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        result = list()
        print("sorted nums:", nums)
        for x in range(len(nums)):
            need = -nums[x]
            number = nums.pop(x)
            print("Number:", number)
            i, j = 0, len(nums)-1
            somm = nums[i] + nums[j]
            if somm == need:
                print("found", sorted([number, nums[i], nums[j]]))
                newEntry = sorted([number, nums[i], nums[j]])
                if newEntry not in result:
                    print("appended", newEntry)
                    result.append(newEntry)
                    print(result)
            while i + 1 < j:
                if somm > need:
                    j -= 1
                elif somm < need:
                    i += 1
                somm = nums[i] + nums[j]
                if somm == need:
                    print("found", sorted([number, nums[i], nums[j]]))
                    newEntry = sorted([number, nums[i], nums[j]])
                    if newEntry not in result:
                        print("appended", newEntry)
                        result.append(newEntry)
                        print(result)
                    else: i += 1

            # add the number back
            bisect.insort(nums, number)

        return result

        # nums = sorted(nums)
        # result = list()
        # for x in range(1, len(nums) -1):
        #     need, number = -nums[x], nums[x]
        #     leftList, rightList = nums[:x], nums[x:]
        #     val1, val2 = leftList.pop(0), rightList.pop()
        #     somm = val1 + val2
        #     while leftList or rightList:
        #         if somm == need:
        #             newEntry = sorted([somm, val1, val2])
        #             if newEntry not in result: result.append(newEntry)
        #             # TODO: handle equality
        #             break
        #         if somm < need and leftList:
        #             val1 = leftList.pop(0)
        #             somm = val1 + val2
        #         elif somm > need and rightList:
        #             val2 = rightList.pop()
        #             somm = val1 + val2
                
        # return result


            

