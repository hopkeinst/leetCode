class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        List = []
        solved = False
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    List.append(i)
                    List.append(j)
                    solved = True
                    break
            if(solved == True):
                break
        return List