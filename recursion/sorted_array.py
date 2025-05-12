# Check if arrya is sorted.

# p -> array is sorted, sp - >

nums = [1,10,23]

def is_sorted(start,nums):

    if start==len(nums)-1:
        return True
    
    else:
        return nums[start] <= nums [start+1] and is_sorted(start+1,nums)

print(is_sorted(0,nums))