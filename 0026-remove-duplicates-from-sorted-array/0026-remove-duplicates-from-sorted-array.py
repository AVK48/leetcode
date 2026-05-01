class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Start the write pointer at the second element
        insert_index = 1
        
        # Iterate from the second element to the end
        for i in range(1, len(nums)):
            # If the current element is different from the previous one, it's unique
            if nums[i] != nums[i - 1]:
                nums[insert_index] = nums[i]
                insert_index += 1
        
        # insert_index represents the count of unique elements
        return insert_index