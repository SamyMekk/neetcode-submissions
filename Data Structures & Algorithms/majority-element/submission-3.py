class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        Dict={}
        current_max = nums[0]
        for element in nums:
            if element not in Dict:
                Dict[element]=1
            else:
                Dict[element]+=1
            if Dict[element] == max(Dict.values()):
                current_max = element
        return current_max
        