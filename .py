class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        for k in range(len(nums)):
            for i in range(k + 1, len(nums)):
                if nums[k] + nums[i] == target:
                    out.append(k)
                    out.append(i)
        return out