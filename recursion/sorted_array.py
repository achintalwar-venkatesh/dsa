# Check if arrya is sorted.

# p -> array is sorted, sp - >

nums = [1,5,8,13]

def is_sorted(idx,nums):

    if len(nums)<=1:
        return True
    
    else:
        return nums[idx] < nums [idx+1] and is_sorted(idx,nums[idx+1:])

print(is_sorted(0,nums))