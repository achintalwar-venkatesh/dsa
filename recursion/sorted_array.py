# Check if arrya is sorted.

# p -> array is sorted, sp - >

nums = [1,0]

def is_sorted(start,end,nums):

    if start==end:
        return True
    
    else:
        return nums[start] <= nums [start+1] and is_sorted(start+1,end,nums)

print(is_sorted(0,len(nums)-1,nums))