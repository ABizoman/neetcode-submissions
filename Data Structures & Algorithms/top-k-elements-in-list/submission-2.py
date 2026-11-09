class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = dict()

        nums = sorted(nums)
        for number in nums:
            current = counts.get(number, 0)
            current += 1
            counts[number] = current


        full_result = sorted(counts, key=lambda x: counts[x])
        print(full_result)

        return full_result[len(full_result) - k:]